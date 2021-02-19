import asyncio
from aiohttp import ClientSession
from models import Session, User, Post

USERS_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_json(client_session: ClientSession, url) -> dict:
    async with client_session.get(url) as response:
        return await response.json()


async def add_user(session, user_data):
    user = User(id=user_data['id'], name=user_data['name'], username=user_data['username'])
    session.add(user)


async def add_post(session, post_data):
    post = Post(id=post_data['id'], user_id=post_data['userId'], title=post_data['title'], body=post_data['body'])
    session.add(post)


async def run():
    client_session = ClientSession()
    user_data = await fetch_json(client_session, USERS_URL)
    post_data = await fetch_json(client_session, POSTS_URL)
    await client_session.close()

    session = Session()

    for user in user_data:
        await add_user(session, user)

    for post in post_data:
        await add_post(session, post)

    session.commit()
    session.close()


if __name__ == '__main__':
    asyncio.run(run())
