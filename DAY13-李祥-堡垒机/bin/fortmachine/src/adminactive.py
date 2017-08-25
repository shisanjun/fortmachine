# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import os,sys
import sqlalchemy
from  sqlalchemy.orm import sessionmaker
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)

from src.views import Views
from src.fomatter import Fomatter
class Interactive(object):

    def __init__(self):
        self.func_obj=Views()
        self.fomatter_obj=Fomatter()
        self.interaction()

    def interaction(self):

        admin_print="""
        --------------------管理员界面-----------------------------
        0: 退出
        1. 增加主机                   2.查看所有主机信息
        3. 增加主机用户               4.查看主机用户
        5. 增加主机组                 6.查看所有主机组
        7. 增加系统用户               8.查看所有系统用户
        9. 主机分配主机用户           10.主机关联主机用户
        11.主机分配系统用户           12.主机关联系统用户
        13.主机分配主机组             14.主机关联主机组
        15.系统用户分配主机组         16.系统用户关联主机组
        """

        student_print="""
        --------------------用户界面-----------------------------
        0:退出 　　　　1.提交作业　　　　　2.查看成绩　　　3.班级成绩总分排名
        """

        admin_menu={
            "0":exit,
            "1":self.func_obj.host_add,
            "2":self.func_obj.host_list,
            "3":self.func_obj.remoteuser_add,
            "4":self.func_obj.remoteuser_list,
            "5":self.func_obj.group_add,
            "6":self.func_obj.group_list,
            "7":self.func_obj.user_add,
            "8":self.func_obj.user_list,
            "9":self.func_obj.hostuser_add,
            "10":self.func_obj.hostuser_list,
            "11":self.func_obj.user_hostuser_add,
            "12":self.func_obj.user_hostuser_list,
            "13":self.func_obj.group_hostuser_add,
            "14":self.func_obj.group_hostuser_list,
            "15":self.func_obj.user_group_add,
            "16":self.func_obj.user_group_list,
        }

        student_menu={
            "0":exit,
            # "1":self.func_obj.sumbit_user_record,
            # "2":self.func_obj.score_query,
            # "3":self.func_obj.sum_score_list
        }

        is_login=self.func_obj.auth()
        if is_login.get("is_auth"):
            if is_login.get("username")=="admin":
                print_str=admin_print
                menu_func=admin_menu
            else:
                print_str=student_print
                menu_func=student_menu

            print(print_str)
            while True:
                num=input("请选择功能>>")
                if len(num)==0 or num not in menu_func:
                     continue
                else:
                    menu_func[num](is_login.get("user_id"))
