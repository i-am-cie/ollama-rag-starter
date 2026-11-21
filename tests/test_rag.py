from unittest.mock import Mock, patch

import numpy as np

import rag


# ---------- load_documents ----------

def test_load_documents_reads_txt_and_md(tmp_path):
    (tmp_path / "a.txt").write_text("hello", encoding="utf-8")
    (tmp_path / "b.md").write_text("# doc", encoding="utf-8")
    (tmp_path / "c.py").write_text("print(1)", encoding="utf-8")

    docs = rag.load_documents(str(tmp_path))
    names = {name for name, _ in docs}
    assert names == {"a.txt", "b.md"}
    assert dict(docs)["a.txt"] == "hello"


def test_load_documents_empty_dir(tmp_path):
    assert rag.load_documents(str(tmp_path)) == []


# ---------- chunk_text ----------

def test_chunk_short_text_single_chunk():
    chunks = rag.chunk_text("short text", size=500, overlap=80)
    assert chunks == ["short text"]


def test_chunk_empty_text_returns_empty():
    assert rag.chunk_text("") == []


def test_chunk_produces_overlapping_chunks():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunks = rag.chunk_text(text, size=10, overlap=3)
    assert len(chunks) > 1
    # 相邻两块应有重叠字符
    assert chunks[0][-3:] == chunks[1][:3]


def test_chunk_strips_whitespace():
    chunks = rag.chunk_text("   padded text   ", size=500, overlap=80)
    assert chunks == ["padded text"]


# ---------- retrieve ----------

def test_retrieve_ranks_most_similar_first():
    corpus = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32)
    query = np.array([[0, 1, 0]], dtype=np.float32)
    idxs, scores = rag.retrieve(query, corpus, top_k=3)
    assert idxs[0] == 1
    assert scores[0] > scores[-1]


def test_retrieve_respects_top_k():
    rng = np.random.default_rng(0)
    corpus = rng.random((5, 4), dtype=np.float32)
    query = rng.random((1, 4), dtype=np.float32)
    idxs, scores = rag.retrieve(query, corpus, top_k=2)
    assert len(idxs) == 2
    assert len(scores) == 2


# ---------- embed ----------

def test_embed_calls_ollama_and_returns_array():
    fake_resp = {"embeddings": [[1, 2, 3], [4, 5, 6]]}
    with patch.object(rag.ollama, "embed", return_value=fake_resp) as mock_embed:
        result = rag.embed(["first", "second"])

    mock_embed.assert_called_once_with(model=rag.EMBED_MODEL, input=["first", "second"])
    assert result.shape == (2, 3)
    assert result.dtype == np.float32


# ---------- build_index ----------

def test_build_index_chunks_and_sources(tmp_path):
    (tmp_path / "doc.txt").write_text("one two three four five", encoding="utf-8")

    def fake_embed(texts):
        return np.zeros((len(texts), 4), dtype=np.float32)

    with patch.object(rag, "embed", side_effect=fake_embed):
        chunks, emb = rag.build_index(str(tmp_path))

    assert chunks, "应至少生成一个块"
    assert all(isinstance(c, tuple) and len(c) == 2 for c in chunks)
    assert chunks[0][0] == "doc.txt"
    assert emb.shape[0] == len(chunks)


def test_build_index_empty_dir_raises_systemexit(tmp_path):
    try:
        rag.build_index(str(tmp_path))
        assert False, "空目录应抛出 SystemExit"
    except SystemExit:
        pass


# ---------- answer ----------

def test_answer_builds_prompt_and_returns_content():
    chunks = [("doc.txt", "本地 RAG 的原理"), ("other.md", "无关内容")]
    corpus_emb = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=np.float32)

    fake_chat = {"message": {"content": "这是答案"}}
    with patch.object(rag, "embed", return_value=np.array([[1, 0, 0, 0]], dtype=np.float32)), \
            patch.object(rag.ollama, "chat", return_value=fake_chat) as mock_chat:
        content, idxs, scores = rag.answer("什么是 RAG？", chunks, corpus_emb)

    assert content == "这是答案"
    assert len(idxs) == rag.TOP_K or len(idxs) == 2
    _, kwargs = mock_chat.call_args
    assert kwargs["model"] == rag.CHAT_MODEL
    prompt = kwargs["messages"][0]["content"]
    assert "什么是 RAG？" in prompt
    assert "doc.txt" in prompt
