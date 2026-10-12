def get_profile(user_id):
    query = """
        SELECT id, user_id, name, email
        FROM profiles
        WHERE user_id = %s
    """

    return execute_query(query, user_id)


def get_user(user_id):
    query = """
        SELECT id, name, email
        FROM users
        WHERE id = %s
    """

    return execute_query(query, user_id)