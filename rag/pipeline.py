"""
RAG Pipeline using the google-genai SDK.
"""

import os
from google import genai

from rag.embedder import Embedder
from rag.vector_store import VectorStore


SYSTEM_PROMPT = (
    "You are an AI assistant that answers questions about Devansh Agrawal. "
    "Use the provided context to answer questions. "
    "Respond in first person as Devansh himself — be warm, professional, and specific. "
    "If something isn't in the context, say you don't have that info but offer what you do know. "
    "Keep responses concise and conversational."
)

GENERATION_MODEL = "gemini-2.5-flash"


class RAGPipeline:
    def __init__(self, api_key: str | None = None, chroma_path: str = "./chroma_db"):
        key = api_key or os.environ.get("GEMINI_API_KEY")
        if not key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.client = genai.Client(api_key=key)
        self.embedder = Embedder(api_key=key)
        self.vector_store = VectorStore(path=chroma_path)

    def retrieve(self, query: str, n: int = 5) -> list[dict]:
        embedding = self.embedder.embed_query(query)
        return self.vector_store.query(embedding=embedding, n_results=n)

    def generate(self, query: str, chunks: list[dict]) -> str:
        context = "\n\n---\n\n".join(c["document"] for c in chunks) if chunks else "No context found."
        prompt = (
            f"Context about Devansh:\n\n{context}\n\n"
            f"---\n\nQuestion: {query}\n\n"
            f"Answer as Devansh, using the context above. {SYSTEM_PROMPT}"
        )
        response = self.client.models.generate_content(model=GENERATION_MODEL, contents=prompt)
        return response.text

    def chat(self, query: str, n_chunks: int = 5) -> dict:
        chunks = self.retrieve(query, n=n_chunks)
        response_text = self.generate(query, chunks)
        sources = [
            c["document"][:200] + "..." if len(c["document"]) > 200 else c["document"]
            for c in chunks
        ]
        return {"response": response_text, "sources": sources}
