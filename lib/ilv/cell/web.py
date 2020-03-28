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
# Cell 手机端网页 是页面拓展基础类的子类
# 主要分以下几层：
# 一、操作层：control 浏览 添加 删除 编辑 查找 统计 登陆 注消
# 二、总览层：total 闪动照片 最近更新
# (一)闪动照片 getShine (二)最近更新 getRecent
# 三、分栏层：subfield 分栏显示
# 四、列表层：list 列表显示
########################################################################
class Web(ilv.core.web.Web):
    #===================================================================
    # 1 基本属性 base profile
    #===================================================================

    #===================================================================
    # 2 预备方法 pre method
    #===================================================================
    
    # 2.1 constructor 构造函数
    #========================
    def __init__(self,env):
        """__init__ construct the class
        
        """
        # 父类方法：super(子类，self).__init__(参数1，参数2，....)
        # 经典写法：父类名称.__init__(self,参数1，参数2，...)
        ilv.core.web.Web.__init__(self,env=env)
        self.opfile.plat = "cell"
        
        # init paras
        pass

    ####################################################################
    # IV help method 辅助方法
    ####################################################################
    ####################################################################
    # 1 getHead get html head
    ####################################################################
    def get_head_htm(self):
        html = ilv.core.web.Web.get_head_htm(self)
        return html 
      
    ####################################################################
    # 1.1 get_control_htm
    ####################################################################
    def get_control_htm(self):
        html = ilv.core.web.Web.get_control_htm(self)
        return html

    ####################################################################
    # 2 get_menu_htm 获得网页菜单
    ####################################################################
    def get_menu_htm(self):
        html = ilv.core.web.Web.get_menu_htm(self)
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
            user_lev = str(user_row["level"])
        else:
            user = "1"
        pattern = self.get_para("p")
        if user=="1" and pattern=="admin":
            act = "add"
            self.urlDict["act"] = act
            self.urlDict["sup"] = self.GUEST_SUP
        html += self.get_act_htm()
        return html
        pass

    ##################################################
    # getAct 1.2 操作内容
    ##################################################
    def get_act_htm(self):
        html = ilv.core.web.Web.get_act_htm(self)
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
        html = ilv.core.web.Web.hire(self,act=act,aim=aim,sup=sup)
        return html

    ####################################################################
    # 3.1.5 edit 编辑会员
    ####################################################################
    def edit(self):
        html = ilv.core.web.Web.edit(self)
        return html
        pass

    ####################################################################
    # 3.1.6 search 查找会员 对ilv.core.web.Web.search进行了重写
    ####################################################################
    def search(self,sup=None):
        html = "" # 需要返回的变量
        row_html = "" # 单位记录信息
        sql = "" # SQL执行语句
        skey = "" # 关键字
        svalue = "" # 匹配值
        
        # 1. 设置初始变量
        # ==================================
        # 1.1 设置表单状态
        #-----------------
        skey_num = 0 # 0未提交 1只有一个关键字 2有两个关键字
        if self.postDict and "skey" in self.postDict:
            skey_num = len(self.postDict["skey"])
        # 1.2 前台信息
        # ------------
        html = self.opfile.get_templet(name="search")
        html = html.replace("ilv_action",self.get_action({"act":"search"}))
        row_html = self.opfile.get_templet(name="search_row") 
        u = self.get_para(name="u") # 访问会员kid
        sup = self.get_para(name="sup")
        sup_row = self.get_para(name="sup_row")
        dtname = sup_row["dtname"]
        # 1.3 设置SQL语句
        # ---------------
        sql = "select * from `%s`" % dtname
        # 1.3.1 设置栏目范围
        if dtname==self.dtColumn:
            # 如果是对栏目进行管理，查看所有栏目
            sql += "where 1=1"
        else:
            # 如果是对会员、新闻进行管理，查看当前栏目下记录信息
            sql += "where `%s` like '%%%s%%'" % (self.dtColumn,sup)
        # 1.3.3 设置录用状态
        if skey_num==0:
            # 如果未提交，正常显示信息，不显示私有信息
            sql += "and `hire`>0"
        elif skey_num==1:
            # 如果只有一个关键字，显示公众信息、会员所属信息
            sql += "and (`hire`>0 or `user`='%s' )" % u
        else:
            # 如果是查询审核进度，显示私有信息
            sql += "and `hire`=-1"
        # 1.3.4 设置查询变量
        if skey_num==1:
            # 一般性查询
            skey = self.postDict["skey"][0]["value"]
            svalue = self.postDict["svalue"][0]["value"]
            sql += " and `%s` like '%%%s%%' " % (skey,svalue)
        elif skey_num==2:
            # 查询审核进度
            # 匹配身份证号
            skey = self.postDict["skey"][0]["value"]
            svalue = self.postDict["svalue"][0]["value"]
            sql += " and `%s`='%s' " % (skey,svalue)
            # 匹配准考证号
            skey = self.postDict["skey"][1]["value"]
            svalue = self.postDict["svalue"][1]["value"]
            sql += " and `%s`='%s' " % (skey,svalue)  
        # 设置当前关键字  
        html = html.replace("ilv_svalue",str(svalue))
        
        # 2 执行SQL语句
        # =============
        self.db.run()
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        self.db.close()
        
        # 3 设置页码
        # ==========    
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
        
        # 4 展示当前页面
        # =============
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
            tmp_html = tmp_html.replace("ilv_summary",str(row["summary"]))
            tmp_html = tmp_html.replace("ilv_datetime",str(row["datetime"]))
            tmp_html = tmp_html.replace("ilv_user",str(row["account"]))
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

        return html
        pass
    ##################################################
    # 2 getTotal
    ##################################################
    def getTotal(self):
        html = ilv.core.web.Web.getTotal(self)
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
        # print("ilv.core.web.Web.get_tab_htm:sql="+sql+"\r\n<br>")
        self.db.execute_query(sql)
        rows = self.db.get_row_dicts()
        # print("ilv.core.web.Web.get_tab_htm:rows="+str(rows)+"\r\n<br>")
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






             
