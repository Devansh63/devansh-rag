"""
VectorStore wrapper around ChromaDB.
"""

import chromadb

COLLECTION_NAME = "devansh_knowledge"


class VectorStore:
    def __init__(self, path: str = "./chroma_db"):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )

    def clear(self) -> None:
        try:
            self.client.delete_collection(name=COLLECTION_NAME)
        except Exception:
            pass
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )

    def add_documents(self, docs, ids, embeddings, metadatas=None):
        if not docs:
            return
        kwargs = {"documents": docs, "ids": ids, "embeddings": embeddings}
        if metadatas:
            kwargs["metadatas"] = metadatas
        self.collection.add(**kwargs)

    def query(self, embedding, n_results=5):
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=min(n_results, self.collection.count()),
            include=["documents", "distances", "metadatas"],
        )
        output = []
        if not results["ids"] or not results["ids"][0]:
            return output
        for i, doc_id in enumerate(results["ids"][0]):
            output.append({
                "id": doc_id,
                "document": results["documents"][0][i],
                "distance": results["distances"][0][i],
                "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
            })
        return output

    def count(self):
        return self.collection.count()
