from datetime import datetime

from sugar_api import WebToken

from models.user import User
from models.group import Group


WebToken.set_secret('secret')


class Authentication(WebToken):

    @classmethod
    async def payload(cls, username, password):
        user = await User.find_one({
            'username': username,
            'password': password
        })

        if not user:
            raise Exception('Invalid username or password.')

        group = await Group.find_by_id(user.group)

        if not group:
            raise Exception('User\'s group not found.')

        return {
            'data': {
                'id': user.id,
                'type': group.name,
                'attributes': {
                    'username': user.username,
                    'timestamp': datetime.utcnow().timestamp()
                }
            }
        }
