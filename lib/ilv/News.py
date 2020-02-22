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
# News 新闻
# 浏览 显示 注册 删除 编辑 查找 统计 登录 注销
####################################################################################################
class News(ilv.Base.Base):
    ################################################################################################
    # 一、基本属性
    ################################################################################################
    pass # 基本属性
    ################################################################################################
    # 二、预设方法
    # 1 构造方法
    # 2 getColumnNode 获得栏目的网页结点
    # 3 getUrl 逐级向上寻找模块文件位置
    ################################################################################################
    ############################################################################################
    # 1 构造方法
    ############################################################################################
    def __init__(self,env=None):
        ilv.Base.Base.__init__(self,env=env)
    ################################################################################################
    # 3 主线方法 getHtml 获得网页，这是唯一的接口
    ################################################################################################
    pass # getHtml
    ################################################################################################
    # 四、辅助方法
    # 1 getHead 获得网页头
    # 2 getMenu 获得网页菜单
    # 3 getBody 获得网页主体
    # 4 getTail 获得网页尾
    ################################################################################################
    ############################################################################################
    # 1 getHead 获得网页头
    ############################################################################################
    pass # getHead
    ########################################################################################
    # 3.1 getAction 基本操作
    ########################################################################################
    pass # getAction
    ####################################################################################
    # 3.1.2 show 显示新闻
    ####################################################################################
    def show(self):
        html = ""
        sup = self.urlDict["sup"]
        aim = self.urlDict["aim"]
        md = ilv.MyData.MyData()
        supRow = md.getRow(self.dtColumn,sup)
        aimRow = md.getRow(supRow["dtname"],aim)
        md.close()
        html += '''
        <div id=divShow><!--显示文章-->
        '''
        if aimRow["title"]:
            html += '''
              <hr>
              <div id=divShowTitle>%s</div><!--标题-->   
            ''' % aimRow["title"]
        if aimRow["summary"]:
            html += '''
              <div id=divShowSummary><!--摘要-->
                <strong>&nbsp;&nbsp;&nbsp;&nbsp;内容提要：</strong>
                %s
              </div><!--/摘要-->
              <hr>
            ''' % aimRow["summary"]
        if aimRow["image"]:
            html += '''
              <div id=divShowImage><img width=800 src=%s /></div><!--图片-->
            ''' % aimRow["image"]
        if aimRow["video"]:
            html += '''
              <div id=divShowVideo><!--视频-->
              <script type=text/javascript src=js/AEV/AEV.js></script>
              <script type=text/javascript>
                  <!--
                  AEV.show(swfDir="js/AEV/Flvplayer.swf",pyDir="../../",flvDir="%s",width="660",height="530");
                  //-->
              </script>
              </div><!--／视频-->
            ''' % aimRow["video"]
        if aimRow["detail"]:
            html += '''
              <div id=divShowDetail><!--详情-->
                  %s
              </div><!--/详情-->
            ''' % aimRow["detail"]
        if aimRow["attach"]:
            html += '''
              <div id=divShowAttach><a href=%s target=_blank>下载附件</a></div><!--附件-->
            ''' % aimRow["attach"]
        html += '''
        </div><!--/显示文章-->
        '''
        return html
        pass
    ####################################################################################
    # 3.1.4 delete 删除会员
    ####################################################################################
    def delete(self):
        html = ""
        html += '''
        <div id=divDelete><!--删除-->
        '''
        htmlError = ""
        if "sup" in self.urlDict and self.urlDict["aim"]:
            sup = self.urlDict["sup"]
        else:
            return "<font color=red>操作错误：删除栏目未指定</font>"
        if "aim" in self.urlDict and self.urlDict["aim"]:
            aim = self.urlDict["aim"]
        else:
            return "<font color=red>操作错误：删除目标未指定</font>"
        md = ilv.MyData.MyData()
        supRow = md.getRow(self.dtColumn,sup)
        md.close()
        if not supRow:
            return "<font color=red>操作错误：删除栏目不正确sup=%s</font>" % sup
        md = ilv.MyData.MyData()
        aimRow = md.getRow(supRow["dtname"],aim)
        md.close()
        if not aimRow:
            return "<font color=red>操作错误：删除目标不正确aim=%s</font>" % aim
        
        html += '''
        确定要删除：<font color=red>%s</font>
        ''' % aimRow["title"]
        html += '''
        <form method=post action=%s?sup=%s&act=%s&aim=%s enctype=multipart/form-data>
            <input type=submit value=确定 />&nbsp;&nbsp;
            <input type=hidden name=run value=yes />
        </form>
        ''' % (fd.action,fd.sup,fd.act,fd.aim)
        html += '''
        <a htef=%s?sup=%s>返回主页</a>
        ''' % (fd.action,fd.sup)
        # 删除记录
        if "run" in fd and fd["run"] == "yes":
            md = ilv.MyData.MyData()
            sql = "delete from `%s` where `kid`='%s' LIMIT 1" % (fd["supName"],fd["aim"])
            md.execute(sql)
            md.close()
            return "删除%s成功" % fd["aimTitle"]
        html += '''
        </div><!--/删除-->
        '''
        return html
        pass
    ####################################################################################
    # 3.1.6 search 查找会员
    ####################################################################################
    def search(self):
        html = ""
        return html
        pass
    ####################################################################################
    # 3.1.7 count 统计会员
    ####################################################################################
    def count(self):
        html = ""
        return html
        pass
    ####################################################################################
    # 3.1.8 login 登录会员
    ####################################################################################
    def login(self):
        html = ""
        return html
        pass
    ####################################################################################
    # 3.1.9 logout 注销会员
    ####################################################################################
    def logout(self):
        html = ""
        return html
        pass
    ############################################################################################
    # 2.3.2 getTotal  获得总览层 闪动照片 最近更新
    ############################################################################################
    pass # getTotal
    ############################################################################################
    # 4 getTail 获得网页尾
    ############################################################################################
    pass # getTail




