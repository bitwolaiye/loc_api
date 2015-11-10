# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, SMALLINT, Integer, DECIMAL, DATETIME, text

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import database_bitcoin_username, database_bitcoin_instance, database_bitcoin_port, database_bitcoin_host, \
    database_bitcoin_password

__author__ = 'zhouqi'

engine = create_engine('mysql://%s:%s@%s:%d/%s' % (
    database_bitcoin_username, database_bitcoin_password, database_bitcoin_host, database_bitcoin_port,
    database_bitcoin_instance))
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine
session = sessionmaker(bind=engine)()

class Location(DeclarativeBase):
    __tablename__ = 'locations'

    __table_args__ = {}

    # column definitions
    loc_id = Column(u'loc_id', INTEGER(), nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(u'user_id', INTEGER(), nullable=False)
    lon = Column(u'lon', DECIMAL(), nullable=False)
    lat = Column(u'lat', DECIMAL(), nullable=False)
    loc_time = Column(u'loc_time', DATETIME(), nullable=False)

    # relation definitions

location_sql = '''
create table locations
(
  loc_id int not null auto_increment,
  user_id int not null,
  lon DECIMAL(11, 8) NOT NULL ,
  lat DECIMAL(11, 8) NOT NULL ,
  loc_time DATETIME NOT NULL ,
   primary key (loc_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
'''

def init():
    session = sessionmaker(bind=engine)()
    tables = session.connection().execute(text('show tables;')).fetchall()
    if len(tables) == 0:
        session.connection().execute(text(location_sql))
        session.commit()

init()
