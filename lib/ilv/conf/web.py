#!/usr/bin/env python3
#-*-code:utf8-*-

'''
Config 基本配置文件
'''

########################################################################
# ilv.conf.web.Web
# 网页配置类
########################################################################
class Web:
    #*******************************************************************
    # 一基本属性
    #*******************************************************************
    # 1 网页基本参数
    # =============
    action = "/py" # 行为
    title = "ilv_web" # 网页基本标题
    br = "<br>\r\n" # a ling mark
    bn = "\r\n"
    pattern = "" # 模式
    
    # 1.1 静态文件位置
    # ----------------
    dir_static = "static/" # 静态文件地址

    # 1.2 终端平台
    # ------------
    plat = "core" # 核心平台
    # plat = "pc" # 电脑终端
    # plat = "cell" # 手机终端
    # plat = "pad" # 平板终端    
    
    # 1.3 用户模式 用于之后拓展
    # -------------------------
    mode = "default" # 默认模式
    # mode = "night" # 夜间模式
    # mode = "day" # 白天模式
    
    # 1.4 出错文件
    error_htm = "static/error/error.html"

    # 2 数据库基本参数
    # ================
    # 2.1 SQLite配置
    # --------------
    dbType = "sqlite" # 基础数据库使用SQLite
    dbHost = "" #也可以为：127.0.0.1
    dbUsr = "" # 数据库登录用户
    dbPsw = "" # 数据库登录密码
    dbName = "data/sqlite/ilv_db" # 操作数据库
    
    # 2.2 MySQL配置
    # -------------
    # dbType = "mysql" # 基础数据库使用SQLite
    # dbHost = "localhost" #也可以为：127.0.0.1
    # dbUsr = "root" # 数据库登录用户
    # dbPsw = "" # 数据库登录密码
    # dbName = "ilv_db" # 操作数据库
    

    # 3 数据表基本参数
    # ===============
    DT_TABLES = ["item","news","user","active"]
    dtNews = "news" # 新闻表
    dtColumn = "item" # 栏目数据表
    dtUser = "user" # 会员数据表
    dtModule = "module" # 模块数据表
    dtActive = "active" # 会员活动表
    db = None # 数据库
    
    # 4 版本信息
    # =========
    revision = "0.1.20140414"
    
    # 5 defaults
    # ==========
    USER_SUP = "1013" # the kid of user in column
    COLUMN_SUP = "1014" # the kid of column in column
    ACTIVE_SUP = "1015" # the column for user to login and logout
    NEWS_SUP = "10"
    
    # 地址栏中各个参数的名称
    # =====================
    SUP_NAME = "sup"
    AIM_NAME = "aim"
    USER_NAME = "u"
    
    # 6 file paths
    # ============
    LOG_DIR = "module/templet/"
    LOG_MSG = "module/templet/msg.html"
    LOG_UWSGI = "module/templet/uwsgi.html"
    
    # 7 environment
    # =============
    env = None # 环境变量，从网站请求获取相关参数
    opfile = None # 文件操作变量
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass
