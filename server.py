import tornado.ioloop
import tornado.web
from tornado.options import define, options
import logging
import os

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('server.py');

define("port", default=8888, help="run on the given port", type=int)
class MainHandler(tornado.web.RequestHandler):

    def get(self):
        logger.debug("received request")
        self.render("index.html")

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/w", MainHandler)
            # (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__),'static')})
            # Add more paths here
        ]
        settings = {
            "debug": True
            # 'static_path': os.path.join(os.path.dirname(__file__),'static')

        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    # app.listen(8888)
    tornado.options.parse_command_line()
    app.listen(options.port)
    logger.info("Starting tornado server on port %d" ,(options.port))
    tornado.ioloop.IOLoop.instance().start()
