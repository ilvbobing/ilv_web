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

########################################################################
# ilv.conf.db.DB
# 数据库的基本配置
########################################################################
#The class of MyData
class DB:
    #*******************************************************************
    # 一 基本属性
    #*******************************************************************
    
    # 1 数据库基本参数
    #================
    dbType = None # 数据库类型
    dbHost = None # 也可以为：127.0.0.1
    dbUsr = None # 数据库登录用户
    dbPsw = None # 数据库登录密码
    dbName = None # 操作数据库
        
    # 2 连接参数
    col_names = None # 列名数组
    data = None # 数据字典
    conn = None # 链接器
    cursor = None # 结果集
    















   
