######!/usr/local/bin/python3
#!/usr/bin/env python3
#-*-code:utf8-*-

"""
1.This is a base class of html.
2.When import this class we can get a default html.
3.The other class (for exampe Microblog) is the child of MyBase
"""
# python library
import os,datetime,struct,stat
import ilv.Time
import ilv.core.db
import ilv.conf.web
import ilv.core.opfile

########################################################################
# ilv.core.web.Web 基础网页 是页面拓展的基础类
# 主要分以下几层：
# 一、操作层：control 浏览 添加 删除 编辑 查找 统计 登陆 注消
# 二、总览层：total 闪动照片 最近更新
# (一)闪动照片 getShine (二)最近更新 getRecent
# 三、分栏层：subfield 分栏显示
# 四、列表层：list 列表显示
########################################################################
class Web(ilv.conf.web.Web):
    ######################################################################
    # 一 基本属性
    ######################################################################
    urlDict = {} # 地址栏参数字典
    postDict = {} # 表单参数字典
    msg = "" # process message,usually is error
    PARAS = {} # 基本参数集，用于存放常用参数

    #######################################################################
    # II pre method
    # 1 construct method
    # 2 get_url find the url from sup until finded
    # 3 getTemplet get the html of templet
    ######################################################################
    ################################################################
    # 1 constructor 构造函数
    ################################################################
    def __init__(self,env):
        """__init__ construct the class
        
        """
        # init paras
        self.plat = "core"
        self.urlDict = env.getUrlDict() # 获取网页地址栏参数
        self.postDict = env.getFormDicts() # 获取网页表单参数
        self.env = env # 获取网页请求环境变量
        
        # 4 初始化参数集
        self.init_paras()
        self.db = ilv.core.db.DB(self.dbType, self.dbHost, self.dbUsr, self.dbPsw, self.dbName) # 默认使用SQLite数据库
        
        # init log file
        log_dir = self.LOG_DIR # 从Config继承：module/templet/
        log_msg = self.LOG_MSG # 从Config继承：module/templet/msg.html
        log_uwsgi = self.LOG_UWSGI # 从Config继承：module/templet/uwsgi.html
        # 此项未执行
        if False and len(self.urlDict)==0:
            if os.path.exists(log_msg): # 删除已存在的msg.html
                os.remove(log_msg) # deletelog
            self.add_msg("<!--ilv_msg-->")
            self.add_msg("MSG:")
            self.add_msg("MSG:")
            if os.path.exists(log_uwsgi):
                os.remove(log_uwsgi)
            self.add_msg("<!--ilv_uwsgi-->",log_uwsgi)
            self.add_msg("UWSGI:",log_uwsgi)
            self.add_msg("UWSGI:",log_uwsgi)
        else:
            mode = stat.S_IRWXO|stat.S_IRWXG|stat.S_IRWXU
            if os.path.exists(log_dir):
                os.chmod(log_dir,mode)
            if os.path.exists(log_msg):
                os.chmod(log_msg,mode)
            if os.path.exists(log_uwsgi):
                os.chmod(log_uwsgi,mode)
        # useful row
        self.PARAS["sup_row"] = self.get_sup_row()
        self.PARAS["aim_row"] = self.get_aim_row()
        self.PARAS["user_row"] = self.get_user_row()
        
        # set opfile
        mode = self.PARAS["sup_row"]["module"]
        self.opfile = ilv.core.opfile.Opfile(dir_static=self.dir_static, plat=self.plat, mode=mode) # 初始化文件操作变量
        
        pass
    ################################################################
    # 2 init_paras
    ################################################################
    def init_paras(self):
        t = ilv.Time.Time()
        paras = self.PARAS
        # useful paras
        paras["act"] = "view" # 浏览模式
        paras["aim"] = "1" # the default aim of news
        paras["aim_row"] = None
        paras["datetime"] = t.getDatetime()
        paras["hire"] = "1"
        paras["ip"] = self.env.getClient()
        paras["millisecond"] = t.getMillisecond()
        paras["page"] = "1"
        paras["p"] = "simple" # mode:simple admin
        paras["sup"] = "10"
        paras["sup_row"] = None
        paras["u"] = "1" # user of client
        paras["user_row"] = None
    ################################################################
    # 3 get_para
    ################################################################
    def get_para(self,name=None,row=None):
        para = None
        if row is None:
            row = {}
        if name is None:
            return None
        if name in row and row[name]:
            para = row[name]
        elif name in self.urlDict and self.urlDict[name]:
            para = self.urlDict[name]
        elif name in self.PARAS and self.PARAS[name]:
            para = self.PARAS[name]
        else:
            if row is not None:
                para = ""
            else:
                self.add_msg("Base.get_para:para=None,name=%s" % str(name))
        return para
    ####################################################################
    # 4 getActon get the website url of http
    ####################################################################
    def get_action(self,paras=None):
        action = "http://"
        action += self.env.getHost()
        action += self.action
        action += "?"
        if paras is None:
            paras = {}
        # simple act aim hire pattern page sup user
        names = ["act","aim","hire","p","page","sup","u","plat"]
        for name in names:
            if name in paras:
                action += "&%s=%s" % (name,str(paras[name]))
            else:
                para = self.get_para(name)
                if para is not None and str(para)!="":
                    action += "&%s=%s" % (name,para)
        return action
        pass
    ################################################################
    # 5 get_module_row
    ################################################################
    def get_module_row(self,name=None,sup=None):
        row = None
        if sup is None:
            sup = self.get_para(name="sup")
        if name is None:
            name = "module"
        idx = 0
        while idx<=10: # recycle only 10 times
            idx += 1
            self.db.run()
            sup_row = self.db.get_row(dtname=self.dtColumn, kid=sup)
            self.db.close()

            if sup_row is None:
                sup = self.PARAS["sup"]
                continue
            if name in sup_row:
                # name is a column of the datatable
                module = sup_row[name]
                if module is not None:
                    row = sup_row
                    break
                else:
                    sup = sup_row[self.dtColumn]
            else:
                self.add_msg("Base.get_module_row(:%s is not in %s" \
                             % (name,sup_row))
                break
        if idx==11:
            self.add_msg("Base.get_module_row:idx=11,name=%s,sup=%s"\
                         % (str(name),str(sup)))
        return row
    ################################################################
    # 6 get_row example:102222 1014 sup
    ################################################################
    def get_row(self,aim=None,sup=None,name=None):
        row = None
        dtname = None
        kid = aim
        dtname_row = self.get_module_row(name="dtname",sup=sup)
        if dtname_row is not None:
            dtname = dtname_row["dtname"] # column
            # 1 default row
            self.db.run()
            row = self.db.get_row(dtname,self.PARAS[name])
            self.db.close()
            if kid is None:
                kid = self.get_para(name)
            if kid==self.PARAS[name]:
                # kid is the default
                pass
            else:
                # self.urlDic[name]!=self.PARAS[name]
                self.db.run()
                aim_row = self.db.get_row(dtname,kid) # None
                self.db.close()
                if aim_row is not None:
                    row = aim_row
                else:
                    self.add_msg("Base.get_row(aim=%s,sup=%s,name=%s):\
                        aim_row is None." % (str(aim),str(sup),str(name)))
        else:
            self.add_msg("Base.get_row(aim=%s,sup=%s,name=%s):\
                dtname_row is None" % (str(aim),str(sup),str(name)))
        # change the right aim in url
        if aim is None and row is not None and name is not None:
            self.urlDict[name] = str(row["kid"])
        return row
    def get_sup_row(self,sup=None):
        return self.get_row(aim=sup,sup=self.COLUMN_SUP,name="sup")
    def get_aim_row(self,aim=None,sup=None):
        return self.get_row(aim=aim,sup=sup,name="aim")

    ################################################################
    # 9 add_msg
    ################################################################
    def add_msg(self,msg=None,path=None):
        # 1 open the log file
        log_dir = self.LOG_DIR
        if path is None:
            log_msg = self.LOG_MSG
        else:
            log_msg = path
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        if not os.path.exists(log_msg):
            output = open(log_msg,mode="w")
        else:
            output = open(log_msg,mode="a")
        if msg:
            output.write(str(msg)+self.bn)
        output.close()
        return str(msg)
        
    ################################################################
    # 10 get_user_row
    ################################################################
    def get_user_row1(self,user=None):    
        row = None
        u = user
        if u is None:
            u = self.get_para("u")
        self.db.run()
        row = self.db.get_row(dtname=self.dtUser,kid=u)
        # 如果没有取出，则显示出错信息。
        if row is None:
            self.add_msg("Base.get_user_row(user=%s):row=%s" % (str(u),str(row)))
        self.db.close()
        return row
    ################################################################
    # 10 get_user_row
    ################################################################
    def get_user_row(self,user=None):
        row = None
        u = user
        #self.add_msg("Base.get_user_row:user=%s" % str(user))
        if u is None:
            u = self.get_para("u")
        # 1 set default row
        # 三个参数：1, 1013,u
        row = self.get_row(self.PARAS["u"],self.USER_SUP,"u")    
        user_row = self.get_row(u,self.USER_SUP,"u")
        if user_row is not None:
            u = str(user_row["kid"])
            if str(u)==str(self.PARAS["u"]):
                # user is default
                pass
            elif "account" in user_row:
                # check if user is loginned
                account = user_row["account"]
                ip = self.env.getClient()
                sql = ""
                sql += " select * from `%s`" % self.dtActive
                sql += " where `account`='%s'" % account
                sql += " and `ip`='%s'" % ip
                sql += " order by `datetime` desc"
                sql += " limit 1"
                self.db.run()
                self.db.execute_query(sql)
                rows = self.db.get_row_dicts()
                self.db.close() 
                if len(rows)>0:
                    # user have loginned some time ago
                    row = rows[0]
                    t = ilv.Time.Time()
                    start = t.datetime(str(row["datetime"]))
                    td = t.timedelta(str(row["timedelta"]))
                    end = start+td
                    now = t.datetime()
                    if end>=now and row["hire"]>-2:
                        # user is loginning and not logout                
                        row = user_row
                    else:
                        self.add_msg("Base.get_user_row(user=%s):\
                            end<now or row[hire]<=-2" % str(u))
                else:
                    self.add_msg("Base.get_user_row(user=%s):\
                        len(rows)=0" % str(u))
            else:
                self.add_msg("Base.get_user_row(user=%s):account is not\
                    in user_row." % str(u))
        else:
            self.add_msg("Base.get_user_row(user=%s):user_row is None"\
                % str(u))
        # change the right user in url
        if user is None and row is not None:
            self.urlDict["u"] = str(row["kid"])
        return row
    ################################################################
    # 11 goto jump to the action url of http
    ################################################################
    def goto(self,action=None):
        html = ""
        html = self.opfile.get_templet("goto")
        if action is None:
            action = self.get_action()
        html = html.replace("ilv_url",action)
        return html
    ################################################################
    # 12 get_sup_node
    ################################################################
    def get_sup_node(self,sup=None,pre1="",pre2=""):
        html = ""
        # 1 加入组合框头
        if pre1=="" and pre2=="": # 一级标题
            html += '''
            <select name=item><!--栏目组合框-->            
            '''
        if sup is None:
            sup = self.get_para("sup")
        sup_row =self.get_row(aim=sup,sup=self.COLUMN_SUP,name="sup")
        if sup_row is not None:
            # 2 搜集子栏目
            sql = ""
            sql += " select * from `item`"
            sql += " where `item`='%s'" % sup
            sql += " and `level`='1'"
            sql += " order by `sid` asc"
            self.db.run()
            self.db.execute_query(sql)
            rows = self.db.get_row_dicts()
            self.db.close()
            # 3 判断当前选项是否被选择
            selectedStr = ""
            if str(sup)==str(self.get_para("sup")):
                selectedStr = "selected"
            # 4 加入当前结点
            if len(rows)>0:
                html += '''
                <option value=%s %s>%s◇%s
                ''' % (sup,selectedStr,pre1+pre2,sup_row["title"])
            else:
                html += '''
                <option value=%s %s>%s◆%s
                ''' % (sup,selectedStr,pre1+pre2,sup_row["title"])        
            # 5 设置子结点
            rowLen = len(rows)
            rowIdx = 0
            subpre1 = ""
            subpre2 = ""
            for row in rows:
                rowIdx += 1
                # 5.1 竖线前缀
                if pre1=="" and pre2=="": # 一级标题
                    subpre1 = ""
                elif pre2=="├": # 其它标题 父亲为中间结点
                    subpre1 = pre1 + "│"
                else: # 其它标题 父亲为末尾结点
                    subpre1 = pre1 + "　" # "┆"
                # 5.2 分支前缀
                if rowIdx<rowLen:
                    subpre2 = "├"
                else:
                    subpre2 = "└"                    
                html += self.get_sup_node(row["kid"],subpre1,subpre2)
        else:
            self.add_msg("Base.get_sup_node:sup_row=None,sup=%s,\
                         pre1=%s,pre2=%s." % (str(sup),pre1,pre2))
        if pre1=="" and pre2=="":
            html += '''
            </select><!--/栏目组合框-->
            '''
        return html
    ####################################################################
    # III major method
    ####################################################################
    ####################################################################
    # 1 getHtml 网页数据
    ####################################################################
    def getHtml(self):
        html = ""
        html += self.get_head_htm() 
        #html += self.get_search_htm()
        html += self.get_menu_htm()        
        html += self.getBody()        
        html += self.getTail()
        return html

    ####################################################################
    # IV help method
    ####################################################################
    ####################################################################
    # 1 getHead get html head
    ####################################################################
    def get_head_htm(self):
        html = None
        # 1 set sup user
        sup_row = self.get_para("sup_row")
        user_row = self.get_para("user_row")
        # 2 set title 需要拓展
        title = sup_row["title"] + "--" + self.title + " " + self.revision
        agent = self.env.get_agent();
        # 4 read templet
        html = self.opfile.get_templet("head")
        html = html.replace("ilv_title",title)
        html = html.replace("ilv_user",user_row["account"])
        html = html.replace("HTTP_USER_AGENT", agent)
        # 5 set control
        html = html.replace("ilv_control",self.get_control_htm())
        return html 
      
    ####################################################################
    # 1.1 get_control_htm
    ####################################################################
    def get_control_htm(self):
        html = "ilv.plat.base.Base.get_control_htm<br>"
        return html

    ####################################################################
    # 2 get_menu_htm 获得网页菜单
    ####################################################################
    def get_menu_htm(self):
        html = ""
        sup_row = self.get_para("sup_row")
        sup = str(sup_row["kid"])
        # 查阅当前的所有子类
        sql = ""
        sql += " select * from `item`"
        sql += " where `item`='%s'" % sup
        user_row = self.get_user_row()
        # 限制只有admin 可以查看所有栏目
        if user_row["account"]!="admin":
            sql += " and `level`='1'"
        sql += " order by `sid` asc"
        self.db.run()
        self.db.execute_query(sql)
        subRows = self.db.get_row_dicts()
        self.db.close()
        paras = {}
        paras["sup"] = 10
        paras["act"] = "view"
        action = self.get_action(paras)
        # 制作链接，去除脚本
        menu_links = "&nbsp;"
        menu_links += "<a href=%s target=_blank>网站首页</a>&nbsp;" % action
        # 向上找一级
        if sup!="10":
            paras["sup"] = sup
            action = self.get_action(paras)
            title = sup_row["title"]
            menu_links += "<a href=%s target=_blank>%s</a>&nbsp;" % (action,title)
        for subRow in subRows:
            paras["sup"] = subRow["kid"]
            action = self.get_action(paras)
            title = subRow["title"]
            menu_links += "<a href=%s target=_blank>%s</a>&nbsp;" % (action,title)
        html = self.opfile.get_templet("menu")
        html = html.replace("ilv_menu_links",menu_links)
        # set the first news 头条新闻
        sql = ""
        sql += " select * from `%s`" % self.dtNews
        sql += " where `hire`>=3"
        sql += " order by `datetime` desc"
        sql += " limit 1"
        self.db.run()
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        self.db.close()
        if len(rows)>0:
            row = rows[0]
            action = self.get_action({"act":"show","aim":row["kid"]})
            html = html.replace("ilv_first_action",action)
            html = html.replace("ilv_first_title",row["title"])
        return html
        pass
        
    ####################################################################
    # 3 getBody 网页主体
    ####################################################################
    def getBody(self):
        html = ""
        act = self.get_para("act")
        user_row = self.get_user_row()
        # 注意取消注释 不用if
        if user_row:
            user = str(user_row["kid"])
        else:
            user = "1"
        pattern = self.get_para("p")
        if user=="1" and pattern=="admin":
            act = "add"
            self.urlDict["act"] = act
            self.urlDict["sup"] = self.ACTIVE_SUP
        elif pattern=="admin":
            pass
        elif    act == self.PARAS["act"]:     
            html += self.getTotal() # 获得总览层 闪动照片 最近更新
            html += self.get_tab_htm() # get the tab
            html += self.getSubfields() # 3、分栏层 分栏显示下属栏目更新
            pass
        html += self.get_act_htm()
        return html
        pass

    ##################################################
    # getAct 1.2 操作内容
    ##################################################
    def get_act_htm(self):
        urlDict = self.urlDict
        act = self.get_para("act")
        htmlAction = ""
        if "act" not in urlDict:
            htmlAction += self.view() 
        elif urlDict["act"] == "view":
            htmlAction += self.view()
        elif urlDict["act"] == "add":
            htmlAction += self.add()
        elif urlDict["act"] == "show":
            htmlAction += self.show()
        elif act=="hire":
            htmlAction += self.hire()
        elif urlDict["act"] == "edit":
            htmlAction += self.edit()
        elif urlDict["act"] == "search":
            htmlAction += self.search()
        else:
            #htmlAction += self.view()
            html = self.get_templet(act)
            if html is None:
                html = self.view()
            else:
                html = html.replace("\r\n","<br>\r\n")
                html = html.replace("\r","-<br>\r")
                html = html.replace("\n","--<br>\n")
            htmlAction += html
        html = ""
        html += str(htmlAction)
        return html
        pass
    ############################################################
    # 3.1.1 view 浏览
    ############################################################
    def view(self):
        return self.search()
        pass
    ############################################################
    # 3.1.2 add
    ############################################################
    def add(self):
        return self.edit()
    ############################################################
    # 3.1.3 show
    ############################################################
    def show(self):
        return self.edit()
        pass
    ############################################################
    # 3.1.4 hire
    ############################################################
    def hire(self,act=None,aim=None,sup=None):
        if act==None:
            act = self.get_para("act")
        aim_row = self.get_aim_row(aim)
        dtname_row = self.get_module_row("dtname")
        if dtname_row is not None:
            dtname = dtname_row["dtname"]
            if dtname in self.DT_TABLES:
                key = act
                value = self.get_para(key)
                sql = ""
                sql += " update `%s`" % dtname
                sql += " set `%s`='%s'" % (key,value)
                sql += " where `kid`='%s'" % str(aim_row["kid"])
                sql += " limit 1"
                self.db.run()
                self.db.execute(sql)
                self.db.close()
            else:
                self.add_msg("Base.hire(act=%s,aim=%s,sup=%s):\
                    dtname=%s is not in self.DT_TABLES" \
                    % (str(act),str(aim),str(sup),str(dtname)))
        else:
            self.add_msg("Base.hire(act=%s,aim=%s,sup=%s):\
                     dtname_row=None." % (str(act),str(aim),str(sup)))
        action = self.get_action({"act":"view"})
        return self.goto(action)
    ####################################################################
    # 3.1.5 edit 编辑会员
    ####################################################################
    def edit(self):
        # 1 paras of url
        paras = {}
        paras["act"] = self.PARAS["act"]
        msg = ""
        act = self.get_para("act")
        sup = self.get_para("sup")
        aim = self.get_para("aim")
        dtname = self.get_module_row("dtname")["dtname"]
        # paras of form
        html = self.opfile.get_templet(act)
        html = html.replace("ilv_action",self.get_action())
        column_node = self.get_sup_node()
        html = html.replace("ilv_columnNode",column_node)
        row = {}
        if act=="edit" or act=="show":
            row = self.get_para("aim_row")
            html = html.replace("selected>",">")
            html = html.replace("value="+str(row[self.dtColumn])+" ",\
                "value="+str(row[self.dtColumn])+" selected")
        if act=="show" and row is not None:
            if str(row["image"])!="None" and row["image"]!="":
                html = html.replace("ilv_image",row["image"])
                html = html.replace("image style=display:none;","image")
            if str(row["video"])!="None" and row["video"]!="":
                html = html.replace("ilv_video",row["video"])
                html = html.replace("video style=display:none;","video")
        # 0-9 kid sid name account title ip password column icon video
        # image attach summary detail dtname class module css level hire
        # hire del datetime millisecond user source coment cite heat score
        ckeys = [\
            "kid","sid","name","account","title","ip","password",\
            "summary","detail","datetime","dtname",\
            "millisecond",\
            "sup","act","aim"\
            ]
        for ckey in ckeys:
            cvalue = str(self.get_para(ckey,row))
            html = html.replace("ilv_"+ckey,cvalue)
        # check the form
        succeed = False
        msg = ""
        if self.postDict is not None and len(self.postDict)>0:
            succeed = True
        # recover the image and video
        if succeed and act=="edit":
            # if there is no image upload,donont chanage
            if "image" in self.postDict and self.postDict["image"][0]["value"]=="":
                self.postDict["image"][0]["value"] = row["image"]
            if "video" in self.postDict and self.postDict["video"][0]["value"]=="":
                self.postDict["video"][0]["value"] = row["video"]
        # check the account and password of user when login
        if succeed and sup=="1015" and act=="add":
            account = self.postDict["account"][0]["value"]
            password = self.postDict["password"][0]["value"]
            self.db.run()
            user_row = self.db.get_row(self.dtUser,account,"account")
            self.db.close()
            if user_row is None:
                msg += "帐号%s不存在。" % account
                self.add_msg(msg)
                succeed = False
            # check the password when account is succeed
            if succeed:
                sql = ""
                sql += " select * from `%s`" % self.dtUser
                sql += " where `account`='%s'" % account
                sql += " and `password`='%s'" % password
                sql += " limit 1"
                self.db.run()
                self.db.execute_query(sql)
                users = self.db.get_row_dicts()
                if len(users)<1:
                    msg += "帐号%s与密码不匹配" % account
                    self.add_msg(msg)
                    succeed = False
                else:
                    paras["u"] = user_row["kid"]
            self.db.close()
        # 2 读取表单数据
        if succeed:
            html += "<br>"+str(self.postDict)+"<br>"
        if succeed:
            keys = self.postDict.keys()
            values = self.postDict.values()
            sql = None
            # 2.1 add record
            if act=="add":
                # 2.1.1 check column kid
                if "kid" in self.postDict:
                    kid = self.postDict["kid"][0]["value"]
                    canUse = False
                    kid = int(self.postDict[self.dtColumn][0]["value"])*100 + int(kid) - 1
                    while not canUse:
                        kid += 1
                        self.db.run()
                        row = self.db.get_row(dtname,str(kid))
                        self.db.close()
                        if row is None:
                            canUse = True
                    self.postDict["kid"][0]["value"] = str(kid)
                # 2.1.2 construct sql                
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
            elif act=="edit":
                sql = ""
                sql += " update `%s`" % dtname
                idx = 0
                for key in self.postDict:
                    idx += 1
                    if idx==1:
                        sql += " set `%s`='%s'" % (key,self.postDict[key][0]["value"]) 
                    else:
                        sql += ",`%s`='%s'" % (key,self.postDict[key][0]["value"])
                sql += " where `kid`='%s'" % row["kid"]
                sql += " limit 1"
            # 2.4 write data
            if sql is not None:
                html += sql + "<br>"
                self.db.run()
                self.db.execute(sql)
                self.db.close()
        # 3 goto the new html
        if succeed:
            return self.goto(action=self.get_action(paras=paras))
        # 4 show act html
        html = html.replace("ilv_msg",msg)
        return html
        pass
    ####################################################################################
    # 3.1.6 search 查找会员
    ####################################################################################
    def search(self,sup=None):
        html = ""
        if sup is None:
            sup = self.get_para("sup")
        # 1 load templet file
        html = self.opfile.get_templet("search")
        html = html.replace("ilv_action",self.get_action({"act":"search"}))
        # 2 get dtname
        dtname_row = self.get_module_row("dtname")        
        if dtname_row is not None:
            dtname = dtname_row["dtname"]
            if dtname in self.DT_TABLES:    
                row_html = self.opfile.get_templet("search_row")         
                sql = ""
                sql += " select * from `%s`" % dtname
                if dtname==self.dtNews:
                    sql += " where `%s` like '%s%%'" % (self.dtColumn,sup)
                svalue = ""
                if self.postDict and "skey" in self.postDict:
                    skey = self.postDict["skey"][0]["value"]
                    svalue = self.postDict["svalue"][0]["value"]
                    sql += " and `%s` like '%%%s%%'" % (skey,svalue)
                html = html.replace("ilv_svalue",str(svalue))
                #sql += " limit 25"
                self.db.run()
                self.db.execute_query(sql)
                rows = self.db.get_row_dicts()
                self.db.close()
                paras = {}
                # set the page
                page = int(self.get_para("page"))
                num_per_page = 10
                total_num = len(rows)
                total_page = int(total_num/num_per_page) + 1
                if page<1 or page>total_page:
                    page = 1
                sql += " limit %s,10" % ((page-1)*10)
                from_page = page-5
                if from_page<1:
                    from_page=1
                to_page = page+5
                if to_page>total_page:
                    to_page = total_page
                page_html = ""
                page_html += "<div id=div_page>"
                page_html += "<a href=%s>首页</a>&nbsp;&nbsp;" \
                    % self.get_action({"page":1})
                if page>1:
                    page_html += "<a href=%s>上一页</a>&nbsp;&nbsp;" \
                        % self.get_action({"page":page-1})
                while from_page<=to_page:
                    action = self.get_action({"page":from_page})
                    if from_page==page:
                        page_html += "<font color=red>第%s页</font>&nbsp;&nbsp;" % (from_page)
                    else:
                        page_html += "<a href=%s>第%s页</a>&nbsp;&nbsp;" \
                            % (action,from_page)
                    from_page += 1
                if page<total_page:
                    page_html += "<a href=%s>下一页</a>&nbsp;&nbsp;" \
                        % self.get_action({"page":page+1})
                page_html += "<a href=%s>末页</a>&nbsp;&nbsp;" \
                    % self.get_action({"page":total_page})
                page_html += "</div><!--/div_page-->"
                self.db.run()
                self.db.execute_query(sql)
                rows = self.db.get_row_dicts()
                self.db.close()
                
                tmp_html = ""
                for row in rows:
                    tmp_html = row_html
                    if sup==self.COLUMN_SUP:
                        pass
                    else:
                        sup = str(row[self.dtColumn])
                        sup_row = self.get_sup_row(sup)
                    paras["sup"] = sup
                    paras["act"] = "view"
                    action = self.get_action(paras)
                    tmp_html = tmp_html.replace("ilv_sup_action",action)         
                    tmp_html = tmp_html.replace("ilv_sup_title",sup_row["title"])
                    paras["aim"] = row["kid"]
                    paras["act"] = "show"
                    action = self.get_action(paras)
                    tmp_html = tmp_html.replace("ilv_action_show",action)
                    if sup==self.COLUMN_SUP:
                        tmp_html = tmp_html.replace("ilv_title",str(row["kid"])+row["title"])
                    elif sup==self.ACTIVE_SUP:
                        tmp_html = tmp_html.replace("ilv_title",str(row["account"]))
                        html = html.replace("发布","登录")
                    else:
                        tmp_html = tmp_html.replace("ilv_title",str(row["title"]))
                    tmp_html = tmp_html.replace("ilv_datetime",str(row["datetime"]))
                    admin_html = ""
                    user_row = self.get_user_row()
                    if user_row["account"]=="admin":
                        paras["act"] = "edit"
                        admin_html += "<a href=%s>编辑</a>&nbsp;" % self.get_action(paras)
                        paras["act"] = "hire"
                        hires = ["删除","隐藏","未审","普通","优质","头条"]
                        paras["hire"] = -3
                        for hire in hires:
                            paras["hire"] += 1
                            action = self.get_action(paras)
                            if row["hire"]==paras["hire"]:
                                admin_html += "%s&nbsp;" % hire
                            else:
                                admin_html += "<a href=%s>%s</a>&nbsp;" % (action,hire)
                    tmp_html = tmp_html.replace("ilv_admin",admin_html)
                    html = html.replace("<ilv_row />",tmp_html+"<ilv_row />")
                html = html.replace("<ilv_page />",page_html)

            else:
                self.add_msg("Base.hire(act=%s,aim=%s,sup=%s):\
                    dtname=%s is not in self.DT_TABLES" \
                    % (str(act),str(aim),str(sup),str(dtname)))            
        else:
            self.add_msg("Base.search(sup=%s):dtname_row is None."\
                         % str(sup))    
        
        return html
        pass
    ##################################################
    # 2 getTotal
    ##################################################
    def getTotal(self):
        sup = self.get_para("sup")
        dtname_row = self.get_module_row("dtname")
        #注意取消注释 不用if
        if dtname_row:
            dtname = dtname_row["dtname"]
        else:
            dtname = "news"
        html = self.opfile.get_templet("total")
        sql = ""
        sql += " select * from `%s`" % dtname
        sql += " where `item` like '%s%%'" % sup
        sql += " and `image` like '%.jpg'"
        sql += " order by `kid` desc"
        sql += " limit 5"
        self.db.run()
        self.db.execute_query(sql)        
        rows = self.db.get_row_dicts()
        self.db.close()
        idx = 0
        srcs = ""
        hrefs = ""
        titles = ""
        split = ""
        for row in rows:
            idx += 1
            if idx>1:
                split = "|"
            srcs += split + row["image"]
            hrefs += split + ("/py?sup=%s&act=show&aim=%s" % (sup,row["kid"]))
            titles += split + row["title"]
        html = html.replace("ilv_srcs",srcs)
        html = html.replace("ilv_hrefs",hrefs)
        html = html.replace("ilv_titles",titles)
        html = html.replace("ilv_recent",self.getRecent())
        return html
    ##################################################
    # 2.1 getRecent
    ##################################################
    def getRecent(self):
        html = ""
        sup = self.get_para("sup")
        recentHtml = self.opfile.get_templet("recent")
        self.db.run()
        sql = "select * from `news` order by `kid` desc limit 10"
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        self.db.close()
        for row in rows:
            tmpStr = recentHtml
            action = self.get_action({"sup":sup,"act":"show","aim":row["kid"]})
            tmpStr = tmpStr.replace("ilv_action",action)
            tmpStr = tmpStr.replace("ilv_title",row["title"])
            tmpStr = tmpStr.replace("ilv_datetime",str(row["datetime"]))
            html += tmpStr
        return html
        pass
    ##################################################
    # 2 get_tab_htm
    ##################################################
    def get_tab_htm(self):
        html = ""
        sup = self.get_para("sup")
        html = self.opfile.get_templet("tab")
        self.db.run()
        sql = ""
        sql += " select * from `%s`" % self.dtColumn
        sql += " where `level`>='1'"
        sql += " and ("
        sql += " `kid`='1022' or `kid`='1023' or `kid`='1024'"
        sql += " or `%s` like '1025%%')" % self.dtColumn
        sql += " order by `kid` asc"
        sql += " limit 10"
        print("ilv.core.web.Web.get_tab_htm:sql="+sql+"\r\n<br>")
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        print("ilv.core.web.Web.get_tab_htm:rows="+str(rows)+"\r\n<br>")
        self.db.close()
        rowIdx = 0
        paras = {}
        for row in rows:
            rowIdx += 1
            paras["sup"] = row["kid"]
            paras["act"] = "view"
            action = self.get_action(paras)
            if rowIdx==1:
                html = html.replace("tab_menu_hide","tab_menu_on",1)
            else:
                html = html.replace("tab_menu_hide","tab_menu_off",1)
            html = html.replace("ilv_menu_action",action,1)
            html = html.replace("ilv_menu_title",row["title"],1)
            sql = ""
            sql += " select * from `news`"
            sql += " where `item` like '%s%%'" % row["kid"]
            sql += " order by `kid` desc"
            sql += " limit 10"
            self.db.run()
            self.db.execute_query(sql)            
            news_rows = self.db.get_row_dicts()
            self.db.close()
            tab_content = ""
            for news_row in news_rows:
                paras["act"] = "show"
                paras["aim"] = news_row["kid"]
                tab_content += """
                <a href=%s target=_blank>
                """ % self.get_action(paras=paras)
                tab_content += news_row["title"]
                tab_content += """
                </a><br><!--/tab_content_row-->
                """
            html = html.replace("ilv_tab_content",tab_content,1)
        return (html)
    ##################################################
    # 3、分栏层 subfields 分栏显示
    ##################################################
    def getSubfields(self):
        html = ""
        html += '''
        <!--3、分栏层 subfields-->
        <div id=divSubfields>
        '''
        sup = self.PARAS["sup"]
        if self.urlDict and "sup" in self.urlDict and self.urlDict["sup"]:
            sup = self.urlDict["sup"]
        self.db.run()
        sql = ""
        sql += " select * from `item`"
        sql += " where `item`='%s'" % sup
        sql += " and `level`='1'"
        sql += " order by `sid` asc"
        sql += " limit 6"
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        self.db.close()
        idx = 0
        for row in rows:
             idx += 1
             # html += "总栏目号："+sup+"。<br>"
             subClass = "subLeft"
             if idx%2==0:
                 subClass = "subRight"
             action = self.get_action({"sup":row["kid"],"act":"view"})
             html += '''
             <!--3.0 单个分栏-->
             <div class=%s>
                 <div class=subTitle>
                     <font color=red>★</font>
                     <a href=%s><font color=#FFFFFF>%s</font></a>
                 </div>
                 %s
             </div>
             <!--3.0 单个分栏-->
             ''' % (subClass,action,row["title"],self.getSubfield(row))            
        html += '''
        </div>
        <!--/3、分栏层 subfields-->
        '''
        return html
        pass
    ##################################################
    # 3.0、单个分栏 getSubfield
    ##################################################
    def getSubfield(self,row=None):
        html = ""
        if row==None:
            return "单个分栏中row为None"
        sup = row["kid"] # 获得需要查阅的栏目kid
        name = "news"
        self.db.run()
        sql = ""
        sql += " select * from `%s`" % name
        sql += " where `item` like '%s%%'" % sup
        sql += " and `level`='1'"
        sql += " order by `datetime` desc"
        sql += " limit 10"
        # html += "<div class=rowSolid>sql语句为："+sql+"。</div>"
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        self.db.close()
        for row in rows:
            kid = row["kid"]
            sup = row[self.dtColumn]
            action = self.get_action({"sup":sup,"act":"show","aim":kid})
            html += '''
                <div class=subRow><!--第二行右栏行-->★
                    <a href=%s target=_blank><!--记录显示链接-->                    
                        %s                    
                    </a><!--/记录显示链接-->
                </div><!--/第二行右栏行-->            
            ''' % (action,row["title"])        
        return html
        pass
    ##################################################
    # htmlTail 网页尾
    ##################################################
    def getTail(self):
        htmlTail = """
        %s
        </div></center><!--/最外层边框-->
        <div style=height:5px;>&nbsp;</div>
        </body>
        </html>
        """ % self.msg
        return htmlTail        




             
