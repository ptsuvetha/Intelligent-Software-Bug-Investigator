from app.rag.retriever import Retriever


def main():

    retriever = Retriever()

    try:

        query = """
        profile.name is accessed when profile is None
        """

        print("\nSearching for:", query)

        results = retriever.search(query)

        print(f"\nFound {len(results)} results\n")

        for result in results:

            print("=" * 60)

            print("Source:")
            print(result["source"])

            print("\nCategory:")
            print(result["category"])

            print("\nScore:")
            print(result["score"])

            print("\nContent:")
            print(result["content"])

            print()

    finally:

        retriever.close()

        print("Qdrant connection closed.")


if __name__ == "__main__":
    main()