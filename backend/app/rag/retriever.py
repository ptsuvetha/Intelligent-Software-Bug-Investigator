from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

    def search(
        self,
        query: str,
        limit: int = 3
    ):

        query_embedding = (
            self.embedding_service.embed(query)
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            limit=limit
        )

        return [
            {
                "source": result.payload["source"],
                "category": result.payload["category"],
                "content": result.payload["content"],
                "score": result.score
            }
            for result in results
        ]

    def close(self):

        self.vector_store.close()