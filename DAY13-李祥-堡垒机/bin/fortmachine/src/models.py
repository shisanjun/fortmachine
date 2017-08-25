# -*- coding:utf-8 -*-
__author__ = 'shisanjun'


from sqlalchemy.orm  import relationship
from sqlalchemy import Table,Column,String,Integer,ForeignKey,UniqueConstraint,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

BASE=declarative_base()

#主机组和主机用户关关系多对多
group_m2m_hostuser=Table(
    "group_m2m_hostuser",
    BASE.metadata,
    Column("group_id",Integer,ForeignKey("groups.id")),
    Column("hostuser_id",Integer,ForeignKey("hostuser.id")),)

#系统用户和主机组多对多
user_m2m_groups=Table("user_m2m_groups",
    BASE.metadata,
    Column("group_id",Integer,ForeignKey("groups.id")),
    Column("user_id",Integer,ForeignKey("user.id")),)

#系统用户和主机用户关系多对多
user_m2m_hostuser=Table("user_m2m_hostuser",
    BASE.metadata,
    Column("user_id",Integer,ForeignKey("user.id")),
    Column("hostuser_id",Integer,ForeignKey("hostuser.id")),)

class Hosts(BASE):
    """
    主机信息表
    """
    __tablename__="hosts"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),unique=True)
    host=Column(String(32),unique=True)
    port=Column(Integer,default=22)


    def __repr__(self):
        return "[%s]:[%s]" %(self.name,self.host)


class Groups(BASE):
    """
    主机组信息表
    """
    __tablename__="groups"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),unique=True)

    hostuser=relationship("HostUser",secondary=group_m2m_hostuser,backref="groups",cascade="all, delete")
    user=relationship("User",secondary=user_m2m_groups,backref="groups",cascade="all, delete")

    def __repr__(self):
        return "groups:%s" %self.name

class RemoteUser(BASE):
    """
    主机用户信息表
    """
    __tablename__="remoteuser"
    __table_args__ = (UniqueConstraint('username', 'password','type', name='_user_passwd_uc'),)
    id=Column(Integer,primary_key=True)
    username=Column(String(32))
    password=Column(String(32))

    auth_type={
        "auth-password":"Auth-password",
        "auth-key":"Auth-key",
    }
    type=Column(ChoiceType(auth_type))

    def __repr__(self):
        return "host use name:%s %s" %(self.name,self.type)

class User(BASE):
    """
    系统用户信息表
    """
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    username=Column(String(32),unique=True)
    password=Column(String(32))

    def __repr__(self):
        return "system user:%s" %self.username


class HostUser(BASE):
    """
    主机和主机用户关系表
    """
    __tablename__="hostuser"
    __table_args__ = (UniqueConstraint('host_id', 'remoteuser_id', name='sys_user_passwd_uc'),)
    id=Column(Integer,primary_key=True)
    host_id=Column(Integer,ForeignKey("hosts.id"))
    remoteuser_id=Column(Integer,ForeignKey("remoteuser.id"))

    host=relationship("Hosts")
    remoteuser=relationship("RemoteUser")
    user=relationship("User",secondary=user_m2m_hostuser,backref="hostuser",cascade="all,delete")

    def __repr__(self):
        return "<HostUser(id='%s',name='%s',user='%s')>" % (self.id,
                                                           self.host.name,
                                                           self.remoteuser.username )

class AuditLog(BASE):
    """
    日志表
    """
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    hostuser_id = Column(Integer,ForeignKey('hostuser.id'))
    action_choices = [
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'Exception'),
    ]
    action_choices2 = [
        (u'cmd',u'CMD'),
        (u'login',u'Login'),
        (u'logout',u'Logout'),
        #(3,'GetFile'),
        #(4,'SendFile'),
        #(5,'Exception'),
    ]
    action_type = Column(ChoiceType(action_choices2))
    #action_type = Column(String(64))
    cmd = Column(String(255))
    date = Column(DateTime)

    user = relationship("User",backref="audit_logs")
    hostuser = relationship("HostUser",backref="audit_logs")
