from server import server

from authentication import Authentication

from models.user import User


server.blueprint(Authentication.resource(url_prefix='/v1'))

server.blueprint(User.resource(url_prefix='/v1'))
