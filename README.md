# ollama-rag-starter

A lightweight, fully local RAG (Retrieval-Augmented Generation) template powered by [Ollama](https://ollama.com).

Ask questions over your own documents — **no API keys, no cloud, no external dependencies beyond Ollama itself**.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-powered-orange.svg)

---

## Why another RAG template?

Most RAG demos stack on LangChain, ChromaDB, OpenAI API keys, and vector databases you have to deploy. This one strips it down to:

- **One Python file** (~80 lines) you can actually read in one sitting
- **Numpy** for vector search — no vector DB needed
- **Ollama** for both embeddings and chat — everything runs on your machine
- Works with plain `.txt` / `.md` files dropped into `docs/`

## Features

- 📄 Load documents from a folder (`.txt`, `.md`)
- ✂️ Simple character-based chunking with overlap
- 🔢 Embeddings via `nomic-embed-text` (local, via Ollama)
- 🔍 Cosine-similarity retrieval with numpy
- 💬 Conversational CLI — ask questions, get sourced answers
- 🔎 Shows which source files and similarity scores were used

## Quick Start

### 1. Prerequisites

Install [Ollama](https://ollama.com/download), then pull the two models:

```bash
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
```

> **GPU/VRAM tip**: Qwen2.5 7B needs ~5–6 GB VRAM. If you have less, use `qwen2.5:3b` instead (edit `CHAT_MODEL` in `rag.py`).

### 2. Install dependencies

```bash
git clone https://github.com/i-am-cie/ollama-rag-starter.git
cd ollama-rag-starter
pip install -r requirements.txt
```

### 3. Drop your documents

Put any `.txt` or `.md` files into the `docs/` folder. A sample file is included.

### 4. Run

```bash
python rag.py
```

You'll see:

```
Indexing documents in ./docs ...
Indexed 12 chunks.

Ask questions (type 'exit' to quit):

> What is Ollama?

Ollama is a tool that lets you run large language models locally on your own computer...

-- sources: ['sample.txt'] (scores: [0.721, 0.615, 0.588])
```

## Project Structure

```
ollama-rag-starter/
├── docs/              # Drop your .txt / .md files here
│   └── sample.txt
├── rag.py             # The entire RAG pipeline (single file)
├── requirements.txt
├── .gitignore
└── README.md
```

## Configuration

Edit the constants at the top of `rag.py`:

| Variable | Default | What it does |
|---|---|---|
| `EMBED_MODEL` | `nomic-embed-text` | Ollama model for embeddings |
| `CHAT_MODEL` | `qwen2.5:7b` | Ollama model for answering |
| `CHUNK_SIZE` | `500` | Characters per text chunk |
| `CHUNK_OVERLAP` | `80` | Overlap between chunks |
| `TOP_K` | `3` | How many chunks to retrieve |

## How It Works

```
Your docs → chunk → embed (Ollama) → numpy array storage
                                              ↑
Question → embed → cosine similarity → top-K chunks → feed to LLM → answer
```

No database. No server. No network calls after the models are pulled.

## Roadmap

- [ ] PDF support (via `pypdf`)
- [ ] Persist embeddings to disk (avoid re-indexing every run)
- [ ] Web UI (Gradio / Streamlit)
- [ ] Config file (YAML / .env)
- [ ] Citation highlighting in answers

## Contributing

Issues and PRs are welcome. Good first PRs:
- Add a new document loader (PDF, HTML, Notion export)
- Improve chunking (sentence-aware instead of character-based)
- Add unit tests

## License

[MIT](./LICENSE)
