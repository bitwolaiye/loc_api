# -*- coding: utf-8 -*-
from tornado.options import options

__author__ = 'zhouqi'

port = 8888
database_bitcoin_username, database_bitcoin_password  = 'loc_api', 'loc_api',
database_bitcoin_host, database_bitcoin_port, database_bitcoin_instance = '127.0.0.1', 3306, 'loc_api'


def init():
    """
    load from conf
    :return:
    """
    pass

init()