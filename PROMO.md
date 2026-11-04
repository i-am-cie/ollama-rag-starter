# Promo Copy — Ready to Post

Copy-paste-ready posts for each channel. Edit links/numbers as needed.

---

## 🦄 Reddit — r/LocalLLaMA

**Title:**
> I built a minimal RAG starter for Ollama — ~100 lines, no LangChain, no vector DB

**Body:**

Hey everyone,

I got frustrated with every RAG tutorial requiring LangChain, ChromaDB, and an OpenAI key — so I stripped it down to the bare minimum.

It's a single Python file (~100 lines) that:
- Loads .txt/.md files from a folder
- Chunks them and embeds with Ollama's nomic-embed-text
- Does cosine-similarity search with numpy (no vector DB)
- Feeds top-K chunks to qwen2.5 (or any Ollama model) and prints sourced answers

Everything runs locally. No API keys. No Docker. Read the whole codebase in one sitting.

Quick start:
```
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
git clone https://github.com/i-am-cie/ollama-rag-starter
pip install -r requirements.txt
python rag.py
```

Repo: https://github.com/i-am-cie/ollama-rag-starter

It's early — PRs welcome for PDF support, sentence chunking, a web UI, etc. Would love feedback.

---

## 📰 Hacker News (Show HN)

**Title:**
> Show HN: A 100-line local RAG template powered by Ollama

**Text:**

I kept seeing RAG tutorials that require installing LangChain, spinning up a vector database, and getting an OpenAI API key just to ask a question over a local PDF. So I built the opposite: a single ~100-line Python file that uses Ollama for both embeddings and chat, and numpy for cosine-similarity retrieval.

No vector database. No API keys. No framework abstraction. You can read the entire codebase in one sitting and modify any part of it.

Repo: https://github.com/i-am-cie/ollama-rag-starter

Happy to hear feedback on chunking strategy, retrieval, or what else you'd want in a minimal starter.

---

## 🟠 掘金 / 知乎 / V2EX（中文）

**标题：**
> 用 Ollama 本地跑 RAG，我只写了 100 行 Python —— 不要 LangChain，不要向量数据库

**正文：**

每次想在本地文档上问问题，教程都让你装 LangChain、起 ChromaDB、注册 OpenAI API key……太折腾了。

于是我把 RAG 拆到不能再拆：一个 Python 文件，用 Ollama 做 embedding 和对话，用 numpy 算余弦相似度。没有向量数据库，没有框架抽象，没有 API key，完全离线跑。

3 步跑起来：
```bash
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
git clone https://github.com/i-am-cie/ollama-rag-starter
pip install -r requirements.txt && python rag.py
```

把自己的 .txt / .md 丢进 docs/ 目录就能提问。

仓库：https://github.com/i-am-cie/ollama-rag-starter

新手友好，整个代码 100 行，5 分钟读完。欢迎提 Issue 和 PR（PDF 支持、Web UI 都在 Roadmap 上）。

---

## 🏷️ GitHub Topics（手动在仓库页面 Add topics）

```
rag ollama local-llm retrieval-augmented-generation qwen llm python local-first no-api-key starter-template numpy cosine-similarity
```

路径：仓库主页 → About 右边齿轮 ⚙️ → 填写 Topics。
