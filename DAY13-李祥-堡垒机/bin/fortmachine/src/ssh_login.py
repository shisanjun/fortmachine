#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import os,sys
from sqlalchemy.orm import sessionmaker
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import sys
import traceback
from paramiko.py3compat import input
from src import models
import datetime

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive


def ssh_login(user_obj,bind_host_obj,mysql_engine,log_recording):
    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('开始连接....................')
        #client.connect(hostname, port, username, password)
        client.connect(bind_host_obj.host.host,
                       bind_host_obj.host.port,
                       bind_host_obj.remoteuser.username,
                       bind_host_obj.remoteuser.password,
                       timeout=30)

        cmd_caches = []
        chan = client.invoke_shell()
        # print(repr(client.get_transport()))
        print('*** 登陆主机!\n')
        cmd_caches.append(models.AuditLog(user_id=user_obj.id,
                                          hostuser_id=bind_host_obj.id,
                                          action_type='login',
                                          date=datetime.datetime.now()
                                          ))
        log_recording(user_obj,bind_host_obj,cmd_caches)
        interactive.interactive_shell(chan,user_obj,bind_host_obj,cmd_caches,log_recording)
        chan.close()
        client.close()

    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)