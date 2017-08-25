#作业13

##本节作业


###作业：堡垒机

####要求：
	所有的用户操作日志要保留在数据库中
	每个用户登录堡垒机后，只需要选择具体要访问的设置，就连接上了，不需要再输入目标机器的访问密码
	允许用户对不同的目标设备有不同的访问权限，例:
	对10.0.2.34 有mysql 用户的权限
	对192.168.3.22 有root用户的权限
	对172.33.24.55 没任何权限
	分组管理，即可以对设置进行分组，允许用户访问某组机器，但对组里的不同机器依然有不同的访问权限

####博客地址:
	数据库--mysql介绍 http://www.cnblogs.com/lixiang1013/p/7290372.html
	数据库-mysql安装 http://www.cnblogs.com/lixiang1013/p/7290384.html
	数据库-mysql管理 http://www.cnblogs.com/lixiang1013/p/7290403.html
	数据库-mysql数据类型 http://www.cnblogs.com/lixiang1013/p/7290409.html
	数据库-mysql数据库和表操作 http://www.cnblogs.com/lixiang1013/p/7290443.html
	数据库-mysql数据操作 http://www.cnblogs.com/lixiang1013/p/7290794.html
	数据库-mysql数据连接 http://www.cnblogs.com/lixiang1013/p/7291581.html
	数据库-mysql事务 http://www.cnblogs.com/lixiang1013/p/7291661.html
	数据库-mysql索引 http://www.cnblogs.com/lixiang1013/p/7294002.html
	数据库-mysql视图 http://www.cnblogs.com/lixiang1013/p/7294040.html
	数据库-mysql触发器 http://www.cnblogs.com/lixiang1013/p/7294090.html
	数据库-mysql储存过程 http://www.cnblogs.com/lixiang1013/p/7294207.html
	数据库-mysql函数 http://www.cnblogs.com/lixiang1013/p/7294724.html
	数据库-mysql中文显示问题 http://www.cnblogs.com/lixiang1013/p/7294732.html

	数据库-python操作mysql(pymsql) http://www.cnblogs.com/lixiang1013/p/7294730.html

	ORM介绍 http://www.cnblogs.com/lixiang1013/p/7375589.html
	SQLAlchemy-介绍安装 http://www.cnblogs.com/lixiang1013/p/7375796.html
	SQLAlchemy-方言(Dialects) http://www.cnblogs.com/lixiang1013/p/7380251.html
	SQLAlchemy-对象关系教程ORM-create http://www.cnblogs.com/lixiang1013/p/7382215.html
	SQLAlchemy-对象关系教程ORM-query http://www.cnblogs.com/lixiang1013/p/7384126.html
	SQLAlchemy-对象关系教程ORM-一对多（外键)，一对一，多对多 http://www.cnblogs.com/lixiang1013/p/7392109.html
	SQLAlchemy-对象关系教程ORM-连接，子查询 http://www.cnblogs.com/lixiang1013/p/7397878.html


##程序结构
	├── fortmachine             堡垒机目录
	│   ├── bin					运行目录
	│   │   ├── __init__.py
	│   │   └── start.py        主运行程序
	│   ├── conf					设置目录
	│   │   ├── __init__.py
	│   │   └── settings.py     设置文件
	│   ├── __init__.py
	│   ├── log					日志目录
	│   │   ├── __init__.py
	│   │   └── fort.log        日志文件
	│   └── src					代码目录
	│       ├── actions.py      
	│       ├── adminactive.py  admin交互程序
	│       ├── connection.py   连接程序
	│       ├── fomatter.py		格式化程序
	│       ├── __init__.py
	│       ├── interactive.py  sesstion交互程序
	│       ├── log.py          日志程序
	│       ├── models.py       建表程序
	│       ├── ssh_login.py    登陆远程程序
	│       ├── urls.py         url动作
	│       ├── utils.py        工具程序
	│       ├── views.py        核心功能程序





###1. 程序说明
	所有的用户操作日志要保留在数据库中
	每个用户登录堡垒机后，只需要选择具体要访问的设置，就连接上了，不需要再输入目标机器的访问密码
	允许用户对不同的目标设备有不同的访问权限，例:
	对10.0.2.34 有mysql 用户的权限
	对192.168.3.22 有root用户的权限
	对172.33.24.55 没任何权限
	分组管理，即可以对设置进行分组，允许用户访问某组机器，但对组里的不同机器依然有不同的访问权限

###2. 测试用例

        账号1：admin 密码:admin


###3. 程序测试

        1) 建立数据库
			create database fortmachine charset=utf8;
		2) 初始化表结构
			python DAY13-李祥-堡垒机/bin/fortmachine/bin/start.py syncdb
        3) 建立admin用户
			insert into user(username,password) values("admin","admin");
		4) 管理员功能
			python DAY13-李祥-堡垒机/bin/fortmachine/bin/start.py admin
		5）远程主机操作功能
            python DAY13-李祥-堡垒机/bin/fortmachine/bin/start.py session

####4. 测试

#####1）管理员功能
	python DAY13-李祥-堡垒机/bin/fortmachine/bin/start.py admin
	请输入用户名>>admin
	请输入密码>>admin
	
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
	        
	请选择功能>>2
	序号	主机名	主机地址	端口
	1	web1	192.168.6.22	22
	2	web2	192.168.6.23	22
	3	web3	192.168.6.24	22
	请选择功能>>4
	序号	用户名	密码	类型
	1	root		Auth-key
	2	mysql	123456	Auth-password
	3	web3	None	Auth-password
	4	root	123456	Auth-password
	请选择功能>>6
	序号	主机组名
	1	sh-yw
	2	bj-yw
	请选择功能>>8
	序号	主机组名
	1	admin
	2	shisanjun
	请选择功能>>10
	序号	主机名	主机用户	主机类型
	1	web1	root	Auth-key
	2	web1	root	Auth-password
	请选择功能>>12
	序号	用户名	主机名	主机用户名	主机用户类型
	1	admin	web1	root	Auth-password
	1	admin	web1	root	Auth-key
	请选择功能>>14
	序号	主机组名	主机名	主机用户名
	1	sh-yw	web1	root
	2	bj-yw	web1	root
	请选择功能>>16
	序号	用户	用户组
	1	admin	sh-yw
	1	admin	bj-yw

#####2）远程主机操作功能
 	python DAY13-李祥-堡垒机/bin/fortmachine/bin/start.py session
	欢迎使用保垒机 
	请输入用户名>>admin
	请输入密码>>admin
	system user:admin
	z.	ungroupped hosts (2)
	0.	sh-yw (1)
	1.	bj-yw (1)
	[admin]:1
	------ 主机组: bj-yw ------
	  0.	root@web1(192.168.6.22)
	----------- END -----------
	[(b)返回, (q)退出, 选择主机登陆]:0
	开始连接....................
	C:\Program Files\Python36\lib\site-packages\paramiko\client.py:711: UserWarning: Unknown ssh-rsa host key for 192.168.6.22: b'3aa91a93889d257a427683d9d5704836'
	  key.get_fingerprint())))
	*** 登陆主机!
	
	Line-buffered terminal emulation. Press F6 or ^Z to send EOF.
	
	
	[root@fhyw-6-22 ~]# df
	df
	Filesystem     1K-blocks     Used Available Use% Mounted on
	/dev/sda3       94114700 15882956  73450944  18% /
	tmpfs             961728       72    961656   1% /dev/shm
	/dev/sda1        1032088    63436    916224   7% /boot
	[root@fhyw-6-22 ~]# exit
	exit
	logout
	
	*** EOF ***
	
	
	close ...............
