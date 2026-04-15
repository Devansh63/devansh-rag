"""
ChromaDB wrapper for storing and querying document embeddings.
"""

import chromadb


COLLECTION_NAME = "devansh_knowledge"
CHROMA_PATH = "./chroma_db"


class VectorStore:
    def __init__(self, path: str = CHROMA_PATH):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            # cosine similarity works well for text embeddings
            metadata={"hnsw:space": "cosine"},
        )

    def clear(self) -> None:
        """Drop and recreate the collection — used before re-ingesting."""
        try:
            self.client.delete_collection(name=COLLECTION_NAME)
        except Exception:
            pass
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )

    def add_documents(
        self,
        docs: list[str],
        ids: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict] | None = None,
    ) -> None:
        """Store document chunks with their precomputed embeddings."""
        if not docs:
            return

        kwargs: dict = {
            "documents": docs,
            "ids": ids,
            "embeddings": embeddings,
        }
        if metadatas:
            kwargs["metadatas"] = metadatas

        self.collection.add(**kwargs)

    def query(
        self,
        embedding: list[float],
        n_results: int = 5,
    ) -> list[dict]:
        """
        Return the top-n most similar chunks for a given query embedding.
        Each result is a dict with keys: id, document, distance, metadata.
        """
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=min(n_results, self.collection.count()),
            include=["documents", "distances", "metadatas"],
        )

        output = []
        if not results["ids"] or not results["ids"][0]:
            return output

        for i, doc_id in enumerate(results["ids"][0]):
            output.append(
                {
                    "id": doc_id,
                    "document": results["documents"][0][i],
                    "distance": results["distances"][0][i],
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                }
            )
        return output

    def count(self) -> int:
        """Return total number of documents in the collection."""
        return self.collection.count()
