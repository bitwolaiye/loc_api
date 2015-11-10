# -*- coding: utf-8 -*-
import os
from tornado import ioloop, web
from handlers import DefaultHandler, LocHandler
from settings import port

__author__ = 'zhouqi'

application = web.Application([
    (r"/api/v1/loc", LocHandler),
    (r"/", DefaultHandler),
], debug=True)

if __name__ == "__main__":
    with open('pid', 'w') as f:
        f.write(str(os.getpid()))
    application.listen(port)
    ioloop.IOLoop.current().start()
