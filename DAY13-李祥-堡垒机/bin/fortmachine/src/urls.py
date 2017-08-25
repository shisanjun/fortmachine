# -*- coding:utf-8 -*-
__author__ = 'shisanjun'
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.views import Views
from src import interactive,adminactive
actions={
    "syncdb":Views.syncdb,
    "admin":adminactive.Interactive,
    "session":Views.start_session

}