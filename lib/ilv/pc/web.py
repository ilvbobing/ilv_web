######!/usr/local/bin/python3
#!/usr/bin/env python3
#-*-code:utf8-*-

"""
1.This is a base class of html.
2.When import this class we can get a default html.
3.The other class (for exampe Microblog) is the child of MyBase
"""
# python library
import ilv.core.web

########################################################################
# Base 基础网页 是页面拓展的基础类
# 主要分以下几层：
# 一、操作层：control 浏览 添加 删除 编辑 查找 统计 登陆 注消
# 二、总览层：total 闪动照片 最近更新
# (一)闪动照片 getShine (二)最近更新 getRecent
# 三、分栏层：subfield 分栏显示
# 四、列表层：list 列表显示
########################################################################
class Web(ilv.core.web.Web):

    ################################################################
    # 1 constructor 构造函数
    ################################################################
    def __init__(self,env):
        """__init__ construct the class
        
        """
        # 父类方法：super(子类，self).__init__(参数1，参数2，....)
        # 经典写法：父类名称.__init__(self,参数1，参数2，...)
        ilv.core.web.Web.__init__(self,env=env)
        self.opfile.plat = "pc"  
        # init paras
        pass

    ####################################################################
    # IV help method
    ####################################################################
    ####################################################################
    # 1 getHead get html head
    ####################################################################
    def get_head_htm(self):
        html = ilv.core.web.Web.get_head_htm(self);
        return html 
    ################################################################
    # 1.1 get_control_htm
    ################################################################
    def get_control_htm(self):
        html = ""
        sup_row = self.get_para("sup_row")
        html = self.opfile.get_templet("control")
        html = html.replace("ilv_title",sup_row["title"])
        paras = {}
        paras["act"] = "add"
        action_add = self.get_action(paras)
        html = html.replace("ilv_action_add",action_add)
        paras["act"] = "view"
        action_view = self.get_action(paras)
        html = html.replace("ilv_action_view",action_view)
        return html
    ############################################################################################
    # 2 get_menu_htm 获得网页菜单
    ############################################################################################
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
        titles = "网站首页"
        urls = action
        if sup!="10":
            paras["sup"] = sup
            action = self.get_action(paras)
            titles += "|%s" % sup_row["title"]
            urls += "|"+action
        for subRow in subRows:
            paras["sup"] = subRow["kid"]
            action = self.get_action(paras)
            titles += "|%s" % subRow["title"]
            urls += "|"+action
        html = self.opfile.get_templet("menu")
        html = html.replace("ilv_titles",titles)
        html = html.replace("ilv_urls",urls)
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
    ################################################################
    # 3 getBody 网页主体
    ################################################################
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
            html = self.opfile.get_templet(act)
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
    ####################################################################
    # 3.1.5 edit 编辑会员
    ####################################################################
    def edit1(self):
        # 1 paras of url
        paras = {}
        paras["act"] = self.PARAS["act"]
        sup = self.get_para("sup")
        dtname = self.get_module_row("dtname")["dtname"]
        act = self.get_para("act")
        # paras of form
        html = self.opfile.get_templet(act)
        html = html.replace("ilv_action",self.get_action())
        column_node = self.get_sup_node()
        msg = ""
        aim = "" # 0
        sid = "" # 1
        title = "" # 2
        account = ""
        ip = self.env.getClient()
        password = ""
        name = ""
        summary = ""        
        detail = ""
        aim_dtname = ""
        t = ilv.Time.Time()
        datetime = t.getDatetime()
        millisecond = t.getMillisecond()
        aimRow =    self.get_aim_row()
        if act=="edit" or act=="show":
            if aimRow is not None:
                aim = str(aimRow["kid"])
                sid = str(aimRow["sid"])
                title = aimRow["title"]
                account = aimRow["account"]
                name = aimRow["name"]
                ip = aimRow["ip"]
                summary = aimRow["summary"]
                detail = aimRow["detail"]
                aim_dtname = str(aimRow["dtname"])
                aim_column = str(aimRow["column"])
                password = aimRow["password"]
                # set column node
                column_node = column_node.replace("selected>",">")
                split = "value="+aim_column+" "
                column_node = column_node.replace(split,split+"selected")
        if act=="show" and aimRow is not None:
            if str(aimRow["image"])!="None" and aimRow["image"]!="":
                html = html.replace("ilv_image",aimRow["image"])
                html = html.replace("image style=display:none;","image")
            if str(aimRow["video"])!="None" and aimRow["video"]!="":
                html = html.replace("ilv_video",aimRow["video"])
                html = html.replace("video style=display:none;","video")
        html = html.replace("ilv_columnNode",column_node)
        html = html.replace("ilv_kid",aim)
        html = html.replace("ilv_sid",sid)
        if ip is None:
            ip = self.env.getClient()
        html = html.replace("ilv_ip",ip)
        html = html.replace("ilv_sup",str(sup))
        html = html.replace("ilv_act",act)
        html = html.replace("ilv_aim",str(aim))
        html = html.replace("ilv_account",str(account))
        html = html.replace("ilv_password",str(password))
        html = html.replace("ilv_title",title)
        html = html.replace("ilv_dtname",aim_dtname)
        if name is None:
            name = ""
        html = html.replace("ilv_name",name)
        if summary is None:
            summary = ""
        html = html.replace("ilv_summary",summary)
        if detail is None:
            detail = ""
        html = html.replace("ilv_detail",detail)
        html = html.replace("ilv_datetime",datetime)
        html = html.replace("ilv_millisecond",millisecond)
        # check the form
        succeed = False
        msg = ""
        if self.postDict is not None and len(self.postDict)>0:
            succeed = True
        # recover the image and video
        if succeed and act=="edit":
            # if there is no image upload,donont chanage
            if "image" in self.postDict and self.postDict["image"][0]["value"]=="":
                self.postDict["image"][0]["value"] = aimRow["image"]
            if "video" in self.postDict and self.postDict["video"][0]["value"]=="":
                self.postDict["video"][0]["value"] = aimRow["video"]
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
                sql += " where `kid`='%s'" % aimRow["kid"]
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
                        sup_row = {"title":"首页"}
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
        # set right
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
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
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




             
