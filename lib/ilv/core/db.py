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
import ilv.conf.db

########################################################################
# ilv.core.db.DB
# 核心数据库操作类
########################################################################
#The class of MyData
class DB(ilv.conf.db.DB):
    
    #*******************************************************************
    # 1 构造函数
    #*******************************************************************
    def __init__(self,
                 dbType = "sqlite",
                 dbHost=None, 
                 dbUsr=None, 
                 dbPsw=None, 
                 dbName="data/sqlite/ilv_db"):
        self.dbType = dbType # 数据库类型
        self.dbHost = dbHost # sqlite 不需要数据服务器
        self.dbUsr = dbUsr # sqlite 不需要用户名
        self.dbPsw = dbPsw # sqlite 不需要密码
        self.dbName = dbName # 数据库名

    #*******************************************************************
    # 2 运行数据库 需要在子类中重载
    #*******************************************************************
    def run(self):
        self.conn = sqlite3.connect(database=self.dbName)
        self.cursor = self.conn.cursor()
        pass

    #*******************************************************************
    # 3 获得列名数组 需要重载
    #*******************************************************************
    def get_col_names(self):
        self.col_names = [tuple[0] for tuple in self.cursor.description]
        return self.col_names
        pass           
    #*******************************************************************
    # 4 导入sql集
    #*******************************************************************
    def execute_sqls(self,sqls_str=None):
        
        # 1 逐句去掉注释
        split_array = None
        if sqls_str.find("\r\n")!=-1:
            sql_array = sqls_str.split("\r\n")
        elif sqls_str.find("\r")!=-1:
            sql_array = sqls_str.split("\r")
        elif sqls_str.find("\n")!=-1:
            sql_array = sqls_str.split("\n")
        else:
            print("ilv.core.db.DB.execute_sqls:未找到换行符")
        sqls_str = ""
        for sql in sql_array:
            split_array = sql.split("#",1)
            sqls_str += split_array[0]
        
        # 逐条执行SQL语句
        sql_array = sqls_str.split(";")
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
                sql = sql.replace('\r\n',' ')
                sql = sql.replace('\r',' ')
                sql = sql.replace('\n',' ')
                sql = sql.replace('\t',' ')
                old_sql = sql
                new_sql = old_sql.replace('  ',' ')
                while new_sql != old_sql:
                    old_sql = new_sql
                    new_sql = old_sql.replace('  ',' ')
                sql = new_sql
                # sql = sql.replace(x'0a','')
                print(sql+";\r\n")
                self.cursor.execute(sql)
        self.conn.commit()        
        
    #*******************************************************************
    # 5 导入sql文件
    #*******************************************************************
    def execute_file(self,path="data/sqlite/setup.sql"):
        sqls_str = ""
        split_array = None             
        
        # 读取SQL语句
        output = open(path,mode='r',buffering=1)
        data = output.readline()
        while data:
            # 如果是注释语句，直接跳过
            if data.find("#")==0:
                data = output.readline()
                continue
            split_array = data.split("#",1)
            sqls_str += split_array[0]
            data = output.readline()
        self.execute_sqls(sqls_str=sqls_str)
        
    #*******************************************************************
    # 6 关闭数据库
    #*******************************************************************
    def close(self):
        if self.cursor != None:
            self.cursor.close()
            self.cursor = None
        if self.conn != None:
            self.conn.close()
            self.conn = None
        self.col_names = None # 列名数组
        self.data = None # 数据字典

    #*******************************************************************
    # 7 获得列数
    #*******************************************************************
    def get_column_count(self):
        if self.col_names:
            return(len(self.col_names))
        else:
            return -1
        
    #*******************************************************************
    # 8 获得行数
    #*******************************************************************
    def get_row_count(self):
        return(len(self.data))
    
    #*******************************************************************
    # 9 获得列的索引
    #*******************************************************************
    def get_column_index(self,cName=""):
        columnIndex = -1
        if self.col_names is None:
            return -1
        i = -1
        for columnName in self.col_names:
            i += 1
            if columnName == cName:
                columnIndex = i
                break
        return columnIndex
        pass

    #*******************************************************************
    # 10 获取单元格数值
    #*******************************************************************
    def get_value_at(self,row=-1,column=-1):
        if row==-1 or row>=self.getRowCount(self):
            return
        if column==-1 or column>=self.getColumnCount(self):
            return
        rowData = self.data[row]
        return rowData[column]

    #*******************************************************************
    # 11 变更sql语句
    #*******************************************************************
    def execute(self,sql = None):
        if sql is None:
            return
        self.cursor.execute(sql)
        self.conn.commit()
        
    #*******************************************************************
    # 12 查询sql语句
    #*******************************************************************
    def execute_query(self,sql = None):
        if sql is None:
            return
        self.cursor.execute(sql)
        
    #*******************************************************************
    # 13 获得行数组
    #*******************************************************************
    def get_row_list(self):
        results = []
        for result in self.cursor:
            results.append(result)
        return results
        
    ##################################################
    # 14 获得列的值
    ##################################################
    def get(self,row=None,cName=""):
        cValue = ""
        if row is None:
            return "MyData.get(row,cName)参数row不能为None"
        if cName == "":
            return "MyData.get(row,cName)cName不能为空"
        cIndex = self.getColumnIndex(cName=cName)
        if cIndex!=-1:
            return row[cIndex]
        return cValue
        pass

    ##################################################
    # 15 获得指定行的字典
    ##################################################
    def get_row(self,dtname="item",kid="",cname="kid"):
        row_dict = {}
        sql = "SELECT * FROM %s WHERE `%s`='%s'" % (dtname,cname,kid)
        # print("DB_Base.get_row:sql="+sql+";\r\n")
        self.cursor.execute(sql)
        col_name_list = self.get_col_names()
        col_value_list = self.cursor.fetchone()
        if col_value_list is None:
            print("ilv.core.db.DB.get_row:col_value_list is None,sql="+sql)
        i = 0
        while i < len(col_name_list):
            col_name = col_name_list[i]
            col_value = col_value_list[i]
            row_dict[col_name] = col_value
            i+=1
        return row_dict
 
    ##################################################
    # 16 获得行字典集
    ##################################################
    def get_row_dict(self,row=None):
        row_dict = {}
        col_names = self.get_col_names()
        i = -1
        for c in row:
            i += 1
            row_dict[col_names[i]] = row[i]
        return row_dict
        pass

    ##################################################
    # 17 获得列字典集
    ##################################################
    def get_row_dicts(self):
        rowDicts = []
        for result in self.cursor:
            rowDict = self.get_row_dict(row=result)
            rowDicts.append(rowDict)
        return rowDicts



























 




   
