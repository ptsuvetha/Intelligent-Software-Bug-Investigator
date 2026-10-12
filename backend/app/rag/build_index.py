from pathlib import Path

from app.rag.ingestion import load_documents
from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


# Project root
BASE_DIR = Path(__file__).resolve().parents[3]

# Data folder
DATA_PATH = BASE_DIR / "data"


def main():

    print("=" * 60)
    print("AI ENGINEERING INVESTIGATOR - INDEX BUILDER")
    print("=" * 60)

    print("\nData path:")
    print(DATA_PATH)

    print("\nDoes data folder exist?")
    print(DATA_PATH.exists())

    print("\nLoading documents...")

    documents = load_documents(str(DATA_PATH))

    print(f"Loaded {len(documents)} documents")

    if len(documents) == 0:
        print("\nERROR: No documents were found.")
        print("Check your data folder.")
        return

    print("\nDocuments found:")

    for document in documents:
        print(
            f" - {document.source}"
        )

    print("\nCreating embeddings...")

    embedding_service = EmbeddingService()

    embeddings = embedding_service.embed_documents(
        [document.content for document in documents]
    )

    print(
        f"Created {len(embeddings)} embeddings"
    )

    vector_store = VectorStore()

    try:

        print("\nCreating/checking Qdrant collection...")

        vector_store.create_collection()

        print("\nStoring vectors...")

        vector_store.add_documents(
            documents,
            embeddings
        )

        print("\nIndexing completed successfully!")

    finally:

        vector_store.close()

        print("Qdrant connection closed.")


if __name__ == "__main__":
    main()