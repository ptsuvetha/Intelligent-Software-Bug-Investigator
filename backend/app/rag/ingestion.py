from pathlib import Path

from app.rag.chunking import chunk_python_code


class Document:

    def __init__(
        self,
        content: str,
        source: str,
        category: str,
        metadata: dict | None = None
    ):
        self.content = content
        self.source = source
        self.category = category
        self.metadata = metadata or {}


def load_documents(data_path: str):

    documents = []

    data_directory = Path(data_path)

    for file_path in data_directory.rglob("*"):

        if not file_path.is_file():
            continue

        try:

            content = file_path.read_text(
                encoding="utf-8"
            )

            relative_path = file_path.relative_to(
                data_directory
            )

            category = relative_path.parts[0]

            # --------------------------------
            # Python files
            # --------------------------------

            if file_path.suffix == ".py":

                chunks = chunk_python_code(
                    content,
                    str(relative_path)
                )

                for chunk in chunks:

                    documents.append(
                        Document(
                            content=chunk["content"],
                            source=chunk["source"],
                            category=category,
                            metadata={
                                "type": "code",
                                "name": chunk.get("name"),
                                "start_line": chunk.get(
                                    "start_line"
                                ),
                                "end_line": chunk.get(
                                    "end_line"
                                )
                            }
                        )
                    )

            # --------------------------------
            # Other files
            # --------------------------------

            else:

                documents.append(
                    Document(
                        content=content,
                        source=str(relative_path),
                        category=category,
                        metadata={
                            "type": "document"
                        }
                    )
                )

        except UnicodeDecodeError:

            continue

    return documents