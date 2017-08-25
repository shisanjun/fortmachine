# -*- coding:utf-8 -*-
__author__ = 'shisanjun'
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.actions import excute_from_command_line
if __name__=="__main__":

    excute_from_command_line(sys.argv)