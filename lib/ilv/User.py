#!/usr/local/bin/python3
#-*-code:utf8-*-
"""
1.This is a base class of html.
2.When import this class we can get a default html.
3.The other class (for exampe Microblog) is the child of MyBase
"""
# python library
import os,datetime

import ilv.Base
####################################################################################################
# User
####################################################################################################
class User(ilv.Base.Base):
    ################################################################################################
    # I standard parameters
    ################################################################################################
    ############################################################################################
    # 1 contructure
    ############################################################################################
    def __init__(self,env=None):
        ilv.Base.Base.__init__(self,env=env)
    ################################################################################################
    # III helpful method
    ################################################################################################
    ####################################################################################
    # 3.1.5 regedit/edit regedit user
    ####################################################################################
    def edit(self):
        # 1 set the form html
        sup = self.getSup()
        urlDict = self.urlDict
        act = urlDict["act"]
        if act=="add":
            html = self.getTemplet(sup,"add")
        elif act=="edit":
            html = self.getTemplet(sup,"edit")
        else:
            self.addMsg("act error when use User.edit() act=%s" % str(act))
        html = html.replace("ilv_action",self.action)
        act = ""
        aim = ""
        title = ""
        account = ""   
        summary = ""
        detail = ""     
        t = ilv.Time.Time()
        datetime = t.getDatetime()
        millisecond = t.getMillisecond()
        ip = self.env.getClient()
        msg = ""
        if self.urlDict and "act" in self.urlDict:
            act = self.urlDict["act"]
        aimRow = None
        if act=="edit":
            aimRow = self.getAimRow()
            if aimRow is not None:
                aim = str(aimRow["kid"])
                title = aimRow["title"]
                account = aimRow["account"]
                summary = aimRow["summary"]
                detail = aimRow["detail"]
            html = html.replace("ilv_submit","IlvForm.edit")
        else:
            html = html.replace("ilv_submit","IlvForm.join")
        html = html.replace("ilv_act",act)
        html = html.replace("ilv_sup",sup)
        html = html.replace("ilv_aim",aim)
        html = html.replace("ilv_title",title)
        html = html.replace("ilv_account",account)
        html = html.replace("ilv_ip",ip)
        if summary is None:
            summary = ""
        html = html.replace("ilv_summary",summary)
        if detail is None:
            detail = ""
        html = html.replace("ilv_detail",detail)
        html = html.replace("ilv_datetime",datetime)
        html = html.replace("ilv_millisecond",millisecond)
        # 2 读取表单数据
        if self.postDict and "title" in self.postDict and self.postDict["title"]:
            keys = self.postDict.keys()
            values = self.postDict.values()
            sql = ""
            sql += " select * from %s" % self.dtColumn
            sql += " where `kid`='%s'" % self.postDict[self.dtColumn][0]["value"]
            sql += " limit 1"
            html += sql + "<br>"
            md = ilv.MyData.MyData()
            supRow = md.getRow(self.dtColumn,self.postDict[self.dtColumn][0]["value"])
            dtname = self.getSupValue(sup=sup,name="dtname")
            sql = None
            # 2.1 add record
            if self.urlDict and "act" in self.urlDict and self.urlDict["act"]=="add":
                sql = ""
                sql += " insert into `%s`" % dtname
                sql += " ("
                idx = 0
                for key in keys:
                    idx += 1
                    if idx == 1:
                        sql += "`%s`" % key
                    else:
                        sql += ",`%s`" % key
                sql += " )"
                sql += "values("
                idx = 0
                for value in values:
                    idx += 1
                    if idx == 1:
                        sql += "'%s'" % value[0]["value"]
                    else:
                        sql += ",'%s'" % value[0]["value"]
                sql += " )"
            # 2.2 edit record
            if self.urlDict and "act" in self.urlDict and self.urlDict["act"]=="edit":
                sql = ""
                sql += " update `%s`" % dtname
                idx = 0
                for key in self.postDict:
                    idx += 1
                    if idx==1:
                        sql += " set `%s`='%s'" % (key,self.postDict[key][0]["value"]) 
                    else:
                        sql += ",`%s`='%s'" % (key,self.postDict[key][0]["value"])
                sql += " where `kid`='%s'" % aimRow["kid"]
                sql += " limit 1"
            # 2.3 write data
            if sql is not None:
                html += sql + "<br>"
                md.execute(sql)
            md.close()
        return html
        pass

