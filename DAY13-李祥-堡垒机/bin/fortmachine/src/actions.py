# -*- coding:utf-8 -*-
__author__ = 'shisanjun'
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src import urls
def excute_from_command_line(argvs):
    if len(argvs)<2:
        print("\033[32;m可用命令如下:\033[0m")
        for key in urls.actions:
            print("\t",key)
        exit()
    if argvs[1] not in urls.actions:
        print("\033[31;m命令不存在:\033[0m")
        return
    urls.actions[argvs[1]]()