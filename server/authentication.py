import hashlib
from datetime import datetime, timedelta

from fire_api import WebToken

from models.user import User


WebToken.set_secret('secret')


class Authentication(WebToken):

    @classmethod
    async def create(cls, attributes):
        key = attributes.get('key')

        if key:

            user = await User.find_one({
                'key': key
            })

            if not user:
                raise Exception('Invalid key.')

            return {
                #'exp': datetime.utcnow() + timedelta(minutes=5),
                'nbf': datetime.utcnow(),
                'iat': datetime.utcnow(),
                'data': {
                    'id': user.id,
                    'groups': user.groups,
                    'scope': {
                        'update-username': user.id,
                        'update-password': user.id
                    },
                    'attributes': {
                        'username': user.username
                    }
                }
            }

        username = attributes.get('username')

        if not username:
            raise Exception('No username provided.')

        email = attributes.get('email')

        if not email:
            raise Exception('No email provided.')

        password = attributes.get('password')

        if not password:
            raise Exception('No password provided.')

        digest = f'hashed-{hashlib.sha256(password.encode()).hexdigest()}'

        user = await User.find_one({
            'username': username,
            'email': email,
            'password': digest
        })

        if not user:
            raise Exception('Invalid username, email or password.')

        return {
            #'exp': datetime.utcnow() + timedelta(minutes=5),
            'nbf': datetime.utcnow(),
            'iat': datetime.utcnow(),
            'data': {
                'id': user.id,
                'groups': user.groups,
                'scope': {
                    'update-username': user.id,
                    'update-password': user.id
                },
                'attributes': {
                    'username': user.username
                }
            }
        }

    @classmethod
    async def refresh(cls, attributes, token):

        token_data = token.get('data')
        token_id = token_data.get('id')
        token_groups = token_data.get('groups')
        token_scope = token_data.get('scope')
        token_attributes = token_data.get('attributes')

        if not await User.exists(token_id):
            raise Exception('User not found for token ID.')

        return {
            'exp': datetime.utcnow() + timedelta(minutes=5),
            'nbf': datetime.utcnow(),
            'iat': datetime.utcnow(),
            'data': {
                'id': token_id,
                'groups': token_groups,
                'scope': token_scope,
                'attributes': token_attributes
            }
        }
