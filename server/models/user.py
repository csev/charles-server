import hashlib

from sugar_odm import MongoDBModel, Field
from sugar_api import JSONAPIMixin


class User(MongoDBModel, JSONAPIMixin):

    __rate__ = [ 1, 'secondly' ]

    __acl__ = {
        'self': ['read'],
        'administrator': ['all'],
        'other': ['read']
    }

    __database__ = {
        'name': 'database-name'
    }

    username = Field(required=True)
    password = Field(required=True, computed='encrypt_password')

    groups = Field(type=list, required=True)

    def on_render(self, data):
        del data['attributes']['password']
        return data

    def encrypt_password(self):
        if self.password == 'hashed-':
            raise Exception('Invalid password.')

        if self.password.startswith('hashed-'):
            return self.password

        return f'hashed-{hashlib.sha256(self.password.encode()).hexdigest()}'
