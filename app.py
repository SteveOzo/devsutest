import tornado.escape
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

from tornado import gen
from tornado.options import define, options



define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/hello/([^/]+)", HomeHandler)
        ]

        settings = dict(
            page_title=u"Devsu Test",
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    def get(self,slug):
        msg = {}
        msg["message"] = "Hello "+slug
        j=json.dumps(msg)
        self.write(j)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
