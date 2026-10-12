def get_user(user_id):
    user = database.get_user(user_id)

    if user is None:
        raise UserNotFoundError(
            f"User {user_id} does not exist"
        )

    return user


def create_user(name, email):
    user = User(
        name=name,
        email=email
    )

    database.save(user)

    return user