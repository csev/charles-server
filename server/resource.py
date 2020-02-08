from sugar_elasticsearch import Elasticsearch
from charles_elasticsearch import Elasticsearch as CharlesElasticsearch
from charles_elasticsearch import AccessStatus

from server import server
from authentication import Authentication

server.blueprint(Authentication.resource(url_prefix='/v1'))

server.blueprint(AccessStatus.resource(url_prefix='/v1'))

server.blueprint(Elasticsearch.resource(url_prefix='/v1'))
server.blueprint(CharlesElasticsearch.resource('basicauth-elasticsearch', url_prefix='/v1/basicauth'))
