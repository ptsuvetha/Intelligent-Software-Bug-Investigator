from pathlib import Path
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


BASE_DIR = Path(__file__).resolve().parents[3]

QDRANT_PATH = BASE_DIR / "qdrant_data"


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(
            path=str(QDRANT_PATH)
        )

        self.collection_name = (
            "engineering_documents"
        )

    def create_collection(self):

        collections = self.client.get_collections()

        existing_collections = [
            collection.name
            for collection in collections.collections
        ]

        if self.collection_name not in existing_collections:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

            print(
                f"Created collection: {self.collection_name}"
            )

        else:

            print(
                f"Collection already exists: "
                f"{self.collection_name}"
            )

    def add_documents(
        self,
        documents,
        embeddings
    ):

        points = []

        for document, embedding in zip(
            documents,
            embeddings
        ):

            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "content": document.content,
                        "source": document.source,
                        "category": document.category,
                        **document.metadata
}
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        print(
            f"Inserted {len(points)} documents"
        )

    def search(
        self,
        query_embedding,
        limit=3
    ):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            limit=limit
        )

        return results.points

    def close(self):
        self.client.close()