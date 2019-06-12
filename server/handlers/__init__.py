from os import listdir
from os.path import dirname
from importlib import import_module

files = filter(lambda file: \
    not file == '__init__.py' \
    and file.endswith('.py'), \
    listdir(dirname(__file__)))

for file in files:
    module = file.split('.')[0]
    import_module(f'.{module}', package=f'handlers')
