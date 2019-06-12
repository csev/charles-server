from os import listdir
from os.path import dirname, join
from importlib import import_module

files = filter(lambda file: file.endswith('.py'), \
    listdir(join(dirname(__file__), 'handlers')))

for file in files:
    module = file.split('.')[0]
    import_module(f'.{module}', package=f'handlers')

import resource
import seed

from server import server

server.run(host='0.0.0.0', port=8080, workers=1)
