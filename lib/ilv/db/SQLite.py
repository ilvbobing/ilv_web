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

import sqlite3
import ilv.db.DB_Base

########################################################################
# 基础数据方法
########################################################################
#The class of MyData
class SQLite(ilv.db.DB_Base.DB_Base):
    
    #*******************************************************************
    # 1 构造函数
    #*******************************************************************
    def __init__(self,
                 dbHost=None, 
                 dbUsr=None, 
                 dbPsw=None, 
                 dbName="data/sqlite/ilv_db"):
        self.dbType = "sqlite"
        self.dbHost = dbHost # sqlite 不需要数据服务器
        self.dbUsr = dbUsr # sqlite 不需要用户名
        self.dbPsw = dbPsw # sqlite 不需要密码
        self.dbName = dbName # 数据库名

    #*******************************************************************
    # 2 连接数据库
    #*******************************************************************
    def run(self):
        self.conn = sqlite3.connect(database=self.dbName)
        self.cursor = self.conn.cursor()
        pass
            
    #*******************************************************************
    # 2 获得列名数组
    #*******************************************************************
    def get_col_names(self):
        self.col_names = [tuple[0] for tuple in self.cursor.description]
        return self.col_names
        pass



























 




   
