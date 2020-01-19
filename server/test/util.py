import json

from fire_document import Document


class Request(object):

    methods = [
        'get',
        'post',
        'put',
        'patch',
        'delete',
        'options'
    ]

    def __init__(self, server, token=None):
        self.server = server
        self.token = token

    def __getattribute__(self, name):
        if not name in super(Request, self).__getattribute__('methods'):
            raise Exception(f'Invalid method: {name}')
        attr = getattr(super(Request, self).__getattribute__('server').test_client, name)
        token = super(Request, self).__getattribute__('token')
        def handler(*args, **kargs):
            headers = kargs.get('headers', { })
            headers['Content-Type'] = 'application/vnd.api+json'
            headers['Accept'] = 'application/vnd.api+json'
            if token:
                headers['Authorization'] = f'Bearer {token}'
            kargs['headers'] = headers
            _, response = attr(*args, **kargs)
            return Document(response.json)
        return handler


def authenticate(server, username='admin', password='admin'):
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json'
    }

    data = {
        'data': {
            'attributes': {
                'username': username,
                'password': password
            }
        }
    }

    _, response = server.test_client.post('/v1/authentication',
        headers=headers,
        data=json.dumps(data)
    )

    response = Document(response.json)

    if response.data:
        return response.data.attributes.token
    else:
        return response.errors

def request(server, token=None):
    return Request(server, token)
