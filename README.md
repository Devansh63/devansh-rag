# Devansh RAG — Ask Me Anything

This is the backend for the "Ask Devansh" chatbot on my portfolio. You ask it something about me, it retrieves the most relevant chunks from my bio and resume, and Gemini generates a response in my voice.

Built with Flask, ChromaDB, and Google Gemini.

## How it works

Standard RAG setup:

1. `data/about_me.md` gets chunked into ~600 character pieces and embedded using Gemini's embedding model
2. The embeddings get stored in a local ChromaDB collection
3. When someone sends a question, it gets embedded and the top 5 most similar chunks are retrieved
4. Those chunks are passed as context to Gemini 2.5 Flash, which generates a response as if it's me

If something isn't in the knowledge base, the bot says so rather than making things up.

## Stack

- **Flask** for the web server and API
- **ChromaDB** for vector storage
- **Google Gemini** for both embedding (`gemini-embedding-001`) and generation (`gemini-2.5-flash`)
- **Docker** for deployment on Render
- **flask-cors** and **flask-limiter** for CORS handling and basic rate limiting

## Running locally

You'll need Python 3.11+ and a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

```bash
git clone https://github.com/Devansh63/devansh-rag.git
cd devansh-rag

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edit .env and paste in your GEMINI_API_KEY

python ingest.py    # chunks and embeds about_me.md into ChromaDB
python app.py       # starts Flask on port 5000
```

Open http://localhost:5000 and start asking questions.

## Deploying to Render

1. Fork this repo
2. Create a new **Web Service** on [render.com](https://render.com) and connect your fork
3. Set the runtime to **Docker** — the `Dockerfile` handles everything
4. Add `GEMINI_API_KEY` as an environment variable in the service settings
5. Hit deploy

The `Dockerfile` runs `ingest.py` at startup, so the vector index gets rebuilt automatically. On the free plan, this adds 30-60 seconds to cold start times, which is fine for a portfolio chatbot.

After deploying, update `RAG_API_URL` in your portfolio's `index.html` to point to your Render URL, and set `ALLOWED_ORIGIN` in Render's environment variables to your portfolio domain.

## Customizing with your own data

This is designed to be forked and repurposed. The main things to change:

1. **Replace `data/about_me.md`** with your own info. Use clear section headers — it helps with retrieval quality.

2. **Re-run ingestion** to rebuild the index:
   ```bash
   python ingest.py
   ```

3. **Update the system prompt** in `rag/pipeline.py` to change the bot's name or persona.

4. **Update the sidebar** in `templates/index.html` with your own name and links.

## Project structure

```
devansh-rag/
├── data/
│   └── about_me.md          # knowledge base — edit this to customize
├── rag/
│   ├── embedder.py          # Gemini embedding wrapper
│   ├── vector_store.py      # ChromaDB wrapper
│   └── pipeline.py          # RAG pipeline (retrieve + generate)
├── static/
│   ├── chat.js
│   ├── style.css
│   └── images/              # drop profile.jpg here (gitignored)
├── templates/
│   └── index.html
├── chroma_db/               # auto-created by ingest.py, gitignored
├── app.py                   # Flask server
├── ingest.py                # ingestion script
├── Dockerfile
├── render.yaml
├── requirements.txt
└── .env.example
```

## Getting a Gemini API key

Go to [aistudio.google.com](https://aistudio.google.com/app/apikey), sign in with your Google account, and create a free API key. The free tier is plenty for a personal chatbot.

---

Built by [Devansh Agrawal](https://www.linkedin.com/in/devansh-agrawal63/)
