import hashlib
from datetime import datetime, timedelta

from sugar_api import WebToken

from charles_auth import checkpw, secret


WebToken.set_secret('secret')


class Authentication(WebToken):

    @classmethod
    async def create(cls, attributes):
        username = attributes.get('username')

        if not username:
            raise Exception('No username provided.')

        password = attributes.get('password')

        if not password:
            raise Exception('No password provided.')

        if not checkpw(username, password, secret):
            raise Exception('Invalid username or password.')

        token = {
            'exp': datetime.utcnow() + timedelta(minutes=5),
            'nbf': datetime.utcnow(),
            'iat': datetime.utcnow(),
            'data': {
                'id': username,
                'groups': [ ],
                'scope': { }
            }
        }

        if username == 'administrator':
            token['data']['groups'].append('administrator')
            token['data']['scope']['elasticsearch.administrator'] = True
        else:
            token['data']['groups'].append('user')
            token['data']['scope']['elasticsearch.index'] = username

        return token

    @classmethod
    async def refresh(cls, attributes, token):

        token_data = token.get('data')
        token_id = token_data.get('id')
        token_groups = token_data.get('groups')
        token_scope = token_data.get('scope')
        token_attributes = token_data.get('attributes')

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
