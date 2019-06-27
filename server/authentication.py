import hashlib
from datetime import datetime

from sugar_api import WebToken

from models.user import User
from models.group import Group


WebToken.set_secret('secret')


class Authentication(WebToken):

    @classmethod
    async def payload(cls, username, password):
        digest = f'hashed-{hashlib.sha256(password.encode()).hexdigest()}'

        user = await User.find_one({
            'username': username,
            'password': digest
        })

        if not user:
            raise Exception('Invalid username or password.')

        groups = [ ]
        for id in user.groups:
            group = await Group.find_by_id(id)
            if not group:
                raise Exception(f'Group {id} not found.')
            groups.append(group.name)

        return {
            'data': {
                'id': user.id,
                'groups': groups,
                'scope': {
                    'update-username': user.id,
                    'update-password': user.id
                },
                'attributes': {
                    'username': user.username,
                    'timestamp': datetime.utcnow().timestamp()
                }
            }
        }
