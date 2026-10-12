import ast


def chunk_python_code(
    code: str,
    file_path: str
):
    """
    Split Python code into function/class-level chunks.
    """

    chunks = []

    try:
        tree = ast.parse(code)

    except SyntaxError:

        # If Python code cannot be parsed,
        # return the entire file as one chunk.

        return [
            {
                "content": code,
                "source": file_path,
                "type": "code"
            }
        ]

    for node in ast.walk(tree):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef
            )
        ):

            start_line = node.lineno
            end_line = node.end_lineno

            lines = code.splitlines()

            chunk = "\n".join(
                lines[start_line - 1:end_line]
            )

            chunks.append(
                {
                    "content": chunk,
                    "source": file_path,
                    "type": "code",
                    "start_line": start_line,
                    "end_line": end_line,
                    "name": node.name
                }
            )

    return chunks