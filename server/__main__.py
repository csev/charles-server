import argparse

from sanic.log import logger
from sanic.websocket import WebSocketProtocol

import handlers
import resource
import seed
import log

from server import server


parser = argparse.ArgumentParser(description='Fire Server')

parser.add_argument('--websocket', action='store_const', const=True)
parser.add_argument('--workers', default=1)
parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', default=8001)

args = parser.parse_args()


if args.websocket:
    logger.info('Starting Realtime Server...')
    server.run(host=args.host, port=args.port, workers=args.workers, protocol=WebSocketProtocol)
else:
    logger.info('Starting API Server...')
    server.run(host=args.host, port=args.port, workers=args.workers)
