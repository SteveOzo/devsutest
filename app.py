import tornado.escape
import os.path
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import json


define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="Chucuri1412", help="database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/hello/([^/]+)", HomeHandler)
        ]

        settings = dict(
            page_title=u"Ventas Aliexpress",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/",
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
