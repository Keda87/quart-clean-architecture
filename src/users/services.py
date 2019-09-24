from .repositories import insert_user


async def register(name: str, email: str):
    data = {
        'name': name,
        'email': email,
    }
    return await insert_user(data)