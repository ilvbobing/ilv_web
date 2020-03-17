#!/usr/local/bin/python3
#-*-code:utf8-*-

"""
Sumary:
This is a class of database.
Params           Type                  Explain
columnNames      list                  The columnName of the table
data             list                  The data of the table
摘要：
这是一个控制数据库的类
"""

import ilv.conf.ant

########################################################################
# ilv.core.ant.Ant
# 网络蚂蚁
########################################################################
#The class of Ant
class Ant(ilv.conf.ant.Ant):
    
    #*******************************************************************
    # 1 构造函数
    #*******************************************************************
    def __init__(self,
                 host="localhost", 
                 usr=None, 
                 psw=None):
        self.host = host # 默认抓取本地网站
        self.usr = usr # 网站登陆用户
        self.psw = psw # 网站登记密码
        self.dbName = dbName # 数据库名

    #*******************************************************************
    # 2 运行数据库 需要在子类中重载
    #*******************************************************************




























 




   
