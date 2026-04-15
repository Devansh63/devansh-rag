"""
Ingest script — reads about_me.md, chunks it, embeds with Gemini, stores in ChromaDB.

Run with: python ingest.py
"""

import os
import sys
import time

from dotenv import load_dotenv
load_dotenv()

from rag.embedder import Embedder
from rag.vector_store import VectorStore

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "about_me.md")
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")
TARGET_CHUNK_SIZE = 600
MIN_CHUNK_SIZE = 100


def load_document(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_into_chunks(text, target_size=TARGET_CHUNK_SIZE, min_size=MIN_CHUNK_SIZE):
    raw_paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current_chunk = ""
    for paragraph in raw_paragraphs:
        if not current_chunk:
            current_chunk = paragraph
        elif len(current_chunk) + len(paragraph) + 2 <= target_size:
            current_chunk += "\n\n" + paragraph
        else:
            if len(current_chunk) >= min_size:
                chunks.append(current_chunk)
                current_chunk = paragraph
            else:
                current_chunk += "\n\n" + paragraph
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    merged = []
    for chunk in chunks:
        if merged and len(chunk) < min_size:
            merged[-1] += "\n\n" + chunk
        else:
            merged.append(chunk)
    return merged


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set.")
        sys.exit(1)

    print("=" * 60)
    print("  Devansh RAG — Ingestion Pipeline")
    print("=" * 60)

    print(f"\n[1/4] Loading: {DATA_FILE}")
    text = load_document(DATA_FILE)
    print(f"      {len(text):,} characters.")

    print(f"\n[2/4] Chunking (target ~{TARGET_CHUNK_SIZE} chars)...")
    chunks = split_into_chunks(text)
    print(f"      {len(chunks)} chunks created.")

    print(f"\n[3/4] Embedding {len(chunks)} chunks...")
    embedder = Embedder(api_key=api_key)
    embeddings = []
    for i, chunk in enumerate(chunks):
        print(f"      chunk {i+1}/{len(chunks)}...", end=" ", flush=True)
        try:
            embeddings.append(embedder.embed_document(chunk))
            print("done")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)
        if i < len(chunks) - 1:
            time.sleep(0.2)

    print(f"\n[4/4] Storing in ChromaDB at {CHROMA_PATH}...")
    store = VectorStore(path=CHROMA_PATH)
    store.clear()
    ids = [f"chunk_{i:03d}" for i in range(len(chunks))]
    metadatas = [{"chunk_index": i, "char_count": len(c)} for i, c in enumerate(chunks)]
    store.add_documents(docs=chunks, ids=ids, embeddings=embeddings, metadatas=metadatas)
    count = store.count()
    print(f"      {count} chunks stored.")
    print("\n" + "=" * 60)
    print(f"  Done! {count} chunks indexed. Run: python app.py")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
