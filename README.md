# ollama-rag-starter

> **Ask questions over your own documents. Fully local. No API keys. No LangChain.**

A ~100-line RAG template powered by [Ollama](https://ollama.com). Drop in your `.txt` / `.md` files, run one command, get answers with sources — everything runs on your machine.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-powered-orange.svg)
![Size](https://img.shields.io/badge/code-~100%20lines-brightgreen.svg)

---

![Web UI screenshot](docs/screenshot.jpg)

---

## Why this exists

Every RAG tutorial on the internet tells you to install LangChain, spin up ChromaDB,
get an OpenAI API key, and wire together 10 abstract classes you'll never read again.

**This repo is the opposite.** One Python file. Numpy for search. Ollama for models.
Read it in 5 minutes, then make it yours.

## Comparison

| | This repo | Typical RAG tutorial |
|---|---|---|
| Lines of code | ~100 | 500+ |
| Dependencies | `ollama`, `numpy` | LangChain, ChromaDB, OpenAI SDK, +10 |
| API keys needed | None | OpenAI / Cohere / etc. |
| Runs offline | ✅ | ❌ |
| Vector database | No (numpy arrays) | Yes (Docker / server) |
| Web UI | Gradio (optional) | Separate setup |
| Time to first answer | < 2 min | 20 min |

## Quick Start

### 1. Install Ollama + models

```bash
# Install from https://ollama.com/download
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
```

> **Low VRAM?** Use `qwen2.5:3b` (~2 GB) — change `CHAT_MODEL` in `rag.py`.

### 2. Clone & install

```bash
git clone https://github.com/i-am-cie/ollama-rag-starter.git
cd ollama-rag-starter
pip install -r requirements.txt
```

### 3a. CLI mode

```bash
python rag.py
```

### 3b. Web UI mode

```bash
pip install gradio
python app.py
# Open http://localhost:7860
```

> **No Ollama?** Try `python app.py --demo` to see the UI with mock answers.

### 4. Add your docs

Drop any `.txt` or `.md` files into `docs/` and restart.

## Configuration

Edit the constants at the top of `rag.py`:

| Variable | Default | What it does |
|---|---|---|
| `EMBED_MODEL` | `nomic-embed-text` | Ollama embedding model |
| `CHAT_MODEL` | `qwen2.5:7b` | Ollama chat model |
| `CHUNK_SIZE` | `500` | Characters per chunk |
| `CHUNK_OVERLAP` | `80` | Overlap between chunks |
| `TOP_K` | `3` | Chunks retrieved per query |

## How it works

```
Your docs → chunk → embed (Ollama) → numpy array
                                          ↑
Question → embed → cosine similarity → top-K → prompt → LLM → answer
```

No database. No server. No network after model download.

## Project structure

```
ollama-rag-starter/
├── docs/              # your documents go here
│   └── sample.txt
├── rag.py             # CLI version (the entire RAG pipeline)
├── app.py             # Gradio web UI
├── requirements.txt
└── README.md
```

## Roadmap

- [x] Gradio web UI
- [ ] PDF support (`pypdf`)
- [ ] Persist embeddings to disk
- [ ] Sentence-aware chunking
- [ ] Config file (YAML)

## Contributing

PRs welcome. Good first issues:
- PDF loader
- Sentence-based chunking
- Unit tests

## License

[MIT](./LICENSE) — do whatever you want.

---

**⭐ Star this repo if it saves you an afternoon.** It helps others find it.
