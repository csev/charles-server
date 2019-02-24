from sugar_odm import MongoDB

from server import server

from models.user import User
from models.group import Group


@server.listener('before_server_start')
async def before_server_start(app, loop):
    MongoDB.set_event_loop(loop)

    administrator = await Group.find_one({ 'name': 'administrator' })

    if not administrator:
        administrator = await Group.add({
            'name': 'administrator'
        })

    user = await User.find_one({ 'groups': { '$all': [ administrator.id ] } })

    if not user:
        user = await User.add({
            'username': 'admin',
            'password': 'admin',
            'groups': [ administrator.id ]
        })
