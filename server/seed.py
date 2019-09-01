from sugar_odm import MongoDB

from server import server

from models.user import User
from models.group import Group


@server.listener('before_server_start')
async def before_server_start(app, loop):
    user = await User.find_one({ 'username': 'admin' })

    if not user:
        await User.add({
            'username': 'admin',
            'password': 'admin',
            'groups': [ 'administrator' ]
        })
