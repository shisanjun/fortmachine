# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import os,sys
import logging
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)


#数据库类型
SQL_TYPE="mysql"
#数据库服务器地址
SQL_HOST="192.168.6.22"
#数据库用户名
SQL_USERNAME="admin"
#数据库密码
SQL_PASSWORD="admin"
#数据库名称
SQL_DB="fortmachine"


#日志级别:DEBUG,INFO,ERROR
LOG_LEVEL=logging.ERROR
#日志文件
LOG_FILE="fort.log"