# -*- coding:utf-8 -*-
__author__ = 'shisanjun'
import os,sys
import logging
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)

from conf import settings

class Log(object):

    def __init__(self):
        self.log_level=settings.LOG_LEVEL
        self.log_file=os.path.join(self.is_dir_exist(),settings.LOG_FILE)

    def is_dir_exist(self):
        log_dir=os.path.join(BASE_DIR,"log")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return log_dir

    def logger(self):

        log_obj=logging.getLogger(__file__)
        log_obj.setLevel(logging.DEBUG)

        ch=logging.StreamHandler()
        ch.setLevel(self.log_level)

        fh=logging.FileHandler(self.log_file,encoding="utf-8")
        fh.setLevel(self.log_level)

        formatter=logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        #判断handler是否已存在，如果存在直接返回，防止生成多个handler对象而多次打印
        if len(log_obj.handlers)>=1:
            return log_obj

        log_obj.addHandler(ch)
        log_obj.addHandler(fh)

        return log_obj
