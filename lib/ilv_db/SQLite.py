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

import os
import sqlite3
import ilv_db.DbBase

########################################################################
# 基础数据方法
########################################################################
#The class of MyData
class SQLite(ilv_db.DbBase.DbBase):
    
    #*******************************************************************
    # 1 构造函数
    #*******************************************************************
    def __init__(self):
        self.dbHost = None # sqlite 不需要数据服务器
        self.dbUsr = None # sqlite 不需要用户名
        self.dbPsw = None # sqlite 不需要密码
        self.dbName = "data/sqlite/ilv_db" # 数据库名
        self.run()

    #*******************************************************************
    # 2 连接数据库
    #*******************************************************************
    def run(self):
        self.conn = sqlite3.connect(database=self.dbName)
        self.cursor = self.conn.cursor()
        pass
        
    #*******************************************************************
    # 3 关闭数据库
    #*******************************************************************
    def close(self):
        self.cursor.close()
        self.conn.close()
        pass

    #*******************************************************************
    # 4 导入sql文件
    #*******************************************************************
    def executeFile(self,path="data/sqlite/setup.sql"):
        sql_str = ""
        split_array = None        
        sql_array = None       
        
        # 1. 读取SQL语句
        output = open(path,mode='r',buffering=1)
        data = output.readline()
        while data:
            # 如果是注释语句，直接跳过
            if data.find("#")==0:
                data = output.readline()
                continue
            split_array = data.split("#",1)
            sql_str += split_array[0]
            data = output.readline()
        # 2. 分割SQL语句
        sql_array = sql_str.split(";")
        
        # 3. 逐条执行SQL语句
        for sql in sql_array:
            ignore = True
            if sql.find("select")!=-1:
                ignore = False
            if sql.find("SELECT")!=-1:
                ignore = False
            if sql.find("insert")!=-1:
                ignore = False
            if sql.find("INSERT")!=-1:
                ignore = False
            if sql.find("update")!=-1:
                ignore = False
            if sql.find("UPDATE")!=-1:
                ignore = False
            if sql.find("create")!=-1:
                ignore = False
            if sql.find("CREATE")!=-1:
                ignore = False
            if sql.find("drop")!=-1:
                ignore = False
            if sql.find("DROP")!=-1:
                ignore = False

            if not ignore:
                sql = sql.replace('\r\n','')
                sql = sql.replace('\r','')
                sql = sql.replace('\n','')
                sql = sql.replace('\t','')
                old_sql = sql
                new_sql = old_sql.replace('  ',' ')
                while new_sql != old_sql:
                    old_sql = new_sql
                    new_sql = old_sql.replace('  ',' ')
                sql = new_sql
                #sql = sql.replace(x'0a','')
                print(sql+";\r\n")
                self.cursor.execute(sql)
        #return sql_str
        
    #*******************************************************************
    # 3 获得列数
    #*******************************************************************
    def getColumnCount(self):
        return -1
        
    #*******************************************************************
    # 4 获得行数
    #*******************************************************************
    def getRowCount(self):
        return(len(self.data))
    
    #*******************************************************************
    # 5 获得列的索引
    #*******************************************************************
    def getColumnIndex(self,cName=""):
        return -1

    #*******************************************************************
    # 6 获取单元格数值
    #*******************************************************************
    def getValueAt(self,row=-1,column=-1):
        return None

    #*******************************************************************
    # 7 获取单元格数值
    #*******************************************************************
    def connect(self):
        return None

    #*******************************************************************
    # 8 变更sql语句
    #*******************************************************************
    def execute(self,sql = None):
        pass
        
    #*******************************************************************
    # 9 查询sql语句
    #*******************************************************************
    def executeQuery(self,sql = None):
        return       


    #*******************************************************************
    # 11 获得行数组
    #*******************************************************************
    def getRowList(self):
        return None
        
    ##################################################
    # 获得列字典集
    ##################################################
    def getRowDicts(self):
        return None

    ##################################################
    # 获得列的值
    ##################################################
    def get(self,row=None,cName=""):
        return None

    ##################################################
    # 获得指定行的字典
    ##################################################
    def get_row(self,dtname="item",kid="",cname="kid"):
        return None
 
    #*******************************************************************
    # 根据指定的索引，获得列
    #*******************************************************************
    def getRow(self,dtname="column",kid="",cname="kid"):
        return None

    ##################################################
    # 获得行字典集
    ##################################################
    def getRowDict(self,row=None):
        return None
   
