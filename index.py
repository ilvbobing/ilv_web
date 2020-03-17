#!/usr/local/bin/python3
#-*-code:utf8-*-

########################################################################
# 设置类库路径
########################################################################
import sys
path ='/home/ilvbobing/ilv_web/lib'
if path not in sys.path:
    sys.path.append(path)

########################################################################
# Note:
# Please build an .pth file in site-packages directory and add path of /www/ilvLib
# For example,I installed python-3.3.1,the .pth file would be build in 
# /usr/local/lib/python3.3/site-packages
# I have build a file named ilvbobing.pth in /usr/local/lib/python3.3/site-packages
# And the content of ilvbobing.pth maybe: /www/ilvLib
########################################################################
import ilv.core.web
import ilv.cell.web
import ilv.pad.web
import ilv.pc.web
import ilv.Demo # 演示类
import ilv.core.env # 环境类，必须引用，保持数据一致，因为getFormDict只能引用一次，之后就无效了。
########################################################################
# The entrance of uWSGI
########################################################################
def  application(environ,start_response):
    ####################################################################
    # 基本参数
    ####################################################################
    # 1 创建环境变量
    # =============
    env = ilv.core.env.Env(environ=environ)
    urlDict = env.getUrlDict()
    agent = env.get_agent()
    
    # 2 根据用户指定模式确定前台模式
    # =============================
    base = None
    if "plat" in urlDict:
        print("index.py,在地址栏中plat="+urlDict["plat"]+"\r\n<br>")
        # 2.1 电脑端模式
        # --------------
        if urlDict["plat"]=="pc":
            base = ilv.pc.web.Web(env=env)
            base.plat = "pc"
        # 2.2 平板模式
        # ------------
        elif urlDict["plat"]=="pad":
            base = ilv.pad.web.Web(env=env)
            base.plat = "pad"
        # 2.3 手机模式
        # ------------
        elif urlDict["plat"]=="cell":
            base = ilv.cell.web.Web(env=env)
            base.plat = "cell"
        # 2.4 默认的文本模式
        else:
            base = ilv.core.web.Web(env=env)
            base.plat = "core"
        
    # 3 根据客户端实际情况确定前台模式
    else:
        # 3.1 如果有Windows或Linux，则为电脑端
        # -----------------------------------
        if "Windows" in agent or "Linux" in agent:
            base = ilv.pc.web.Web(env=env)
            base.plat = "pc"
        # 3.2 如果有Mobile，则为手机端
        elif "Mobile" in agent:
            base = ilv.cell.web.Web(env=env)
            base.plat = "cell"
        # 3.3 如果有Android，且没有Mobile，则为平板
        # ----------------------------------------
        elif "Android" in agent:
            base = ilv.pad.web.Web(env=env)
            base.plat = "pad"
        # 3.4 其他情况显示默认的文本模式
        # -----------------------------
        else:
            base = ilv.core.web.Web(env=env)
            base.plat = "core"
    
    ####################################################################
    # 根据参数集设置网页需要展示的效果
    ####################################################################
    if "AEE_uploadFinally" in urlDict: # 实现AEE插件上传功能
        response_body = "OK"
    else:
        response_body = base.getHtml()
        # response_body = str(environ["wsgi.input"])
        #response_body = str(environ)
    if urlDict is not None and "demo" in urlDict:
        demo = ilv.Demo.Demo(env=env)
        response_body = demo.getHtml()
        pass
    status = "200 OK"
    bHtml = b"" + response_body.encode(encoding="utf-8")
    response_headers = [("Content-Type","text/html"),("Content-Length",str(len(bHtml))),("charset","utf-8"),("Set-Cookie","session=12345")]
    start_response(status,response_headers)
    return bHtml


