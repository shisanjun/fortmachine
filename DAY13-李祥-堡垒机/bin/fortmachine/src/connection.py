# -*- coding:utf-8 -*-
__author__ = 'shisanjun'
import os,sys
import sqlalchemy
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)
from conf import settings

class Connection(object):
    def __init__(self):
        self.type=settings.SQL_TYPE.lower()
        self.host=settings.SQL_HOST
        self.username=settings.SQL_USERNAME
        self.password=settings.SQL_PASSWORD
        self.db=settings.SQL_DB


    def create_connection(self):
        if self.type=="mysql":
            conn="{_type}+pymysql://{_username}:{_password}@{_host}/{_db}?charset=utf8".format(
                _type=self.type,_username=self.username,_password=self.password,_host=self.host,_db=self.db
            )

        engine=sqlalchemy.create_engine(conn,encoding="utf-8",echo=False)
        return engine