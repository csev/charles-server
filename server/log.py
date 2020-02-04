import os, sys
import logging

source_id = os.getenv('CHARLES_TIMBER_SOURCE_ID')
api_key = os.getenv('CHARLES_TIMBER_API_KEY')

config = {
    'version': 1,
    'formatters': {
        'generic': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(process)d %(message)s'
        },
        'access': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(process)d %(host)s %(request)s %(message)s %(status)d %(byte)d'
        }
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'generic'
        },
        'stderr': {
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'formatter': 'generic'
        },
        'access': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'access'
        },

    },
    'loggers': {
        'sanic.root': {
            'level': 'INFO',
            'handlers': [ 'stdout' ]
        },
        'sanic.access': {
            'level': 'INFO',
            'handlers': [ 'access' ]
        },
        'sanic.error': {
            'level': 'INFO',
            'handlers': [ 'stderr' ]
        }
    }
}

if source_id and api_key:
    config['handlers'].update({
        'timber': {
            'level': 'DEBUG',
            'class': 'timber.TimberHandler',
            'formatter': 'generic',
            'api_key': api_key,
            'source_id': source_id
        },
        'timber_access': {
            'level': 'DEBUG',
            'class': 'timber.TimberHandler',
            'formatter': 'access',
            'api_key': api_key,
            'source_id': source_id
        }
    })
    config['loggers']['sanic.root']['handlers'].append('timber')
    config['loggers']['sanic.access']['handlers'].append('timber_access')
    config['loggers']['sanic.error']['handlers'].append('timber')

logging.config.dictConfig(config)
