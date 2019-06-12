import handlers
import resource
import seed

from server import server

server.run(host='0.0.0.0', port=8080, workers=1)
