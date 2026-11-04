"""
ollama-rag-starter: Lightweight local RAG powered by Ollama.

Run: python rag.py
Requires: ollama pull nomic-embed-text && ollama pull qwen2.5:7b
"""

import os
import glob
import numpy as np
import ollama

# ---- Configuration ----
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen2.5:7b"
CHUNK_SIZE = 500      # characters per chunk
CHUNK_OVERLAP = 80    # overlap between adjacent chunks
TOP_K = 3             # how many chunks to retrieve
DOCS_DIR = "docs"


# ---------- Document loading ----------
def load_documents(docs_dir: str = DOCS_DIR):
    """Load all .txt and .md files recursively from docs_dir."""
    texts = []
    for path in glob.glob(os.path.join(docs_dir, "**/*"), recursive=True):
        if path.endswith((".txt", ".md")):
            with open(path, "r", encoding="utf-8") as f:
                texts.append((os.path.basename(path), f.read()))
    return texts


# ---------- Chunking ----------
def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    """Split text into overlapping chunks by character count."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return [c.strip() for c in chunks if c.strip()]


# ---------- Embedding ----------
def embed(texts):
    """Embed a list of strings using Ollama. Returns numpy array."""
    resp = ollama.embed(model=EMBED_MODEL, input=texts)
    return np.array(resp["embeddings"], dtype=np.float32)


# ---------- Retrieval ----------
def retrieve(query_emb, corpus_emb, top_k: int = TOP_K):
    """Cosine-similarity search. Returns (indices, scores)."""
    q = query_emb / np.linalg.norm(query_emb, axis=1, keepdims=True)
    c = corpus_emb / np.linalg.norm(corpus_emb, axis=1, keepdims=True)
    scores = (c @ q.T).flatten()
    top_idx = np.argsort(scores)[::-1][:top_k]
    return top_idx, scores[top_idx]


# ---------- Build index ----------
def build_index(docs_dir: str = DOCS_DIR):
    """Load docs, chunk them, embed everything. Returns (chunks, embeddings)."""
    all_chunks = []  # list of (source_filename, chunk_text)
    for fname, content in load_documents(docs_dir):
        for chunk in chunk_text(content):
            all_chunks.append((fname, chunk))

    if not all_chunks:
        raise SystemExit(f"No .txt/.md files found in ./{docs_dir}/ — add some documents first!")

    corpus_texts = [c[1] for c in all_chunks]
    corpus_emb = embed(corpus_texts)
    return all_chunks, corpus_emb


# ---------- Ask ----------
def answer(question: str, all_chunks, corpus_emb):
    """Retrieve context and generate an answer via Ollama chat."""
    q_emb = embed([question])
    idxs, scores = retrieve(q_emb, corpus_emb)

    context = "\n\n".join(
        [f"[{all_chunks[i][0]}]\n{all_chunks[i][1]}" for i in idxs]
    )

    prompt = f"""Answer the question based ONLY on the context below.
If the answer is not in the context, say you don't know.

Context:
{context}

Question: {question}
Answer:"""

    resp = ollama.chat(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp["message"]["content"], idxs, scores


# ---------- CLI ----------
def main():
    print(f"Indexing documents in ./{DOCS_DIR} ...")
    all_chunks, corpus_emb = build_index()
    print(f"Indexed {len(all_chunks)} chunks from {len(set(c[0] for c in all_chunks))} file(s).\n")
    print("Ask questions (type 'exit' to quit):")

    while True:
        try:
            q = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("exit", "quit"):
            break
        if not q:
            continue

        ans, idxs, scores = answer(q, all_chunks, corpus_emb)
        print(f"\n{ans}")
        sources = [all_chunks[i][0] for i in idxs]
        print(f"\n-- sources: {sources} (scores: {[round(float(s), 3) for s in scores]})")


if __name__ == "__main__":
    main()
