import hashlib

from sugar_odm import MongoDBModel, Field
from sugar_api import JSONAPIMixin


class User(MongoDBModel, JSONAPIMixin):

    __acl__ = {
        'self': ['read', 'update'],
        'administrator': ['all'],
        'other': ['read']
    }

    __database__ = {
        'name': 'database-name'
    }

    username = Field(required=True)
    password = Field(required=True)

    groups = Field(type=list, required=True)

    def set_password(self, password):
        self.password = hashlib.sha256(password).hexdigest()
