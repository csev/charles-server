from sanic import Sanic
from sugar_api import CORS


CORS.set_origins('*')

server = Sanic('sugar-blog')
