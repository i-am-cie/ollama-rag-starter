# Promo Copy — Ready to Post

Copy-paste-ready posts for each channel. Edit links/numbers as needed.

> **发布节奏建议（按截图原则4）：每天发一个社区，根据 Upvote/评论反馈迭代文案。**
> 不要全网复制粘贴同一个标题——每个社区的读者在意的点不一样。

---

## 📅 发布节奏表

| Day | 社区 | 钩子角度 | 发布后关注指标 |
|-----|------|----------|----------------|
| 1 | r/LocalLLaMA | 本地优先 / 隐私 / 离线 | 评论里有没有人问 PDF 支持 |
| 2 | V2EX（分享创造） | 周末折腾的小项目 | 站长评价 / 技术讨论深度 |
| 3 | 掘金 | 新手友好 / 5分钟读懂 RAG | 收藏数 / 评论里的问题 |
| 4 | Hacker News (Show HN) | 技术极简 / 反框架抽象 | 首页排名 / 评论里的技术挑战 |
| 5 | 即刻 | 短平快个人感受 | 转发数 / 评论质量 |
| 6 | r/Python | 代码量 / 可读性 / 学习原理 | star 增量 |
| 7 | 复盘 | 根据前6天数据，挑反馈最好的钩子，改写后重发一次 | — |

---

## 🦄 Reddit — r/LocalLLaMA

**钩子角度：本地优先、隐私、离线可用**

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

It's early — PRs welcome for PDF support, sentence chunking, etc. Would love feedback on what you'd want in a minimal starter.

---

## 📰 Hacker News (Show HN)

**钩子角度：技术极简、反框架抽象**

**Title:**
> Show HN: A 100-line local RAG template powered by Ollama

**Text:**

I kept seeing RAG tutorials that require installing LangChain, spinning up a vector database, and getting an OpenAI API key just to ask a question over a local PDF. So I built the opposite: a single ~100-line Python file that uses Ollama for both embeddings and chat, and numpy for cosine-similarity retrieval.

No vector database. No API keys. No framework abstraction. You can read the entire codebase in one sitting and modify any part of it.

Repo: https://github.com/i-am-cie/ollama-rag-starter

Happy to hear feedback on chunking strategy, retrieval, or what else you'd want in a minimal starter.

---

## 🐍 Reddit — r/Python

**钩子角度：代码量、可读性、学习 RAG 原理**

**Title:**
> I wrote a RAG system in ~100 lines of Python — no LangChain, no vector DB

**Body:**

I wanted to actually understand how RAG works under the hood, so I rebuilt it from scratch without any frameworks.

The whole thing is one file (`rag.py`):
- `load_documents()` — reads .txt/.md from a folder
- `chunk_text()` — splits into overlapping character chunks
- `embed()` — calls Ollama for embeddings
- `retrieve()` — cosine similarity with numpy
- `answer()` — builds a prompt and calls the LLM

No magic. No abstract base classes. No vector database server.
You can read every line in 5 minutes and see exactly how retrieval works.

It uses Ollama for both embeddings and chat, so everything runs locally — no API keys.

Repo: https://github.com/i-am-cie/ollama-rag-starter

Would love feedback on the chunking approach or what a minimal RAG starter should include.

---

## 🟠 V2EX — 分享创造节点

**钩子角度：周末折腾的小项目、新手友好**

**标题：**
> 周末花了一下午，用 Ollama 写了个 100 行的本地 RAG 工具

**正文：**

每次想在自己的文档上问问题，教程都让你装 LangChain、起 ChromaDB、注册 OpenAI API key……光环境配置就半小时。

于是我把 RAG 拆到不能再拆：一个 Python 文件，用 Ollama 做 embedding 和对话，用 numpy 算余弦相似度。

没有向量数据库，没有框架抽象，没有 API key，完全离线跑。整个代码 100 行，5 分钟读完。

3 步跑起来：
```bash
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
git clone https://github.com/i-am-cie/ollama-rag-starter
pip install -r requirements.txt && python rag.py
```

把自己的 .txt / .md 丢进 docs/ 目录就能提问。

仓库：https://github.com/i-am-cie/ollama-rag-starter

有 Gradio Web UI 可选。PDF 支持、持久化索引都在 Roadmap 上，欢迎提 Issue 和 PR。

---

## 🟡 掘金 / 知乎

**钩子角度：新手友好、5分钟读懂 RAG 原理**

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

新手友好，整个代码 100 行，5 分钟读完。适合用来理解 RAG 到底是怎么工作的。

---

## ⚡ 即刻

**钩子角度：短平快、个人感受**

**文案：**

周末把 RAG 拆到了极限 —— 100 行 Python，一个文件，不要 LangChain 不要向量数据库不要 API key。
用 Ollama 跑 embedding + 对话，numpy 算余弦相似度，本地完全离线。
把笔记丢进文件夹就能问问题。
https://github.com/i-am-cie/ollama-rag-starter

---

## 🟢 少数派

**钩子角度：实用工具、隐私敏感人群**

**标题：**
> 不想把文档传给 OpenAI？这个 100 行的本地 RAG 工具可能适合你

**正文：**

很多人想给自己的笔记、文档做一个"AI 问答"，但又不想把内容上传到云端。

这个小工具就是解决这个问题的：所有数据都在你自己电脑上，用 Ollama 跑本地模型，不需要任何 API key。

它只做一件事：把你 `docs/` 文件夹里的 `.txt` / `.md` 文件切片、向量化，然后你用自然语言提问，它会找到最相关的几段文档，让本地大模型基于这些内容回答你，并标注来源。

代码量很小（一个 Python 文件，约 100 行），你可以读完每一行然后改成自己想要的样子。

开源地址：https://github.com/i-am-cie/ollama-rag-starter

---

## 🏷️ GitHub Topics（手动在仓库页面 Add topics）

```
rag ollama local-llm retrieval-augmented-generation qwen llm python local-first no-api-key starter-template numpy cosine-similarity
```

路径：仓库主页 → About 右边齿轮 ⚙️ → 填写 Topics。
