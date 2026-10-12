from app.rag.chunking import chunk_python_code


code = """
def get_user_profile(user_id):
    profile = database.get_profile(user_id)

    return {
        "name": profile.name,
        "email": profile.email
    }


def update_user_profile(user_id, name, email):
    profile = database.get_profile(user_id)

    profile.name = name
    profile.email = email

    database.save(profile)
"""


chunks = chunk_python_code(
    code,
    "code/profile_service.py"
)


for index, chunk in enumerate(chunks):

    print("=" * 60)

    print(f"Chunk {index}")

    print("Name:")
    print(chunk["name"])

    print("Source:")
    print(chunk["source"])

    print("Lines:")
    print(
        chunk["start_line"],
        "-",
        chunk["end_line"]
    )

    print("\nContent:")

    print(chunk["content"])