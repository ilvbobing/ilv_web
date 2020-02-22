#!/usr/local/bin/python3
#-*-code:utf8-*-
"""
Sumary:
This is a class of sql.
Params           Type                  Explain
columnNames      list                  The columnName of the table
data             list                  The data of the table
摘要：
这是一个控制数据库的类
"""
import mysql.connector

import ilv.Config

#The class of MyData
class MyData(ilv.Config.Config):
    ################################################################################################
    # 一 基本属性
    ################################################################################################
    columnNames = None #列名称
    data = None #表数据
    cnx = None #链接器
    cursor = None #结果集
    ################################################################################################
    # 二 预设方法
    ################################################################################################
    def __init__(self):
        self.run()
    ################################################################################################
    # 三 主线方法
    # 1 运行数据库
    # 2 获得列数
    ################################################################################################
    ############################################################################################
    # 1 运行数据库
    ############################################################################################
    def run(self):
        self.columnNames = None
        self.data = []
        self.cnx = self.connect()
        self.cursor = self.cnx.cursor()
    ############################################################################################
    # 2 获得列数
    ############################################################################################
    def getColumnCount(self):
        if self.columnNames:
            return(len(self.columnNames))
        else:
            return -1

    ##################################################
    # 获得列的索引
    ##################################################
    def getColumnIndex(self,cName=""):
        columnIndex = -1
        if self.columnNames is None:
            return -1
        i = -1
        for columnName in self.columnNames:
            i += 1
            if columnName == cName:
                columnIndex = i
                break
        return columnIndex
        pass
    def getRowCount(self):
        return(len(self.data))
    def getValueAt(self,row=-1,column=-1):
        if row==-1 or row>=self.getRowCount(self):
            return
        if column==-1 or column>=self.getColumnCount(self):
            return
        rowData = self.data[row]
        return rowData[column]
    def connect(self):
        return mysql.connector.connect(user=self.dbUsr,password=self.dbPsw,host=self.dbHost,database=self.dbName)
    def execute(self,sql = None):
        if sql is None:
            return
        self.cursor.execute(sql)
        self.cnx.commit()
    def executeQuery(self,sql = None):
        if sql is None:
            return
        self.cursor.execute(sql)
        self.columnNames = self.cursor.column_names       
    def close(self):
        if self.cursor != None:
            self.cursor.close()
            self.cursor = None
        if self.cnx != None:
            self.cnx.close()
            self.cnx = None
    def getRowList(self):
        results = []
        for result in self.cursor:
            results.append(result)
        return results
    ##################################################
    # 获得列字典集
    ##################################################
    def getRowDicts(self):
        rowDicts = []
        for result in self.cursor:
            rowDict = self.getRowDict(row=result)
            rowDicts.append(rowDict)
        return rowDicts
    ##################################################
    # 获得列的值
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
    # 获得指定行的字典
    ##################################################
    def get_row(self,dtname="item",kid="",cname="kid"):
        row = None
        rowDict = None
        sql = ""
        sql += " select * from `%s`" % dtname
        sql += " where `%s`='%s'" % (cname,kid)
        sql += " limit 1"
        self.executeQuery(sql)
        rowList = self.getRowList()
        if len(rowList)>0:
            row = rowList[0]
        if row is not None:
            rowDict = self.getRowDict(row=row)     
        return rowDict
        pass
    def getRow(self,dtname="column",kid="",cname="kid"):
        return self.get_row(dtname=dtname,kid=kid,cname=cname)
    ##################################################
    # 获得行字典集
    ##################################################
    def getRowDict(self,row=None):
        rowDict = {}
        i = -1
        for c in row:
            i += 1
            rowDict[self.columnNames[i]] = row[i]
        return rowDict
        pass
   






