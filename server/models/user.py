import hashlib

from sugar_odm import MongoDBModel, Field
from sugar_api import JSONAPIMixin


class User(MongoDBModel, JSONAPIMixin):

    __rate__ = ( 1, 'secondly' )

    __acl__ = {
        'self': ['read', 'update', 'delete'],
        'administrator': ['all'],
        #'other': ['read'],
        'unauthorized': ['create']
    }

    __get__ = {
        'groups': ['self', 'administrator']
    }

    __set__ = {
        'username': ['self', 'administrator', 'unauthorized'],
        'password': ['self', 'administrator', 'unauthorized'],
        'groups': ['administrator']
    }

    __database__ = {
        'name': 'vue-sugar-template'
    }

    username = Field(required=True)
    password = Field(required=True, computed='encrypt_password')

    groups = Field(type=list, computed='default_groups', computed_empty=True)

    def on_render(self, data, token):
        del data['attributes']['password']

    def default_groups(self):
        return [ 'users' ]

    def encrypt_password(self):
        if self.password == 'hashed-':
            raise Exception('Invalid password.')

        if self.password.startswith('hashed-'):
            return self.password

        return f'hashed-{hashlib.sha256(self.password.encode()).hexdigest()}'
