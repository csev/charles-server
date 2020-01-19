import os
from uuid import uuid4

from fire_odm import MongoDB

from server import server

from models.user import User


@server.listener('before_server_start')
async def before_server_start(app, loop):
    user = await User.find_one({ 'username': 'administrator' })

    if not user:
        user = await User.add({
            'username': os.getenv('FIRE_ADMIN_USERNAME', 'administrator'),
            'password': os.getenv('FIRE_ADMIN_PASSWORD', 'password'),
            'email': os.getenv('FIRE_ADMIN_EMAIL', 'paul.severance@gmail.com'),
            'secret': str(uuid4()),
            'groups': [ 'administrator' ]
        })
        await user.send_confirmation_email()
