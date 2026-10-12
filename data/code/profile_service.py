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