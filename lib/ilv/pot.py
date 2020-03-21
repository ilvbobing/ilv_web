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

import ilv.core.web
import ilv.cell.web
import ilv.pad.web
import ilv.pc.web

########################################################################
# ilv.plat.get_web
########################################################################
def get_web(env=None):
    # 根据用户指定模式确定前台模式
    # =============================
    urlDict = env.getUrlDict()
    agent = env.get_agent()
    base = None
    if "plat" in urlDict:
        print("index.py,在地址栏中plat="+urlDict["plat"]+"\r\n<br>")
        # 2.1 电脑端模式
        # --------------
        if urlDict["plat"]=="pc":
            base = ilv.pc.web.Web(env=env)
        # 2.2 平板模式
        # ------------
        elif urlDict["plat"]=="pad":
            base = ilv.pad.web.Web(env=env)
        # 2.3 手机模式
        # ------------
        elif urlDict["plat"]=="cell":
            base = ilv.cell.web.Web(env=env)
        # 2.4 默认的文本模式
        else:
            base = ilv.core.web.Web(env=env)
        
    # 3 根据客户端实际情况确定前台模式
    else:
        # 3.1 如果有Windows或Linux，则为电脑端
        # -----------------------------------
        if "Mobile" in agent:
            base = ilv.cell.web.Web(env=env)
        # 3.2 如果有Mobile，则为手机端
        elif "Android" in agent:
            base = ilv.pad.web.Web(env=env)
        # 3.3 如果有Android，且没有Mobile，则为平板
        # ----------------------------------------
        elif "Windows" in agent or "Linux" in agent:
            base = ilv.pc.web.Web(env=env)
        # 3.4 其他情况显示默认的文本模式
        # -----------------------------
        else:
            base = ilv.core.web.Web(env=env)
    return base
    pass



























 




   
