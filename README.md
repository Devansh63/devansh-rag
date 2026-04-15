# devansh-rag

Personal RAG chatbot that answers questions about me (Devansh Agrawal) using a **Retrieval-Augmented Generation** pipeline. Powers the AI assistant embedded at devanshagrawal.com.

Built with Google Gemini, ChromaDB, and Flask. Deployed on Render.

---

## How It Works

1. **Ingest** — `data/about_me.md` is split into chunks and embedded with Gemini `gemini-embedding-001`.
2. **Store** — Chunks and embeddings are persisted in ChromaDB.
3. **Retrieve** — At query time, the question is embedded and the top 5 semantically similar chunks are fetched.
4. **Generate** — Those chunks are passed as context to Gemini 2.5 Flash, which answers as me.

---

## Stack

- **LLM**: Google Gemini 2.5 Flash
- **Embeddings**: Gemini `gemini-embedding-001`
- **Vector store**: ChromaDB
- **Backend**: Flask + Gunicorn
- **Deploy**: Docker on Render
- **Rate limiting**: flask-limiter (10 req/min on `/api/chat`)
- **CORS**: flask-cors (controlled via `ALLOWED_ORIGIN` env var)

---

## Running Locally

```bash
git clone https://github.com/Devansh63/devansh-rag.git
cd devansh-rag

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Add your GEMINI_API_KEY to .env

python ingest.py
python app.py
# Open http://localhost:5000
```

---

## Deploying to Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com), create a new **Web Service**, connect this repo
3. Render reads `render.yaml` automatically
4. Set `GEMINI_API_KEY` in the Render dashboard (Environment tab)
5. Set `ALLOWED_ORIGIN` to your Netlify URL (e.g. `https://devanshagrawal.netlify.app`)
6. Deploy — first boot takes ~60s while `ingest.py` builds the ChromaDB index

---

## Updating the Knowledge Base

1. Edit `data/about_me.md`
2. Run `python ingest.py` locally to verify
3. Push — Render redeploys and rebuilds the index automatically

---

## Project Structure

```
devansh-rag/
├── data/about_me.md      # Knowledge base
├── rag/
│   ├── embedder.py       # Gemini embedding wrapper
│   ├── vector_store.py   # ChromaDB wrapper
│   └── pipeline.py       # RAG pipeline
├── static/
│   ├── chat.js
│   └── style.css
├── templates/index.html  # Standalone chat UI
├── app.py                # Flask server
├── ingest.py             # Data ingestion
├── Dockerfile
├── render.yaml           # Render deploy config
└── requirements.txt
```

---

Built by [Devansh Agrawal](https://www.linkedin.com/in/devansh-agrawal63/)
