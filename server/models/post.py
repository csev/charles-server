from sugar_odm import MongoDBModel, Field
from sugar_api import JSONAPIMixin


class Post(MongoDBModel, JSONAPIMixin):

    __acl__ = {
        '$owner': ['all'],
        'administrator': ['all'],
        'other': ['read', 'read_all'],
        'unauthorized': ['read', 'read_all']
    }

    __database_options__ = {
        'name': 'sugar-blog'
    }

    title = Field(required=True)
    owner = Field(required=True)
    created = Field(type=int, required=True)
    updated = Field(type=int)
    tags = Field(type=[ str ])
    content = Field(required=True)
