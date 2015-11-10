# -*- coding: utf-8 -*-
from decimal import Decimal
from datetime import datetime
from tornado.web import RequestHandler
from models import session, Location

__author__ = 'zhouqi'

class LocHandler(RequestHandler):
    def get(self):
        self.set_status(404)

    def post(self):
        user_id = int(self.get_arguments('user_id'))
        lon_list = [Decimal(each) for each in self.get_argument('lon_list').split(',')]
        lat_list = [Decimal(each) for each in self.get_argument('lat_list').split(',')]
        loc_time_list = [datetime.fromtimestamp(int(each)) for each in self.get_arguments('loc_time_list').split(',')]
        for idx, lon in enumerate(lon_list):
            session.add(Location(**{'user_id': user_id, 'lon': lon_list[idx], 'lat': lat_list[idx], 'loc_time': loc_time_list[idx]}))
        session.commit()
        self.write({'result': True})


class DefaultHandler(RequestHandler):
    def get(self):
        self.set_status(404)

    def post(self):
        self.set_status(404)
