# -*- coding:utf-8 -*-
__author__ = 'shisanjun'
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)

class Fomatter(object):

    def input_str_format(self,input_str):
        """
        格式化字符串输入
        """
        while True:
            format_str=input("%s>>" %input_str).strip()
            if len(format_str)==0:continue
            else:return str(format_str)

    def input_num_format(self,input_str,obj):
        """
        格式化数字输入
        """
        while True:
            format_str=input("%s>>" %input_str).strip()
            if len(format_str)==0 or format_str not in obj:
                continue
            else:
                return int(format_str)

    def show_color(self,s,type="green"):

        if type=="red":
            print("\033[1;31m%s\033[0m" %s)
        elif type=="green":
            print("\033[1;32m%s\033[0m" %s)
        else:
            print("\033[1;33m%s\033[0m" %s)