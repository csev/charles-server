from fire_elasticsearch import Elasticsearch

from server import server

server.blueprint(Elasticsearch.resource(url_prefix='/v1'))
