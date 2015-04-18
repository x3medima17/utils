import tornado.web
import tornado.ioloop
import tornado.httpserver
import os

from tornado.options import define, options

define("port",default=8080,help="Service port",type=int)
options.parse_command_line()




class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",MainHandler),
        ]
        
        settings = dict(
            debug = True,
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            login_url = "/auth",
            cookie_secret = "Settings.COOKIE_SECRET",
            
        )
        tornado.web.Application.__init__(self,handlers,**settings)


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world")


if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
