#!/usr/bin/env python3
#-*-code:utf8-*-

'''
Demo 演示台
1 演示上传表单
'''
import os
####################################################################################################
# Demo 演示类
####################################################################################################
class Demo:
    ################################################################################################
    # 一基本属性
    ################################################################################################
    action = "/py" # 行为
    urlDict = None # 地址参数
    env = None # 环境
    ################################################################################################
    # 1 构造函数--二 配置函数
    ################################################################################################
    def __init__(self,env=None):
        self.env = env
        if env:
            self.urlDict = env.getUrlDict()
        pass
    ################################################################################################
    # 1 getHtml 获得网页数据--三 主线函数
    ################################################################################################
    def getHtml(self):
        html = ""
        html += self.getHead()
        html += self.getBody()
        html += self.getTail()
        return html
        pass
    ##################################################
    # 1.1 getHead 网页头
    ##################################################
    def getHead(self):
        html = ""
        html += """
        <html>
        <head>
        <meta charset=utf-8 />
        <title>模块演示</title>
        <link type=text/css href=module/css/demo.css rel=stylesheet />
        </head>
        <body>
        <div id=divPaddingTop>&nbsp;</div><!--最上层留白-->
        <center><div id=div_body><!--最外层边框-->
        """
        return html
        pass
    ##################################################
    # 1.2 getBody 网页主体
    ##################################################
    def getBody(self):
        html = ""
        html += '''
        <div id=divBody><!--网页主体-->
            %s
            %s
        </div><!--/网页主体-->
        ''' % (self.getMenu(),self.getDemo())
        return html
    ##################################################
    # 1.2.1 getMenu 演示菜单
    ##################################################
    def getMenu(self):
        html = ""
        html += '''
        <div id=divMenu>菜单
            <div class=menuRow><a href=%s?demo=form>演示表单提交</a></div>
            <div class=menuRow><a href=%s?demo=regex>演示正则表达式</a></div>
            <div class=menuRow><a href=%s?demo=cookie>演示Cookie</a></div>
        </div>
        ''' % (self.action,self.action,self.action)
        return html
        pass
    ##################################################
    # 1.2.2 getDemo 演示内容
    ##################################################
    def getDemo(self):
        html = ""
        html += '''
        <div id=divDemo><!--演示内容-->
        '''
        if self.urlDict is None or "demo" not in self.urlDict:
            return html
            pass
        if self.urlDict["demo"]=="form":
            if self.env:
                html += '''
                %s
                ''' % self.env.getDemo()
        elif self.urlDict["demo"]=="regex":
            regex = ilv.Regex.Regex()
            html += '''
            %s
            ''' % regex.getDemo()
        elif self.urlDict["demo"]=="cookie":
            html += '''
            os.environ=%s<br>
            os.environ["HTTP_COOKIE"]=<br>
            ''' % (os.environ)
        html += '''
        </div><!--/演示内容-->
        '''
        return html
        pass
    ##################################################
    # 1.3 getTail 网页结尾
    ##################################################
    def getTail(self):
        html = ""
        html += """
        </div></center><!--/最外层边框-->
        <div style=height:5px;>&nbsp;</div>
        </body>
        </html>
        """
        return html
        pass
    pass
