import os, sys
import logging

from sanic.log import LOGGING_CONFIG_DEFAULTS
from timber import TimberHandler

source_id = os.getenv('FIRE_TIMBER_SOURCE_ID')
api_key = os.getenv('FIRE_TIMBER_API_KEY')

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'generic': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s [%(levelname)s] %(message)s'
        },
        'access': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s [%(levelname)s] [%(host)s]: %(request)s %(message)s %(status)d %(byte)d'
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
    },
    'loggers': {
        'sanic.root': {
            'level': 'INFO',
            'handlers': [ 'stdout', 'timber' ]
        },
        'sanic.access': {
            'level': 'INFO',
            'handlers': [ 'access', 'timber_access' ]
        },
        'sanic.error': {
            'level': 'INFO',
            'handlers': [ 'stderr', 'timber' ]
        },
        'sanic.app': {
            'level': 'DEBUG',
            'handlers': [ 'stdout', 'timber' ]
        }
    }
})
