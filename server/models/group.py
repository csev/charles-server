from sugar_odm import MongoDBModel, Field
from sugar_api import JSONAPIMixin


class Group(MongoDBModel, JSONAPIMixin):

    __acl__ = {
        'administrator': ['all']
    }

    __database_options__ = {
        'name': 'sugar-blog'
    }

    name = Field(required=True)
