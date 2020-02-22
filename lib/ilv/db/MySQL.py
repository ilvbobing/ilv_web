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

import mysql.connector
import ilv.db.DB_Base

########################################################################
# 基础数据方法
########################################################################
#The class of MyData
class MySQL(ilv.db.DB_Base.DB_Base):
    
    #*******************************************************************
    # 1 构造函数
    #*******************************************************************
    def __init__(self,
                 dbHost="localhost", 
                 dbUsr="root", 
                 dbPsw="", 
                 dbName="ilv_db"):
        self.dbType = "mysql"
        self.dbHost = dbHost # sqlite 不需要数据服务器
        self.dbUsr = dbUsr # sqlite 不需要用户名
        self.dbPsw = dbPsw # sqlite 不需要密码
        self.dbName = dbName # 数据库名

    #*******************************************************************
    # 2 连接数据库
    #*******************************************************************
    def run(self):
        self.columnNames = None
        self.data = []
        self.conn = mysql.connector.connect(user=self.dbUsr,password=self.dbPsw,host=self.dbHost,database=self.dbName)
        self.cursor = self.conn.cursor()
        pass
            
    #*******************************************************************
    # 2 获得列名数组
    #*******************************************************************
    def get_col_names(self):
        self.col_names = self.cursor.column_names
        return self.col_names
        pass

 







































   
