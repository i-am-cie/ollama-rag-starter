# ollama-rag-starter

> **Ask questions over your own documents. Fully local. No API keys. No LangChain.**

A ~100-line RAG template powered by [Ollama](https://ollama.com). Drop in your `.txt` / `.md` files, run one command, get answers with sources — everything runs on your machine.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-powered-orange.svg)
![Size](https://img.shields.io/badge/code-~100%20lines-brightgreen.svg)

---

> 📸 **Screenshot goes here** — run the project and drop a terminal GIF / PNG below this line.

```
$ python rag.py

Indexing documents in ./docs ...
Indexed 12 chunks.

Ask questions (type 'exit' to quit):

> How do I install Ollama?

Install Ollama from ollama.com/download, then run `ollama pull qwen2.5:7b`
to download a model. That's it — no API keys, no cloud setup.

-- sources: ['sample.txt'] (scores: [0.721, 0.615, 0.588])
```

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
| Time to first answer | < 2 min | 20 min |
| Read the whole codebase | ✅ One sitting | 😵 |

## Quick Start

### 1. Install Ollama + models

```bash
# Install from https://ollama.com/download
ollama pull nomic-embed-text
ollama pull qwen2.5:7b
```

> **Low VRAM?** Use `qwen2.5:3b` (~2 GB) — change `CHAT_MODEL` in `rag.py`.

### 2. Clone & run

```bash
git clone https://github.com/i-am-cie/ollama-rag-starter.git
cd ollama-rag-starter
pip install -r requirements.txt
python rag.py
```

### 3. Add your own docs

Drop any `.txt` or `.md` files into `docs/` and restart. That's the whole setup.

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
├── rag.py             # the entire RAG pipeline
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] PDF support (`pypdf`)
- [ ] Persist embeddings to disk
- [ ] Gradio web UI
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
