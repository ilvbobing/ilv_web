#!/usr/local/bin/python3
#-*-code:utf8-*-

"""
Sumary:
This is a function for control the plat of web.
Params           Type                  Explain
env              Env                   The envirent of the client
摘要：
这是一个控制网页平台的方法
"""

import ilv.core.web
import ilv.cell.web
import ilv.pad.web
import ilv.pc.web

########################################################################
# ilv.plat.get_web
########################################################################
def get_web(env=None):

    # 1. 固定平台：开发者模式
    # ======================
    # base = ilv.core.web.Web(env=env)
    # return base
    # pass
    
    # 2. 根据用户指定模式确定前台模式
    # =============================
    urlDict = env.getUrlDict()
    agent = env.get_agent()
    base = None
    if "plat" in urlDict:
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
    # ===============================
    else:
        # 3.1 如果有Windows或Ubuntu，则为电脑端
        # -----------------------------------
        if "Windows" in agent or "Ubuntu" in agent:
            base = ilv.pc.web.Web(env=env)
        # 3.2 如果有Mobile，则为手机端
        elif "Mobile" in agent or "Safari" in agent:
            base = ilv.cell.web.Web(env=env)
        # 3.3 如果有Android，且没有Mobile，则为平板
        # ----------------------------------------
        elif "Android" in agent:
            base = ilv.pad.web.Web(env=env)
        # 3.4 其他情况显示默认的文本模式
        # -----------------------------
        else:
            base = ilv.core.web.Web(env=env)
    return base
    pass



























 




   
