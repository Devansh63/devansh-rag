"""
Embedder using the google-genai SDK (gemini-embedding-001).
"""

import os
from google import genai
from google.genai import types


class Embedder:
    MODEL = "gemini-embedding-001"

    def __init__(self, api_key: str | None = None):
        key = api_key or os.environ.get("GEMINI_API_KEY")
        if not key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.client = genai.Client(api_key=key)

    def embed_document(self, text: str) -> list[float]:
        result = self.client.models.embed_content(
            model=self.MODEL,
            contents=text,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT"),
        )
        return result.embeddings[0].values

    def embed_query(self, text: str) -> list[float]:
        result = self.client.models.embed_content(
            model=self.MODEL,
            contents=text,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY"),
        )
        return result.embeddings[0].values
