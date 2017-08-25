# -*- coding:utf-8 -*-
__author__ = 'shisanjun'


import os,sys
from sqlalchemy.orm import sessionmaker
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src.utils import yaml_parser,print_err
from src import models
from src.connection import Connection
from src.fomatter import Fomatter
from src.log import Log
from src.ssh_login import ssh_login
class Views(object):
    engine=Connection().create_connection()
    logger=Log().logger()
    fomatter=Fomatter()
    Session=sessionmaker(bind=engine)
    session=Session()
    def __init__(self):


        self.auth_dict={}


    @classmethod
    def syncdb(self,argvs):
        """
        创建表结构
        :param argvs:
        :return:
        """
        from src.models import BASE
        BASE.metadata.create_all(bind=self.engine)

    def auth(self):
        """
        用户认证
        :return:
        """
        username=self.fomatter.input_str_format("请输入用户名")
        password=self.fomatter.input_str_format("请输入密码")
        user_obj=self.session.query(models.User).filter(models.User.username==username,models.User.password==password).first()
        if user_obj is None:
            self.auth_dict["username"]=username
            self.auth_dict["is_auth"]=False
            self.logger.debug("用户认证失败")
        else:
            self.auth_dict["username"]=username
            self.auth_dict["is_auth"]=True
            self.logger.debug("用户认证成功")
        return self.auth_dict

    def host_add(self,*args):
        """
        增加主机
        :param args:
        :return:
        """
        name=self.fomatter.input_str_format("请输入主机名")
        host=self.fomatter.input_str_format("请输入主机地址")
        port=self.fomatter.input_str_format("请输入主机端口")

        host_obj=models.Hosts(name=name,host=host,port=port)
        try:
            self.session_add(host_obj)
        except Exception as e:
            print(e)

    def host_list(self,*args):
        """
        查看所有主机
        :param args:
        :return:
        """
        host_objs=self.session.query(models.Hosts).all()
        if len(host_objs)==0:
             self.logger.info("主机表为空")
             return None
        else:
            self.fomatter.show_color("序号\t主机名\t主机地址\t端口")

            for host in host_objs:
                self.fomatter.show_color("%s\t%s\t%s\t%s" %(host.id,host.name,host.host,host.port))
        return True

    def group_add(self,*args):
        """
        增加主机组
        :param args:
        :return:
        """
        name=self.fomatter.input_str_format("请输入主机名")
        group_obj=models.Groups(name=name)
        try:
            self.session_add(group_obj)
        except Exception as e:
            print(e)

    def group_list(self,*args):
        """
        查看所有主机
        :param args:
        :return:
        """
        group_objs=self.session.query(models.Groups).all()
        if len(group_objs)==0:
             self.logger.info("主机表组为空")
             return None
        else:
            self.fomatter.show_color("序号\t主机组名")

            for group_obj in group_objs:
                self.fomatter.show_color("%s\t%s" %(group_obj.id,group_obj.name))
        return True

    def remoteuser_add(self,*args):
        """
        增加主机用户
        :param args:
        :return:
        """
        name=self.fomatter.input_str_format("请输入主机用户名")
        password=self.fomatter.show_color(input("请输入密码>>"))
        while True:
            type=self.fomatter.input_str_format("请选择类型1：密码；2秘钥")
            if type not in ("1","2"):
                continue
            else:break

        if type=="1":
            remoteuser_obj=models.RemoteUser(username=name,password=password,type="auth-password")
        elif type=="2":
            remoteuser_obj=models.RemoteUser(username=name,password=password,type="auth-key")
        try:
            self.session_add(remoteuser_obj)
        except Exception as e:
            print(e)

    def remoteuser_list(self,*args):
        """
        查看所有主机用户
        :param args:
        :return:
        """
        remoteuser_objs=self.session.query(models.RemoteUser).all()
        if len(remoteuser_objs)==0:
             self.logger.info("主机用户表为空")
             return None
        else:
            self.fomatter.show_color("序号\t用户名\t密码\t类型")

            for remoteuser_obj in remoteuser_objs:
                self.fomatter.show_color("%s\t%s\t%s\t%s" %(remoteuser_obj.id,remoteuser_obj.username,remoteuser_obj.password,remoteuser_obj.type.value))
        return True

    def user_add(self,*args):
        """
        增加系统用户
        :param args:
        :return:
        """
        name=self.fomatter.input_str_format("请输入系统用户名")
        password=self.fomatter.input_str_format("请输入系统用户密码")
        user_obj=models.User(username=name,password=password)
        try:
            self.session_add(user_obj)
        except Exception as e:
            print(e)

    def user_list(self,*args):
        """
        查看所有主机
        :param args:
        :return:
        """
        user_objs=self.session.query(models.User).all()
        if len(user_objs)==0:
             self.logger.info("系统用户表为空")
             return None
        else:
            self.fomatter.show_color("序号\t主机组名")

            for user_obj in user_objs:
                self.fomatter.show_color("%s\t%s" %(user_obj.id,user_obj.username))
        return True

    def hostuser_add(self,*args):
        """
        关联主机和主机用户
        :param args:
        :return:
        """
        if self.host_list() is None:
            self.logger.info("主机为空，请先添加主机")
            return
        host_id=self.fomatter.input_str_format("请输入主机序号")

        host_obj=self.session.query(models.Hosts).filter_by(id=host_id).first()
        if host_obj is None:
            self.logger.error("输入主机序号有误，请重新输入")
            return

        if self.remoteuser_list() is None:
            self.logger.info("主机用户为空，请先增加主机用户")
            return
        remoteuser_id=self.fomatter.input_str_format("请输入主机用户号")

        remoteuser_obj=self.session.query(models.RemoteUser).filter_by(id=remoteuser_id).first()
        if remoteuser_obj is None:
            self.logger.error("输入主机用户序号有误，请重新输入")
            return

        host_user_obj=models.HostUser(host_id=host_id,remoteuser_id=remoteuser_id)
        try:
            self.session_add(host_user_obj)
        except Exception as e:
            self.session.rollback()
            self.logger.info("记录已存在")

    def hostuser_list(self,*args):
        """
        查看所有主机和主机用户关联
        :param args:
        :return:
        """
        host_user_objs=self.session.query(models.HostUser).all()
        if len(host_user_objs)==0:
             self.logger.info("没有主机和主机用户关系")
             return None
        else:
            self.fomatter.show_color("序号\t主机名\t主机用户\t主机类型")

            for host_user_obj in host_user_objs:
                self.fomatter.show_color("%s\t%s\t%s\t%s" %(host_user_obj.id,
                    host_user_obj.host.name,host_user_obj.remoteuser.username,host_user_obj.remoteuser.type.value))
        return True

    def user_hostuser_add(self,*args):
        """
        增加系统用户和主机及用户关系统
        :param args:
        :return:
        """
        if self.user_list() is None:
            self.logger.info("用户表为空，请先添加")
            return
        user_id=self.fomatter.input_str_format("请输入用户序号")

        user_obj=self.session.query(models.User).filter_by(id=user_id).first()
        if user_obj is None:
            self.logger.error("输入用户序号有误，请重新输入")
            return

        if self.hostuser_list() is None:
            self.logger.info("请先增加主机和主机用户关系")
            return
        hostuser_id=self.fomatter.input_str_format("请输入主机与用户关系序号")

        hostuser_obj=self.session.query(models.HostUser).filter_by(id=hostuser_id).first()
        if hostuser_obj is None:
            self.logger.error("输入主机和用户关系序号有误，请重新输入")
            return
        if hostuser_obj not in user_obj.hostuser:
            user_obj.hostuser.append(hostuser_obj)

        try:
            self.session_add(user_obj)
        except Exception as e:
            self.session.rollback()
            self.logger.info("记录已存在")

    def user_hostuser_list(self,*args):
        """
        查看系统用户和主机及用户关系统
        :param args:
        :return:
        """
        user_objs=self.session.query(models.User).all()
        if user_objs is None:
            self.logger.error("输入主机和用户关系序号有误，请重新输入")

        self.fomatter.show_color("序号\t用户名\t主机名\t主机用户名\t主机用户类型")
        for user_obj in user_objs:
            for hostuser_obj in user_obj.hostuser:
                self.fomatter.show_color("%s\t%s\t%s\t%s\t%s" %(user_obj.id,
                    user_obj.username,hostuser_obj.host.name,hostuser_obj.remoteuser.username,hostuser_obj.remoteuser.type.value))

    def group_hostuser_add(self,*args):
        """
        增加主机组和主机及用户关系统
        :param args:
        :return:
        """
        if self.group_list() is None:
            self.logger.info("用户组表为空，请先添加")
            return
        group_id=self.fomatter.input_str_format("请输入用户序号")

        group_obj=self.session.query(models.Groups).filter_by(id=group_id).first()
        if group_obj is None:
            self.logger.error("输入用户组序号有误，请重新输入")
            return

        if self.hostuser_list() is None:
            self.logger.info("请先增加主机和主机用户关系")
            return
        hostuser_id=self.fomatter.input_str_format("请输入主机与用户关系序号")

        hostuser_obj=self.session.query(models.HostUser).filter_by(id=hostuser_id).first()
        if hostuser_obj is None:
            self.logger.error("输入主机和用户关系序号有误，请重新输入")
            return
        if hostuser_obj not in group_obj.hostuser:
            group_obj.hostuser.append(hostuser_obj)
        try:
            self.session_add(group_obj)
        except Exception as e:
            self.session.rollback()
            self.logger.info("记录已存在")

    def group_hostuser_list(self,*args):
        """
        查看主机组和主机及用户关系统
        :param args:
        :return:
        """
        group_objs=self.session.query(models.Groups).all()
        if group_objs is None:
            self.logger.error("输入主机和用户关系序号有误，请重新输入")

        self.fomatter.show_color("序号\t主机组名\t主机名\t主机用户名")
        for group_obj in group_objs:
            for hostuser_obj in group_obj.hostuser:
                self.fomatter.show_color("%s\t%s\t%s\t%s" %(group_obj.id,
                    group_obj.name,hostuser_obj.host.name,hostuser_obj.remoteuser.username))

    def user_group_add(self,*args):
        """
        增加系统用户和主机组关系统
        :param args:
        :return:
        """
        if self.user_list() is None:
            self.logger.info("用户表为空，请先添加")
            return
        user_id=self.fomatter.input_str_format("请输入用户序号")

        user_obj=self.session.query(models.User).filter_by(id=user_id).first()
        if user_obj is None:
            self.logger.error("输入用户序号有误，请重新输入")
            return

        if self.group_list() is None:
            self.logger.info("请先增加主机组")
            return
        group_id=self.fomatter.input_str_format("请输入主机组序号")

        group_obj=self.session.query(models.Groups).filter_by(id=group_id).first()
        if group_obj is None:
            self.logger.error("输入主机和用户关系序号有误，请重新输入")
            return
        if group_obj not in user_obj.groups:
            user_obj.groups.append(group_obj)
        try:
            self.session_add(user_obj)
        except Exception as e:
            self.logger.info("系统用户与主机组记录已存在")
            self.session.rollback()

    def user_group_list(self,*args):
        """
        查看系统用户和主机组关系统
        :param args:
        :return:
        """
        user_objs=self.session.query(models.User).all()
        if user_objs is None:
            self.logger.error("输入主机和用户关系序号有误，请重新输入")

        self.fomatter.show_color("序号\t用户\t用户组")
        for user_obj in user_objs:
            for group_obj in user_obj.groups:
                self.fomatter.show_color("%s\t%s\t%s" %(user_obj.id,user_obj.username,group_obj.name))

    def session_add(self,data):
        """
        数据提交
        :param data:
        :return:
        """
        if type(data)=="list":
            self.session.add_all(data)
        else:
            self.session.add(data)
        self.session.commit()

    @classmethod
    def start_session(self):
        """
        用户会话
        :return:
        """
        print('欢迎使用保垒机 ')
        username=self.fomatter.input_str_format("请输入用户名")
        password=self.fomatter.input_str_format("请输入密码")
        user_obj=self.session.query(models.User).filter(models.User.username==username,models.User.password==password).first()
        if user_obj:
            self.fomatter.show_color(user_obj)
            # print(user_obj.hostuser)
            # print(user_obj.groups)
            exit_flag = False
            while not exit_flag:
                if user_obj.hostuser:
                    print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' %len(user_obj.hostuser) )
                for index,group in enumerate(user_obj.groups):
                    print('\033[32;1m%s.\t%s (%s)\033[0m' %(index,group.name,  len(group.hostuser)) )

                choice = input("[%s]:" % user_obj.username).strip()
                if len(choice) == 0:continue
                if choice == 'z':
                    print("------ 主机组: 分未配的主机 ------" )
                    for index,hostuser in enumerate(user_obj.hostuser):
                        print("  %s.\t%s@%s(%s)"%(index,
                                                  hostuser.remoteuser.username,
                                                  hostuser.host.name,
                                                  hostuser.host.host,
                                                  ))
                    print("----------- END -----------" )
                elif choice.isdigit():
                    choice = int(choice)
                    if choice < len(user_obj.groups):
                        print("------ 主机组: %s ------"  % user_obj.groups[choice].name )
                        for index,bind_host in enumerate(user_obj.groups[choice].hostuser):
                            print("  %s.\t%s@%s(%s)"%(index,
                                                      bind_host.remoteuser.username,
                                                      bind_host.host.name,
                                                      bind_host.host.host,
                                                      ))
                        print("----------- END -----------" )

                        #host selection
                        while not exit_flag:
                            user_option = input("[(b)返回, (q)退出, 选择主机登陆]:").strip()
                            if len(user_option)==0:continue
                            if user_option == 'b':break
                            if user_option == 'q':
                                exit_flag=True
                            if user_option.isdigit():
                                user_option = int(user_option)
                                if user_option < len(user_obj.groups[choice].hostuser) :
                                    # print('host:',user_obj.groups[choice].hostuser[user_option])
                                    # print('audit log:',user_obj.groups[choice].hostuser[user_option].audit_logs)
                                    ssh_login(user_obj,
                                                        user_obj.groups[choice].hostuser[user_option],
                                                        self.session,
                                                        self.log_recording)
                    else:
                        print("no this option..")

    @classmethod
    def log_recording(self,user_obj,bind_host_obj,logs):
        '''
        日志记录
        '''
        # print("\033[41;1m--logs:\033[0m",logs)

        self.session.add_all(logs)
        self.session.commit()