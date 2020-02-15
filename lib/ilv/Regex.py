#!/usr/bin/env python3
#-*-code:utf8-*-

'''
Regular expression operations
正则表达式操作
1 替换 re.sub(pattern,repl,string,count=0,flags=0) 正则表达式 替代值 源
repl可以换成函数,也可以是字符串
'''
import re # 必须引用正则表达式的包

###################################################################################################
# Regex 正则表达式
###################################################################################################
class Regex:
    br = "<br>\r\n"
    ##################################################
    # init 构造函数
    ##################################################
    def __init__(self):
        pass
    ##################################################
    # demo 演示
    # 1 toSave 将数据去掉IP和单引号
    ##################################################
    def getDemo(self):
        html = ""
        # 1 去除IP
        html += "1 去除字符串中的IP"+self.br
        src = "src=http://24.71.66.75/upload/test.jpg"+self.br
        src += "src=HTTP://24.71.66.75/upload/test.jpg"+self.br
        src += src+src+src+src
        html += "输入值："+src+self.br
        html += "正则表达式：" + r"(src=http://[\w\d\._]+/)"+self.br
        html += "返回值："+self.toData(src)+self.br
        return html
        pass
    ##################################################
    # 1 toData()
    # 1 delIp(html) 去除字符串中的IP
    # 2 更换所有单引号，更换成两个汉字单引号’1’
    # 3 更换英文右侧单引号为两个中文单引号’2’
    # html = "src=http://24.71.66.75/upload/test.jpg "
    # return "src=upload/test.jpg"
    ##################################################
    def toData(self,html=''):
        dataStr = html
        # 1 去除IP
        pattern = r"src=http://[\w\d\._]+/"
        flags=re.IGNORECASE
        dataStr = re.sub(pattern,self.ipRepl,dataStr,flags=flags)
        # 2 更换英文左上角单引号为两个中文单引号’1’
        pattern = r"`"
        dataStr = re.sub(pattern,'’1’',dataStr)
        # 3 更换英文右侧单引号为两个中文单引号’2’
        pattern = r"'"
        dataStr = re.sub(pattern,'’2’',dataStr)
        return dataStr
        pass
    ##################################################
    # 2 toHtml()
    # 1 恢复所有’1’为左上角单引号
    # 2 恢复所有’2’为右侧单引号
    ##################################################
    def toHtml(self,dataStr=''):
        html = dataStr
        # 1 恢复所有’1’为左上角单引号
        html = re.sub(r"’1’","`",html)
        # 2 恢复所有’2’为右侧单引号
        html = re.sub(r"’2’","'",html)
    ##################################################
    # 1.1 ipRepl(m) re.sub的替换函数，可以直接用字符串
    ##################################################
    def ipRepl(self,m): # m是比较后的数组可以引用m.group(0)
        return "src="
        pass
        














