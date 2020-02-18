#!/usr/local/bin/python3
#-*-code:utf8-*-
"""
1.This is a base class of html.
2.When import this class we can get a default html.
3.The other class (for exampe Microblog) is the child of MyBase
"""
# python library
import os,datetime,mysql.connector

import ilv.Base
import ilv.MyData
###################################################################################################
# Microblog 微博网页
###################################################################################################
class Microblog(ilv.Base.Base):
    def __init__(self):
        ilv.Base.Base.__init__(self)
    ###################################################################################################
    # getBody 网页主体
    ###################################################################################################
    def getBody(self):
        html = ""
        html += "<div id=div_first><!--第一行-->"
        html += self.getFirstLeft()
        html += self.getFirstRight()
        html += self.getFirstMiddle()
        html += "</div><!--/第一行-->"
        return html
    def addRecord(self):
        addHtml = '''\
            <form method=post action=%s enctype=multipart/form-data>
            <img src=/images/xxs.png />
            <input type=text name=title value='' /><img src=/images/addTitle.png height=20 />
            <textarea name=summary style=width:100%%;height:100px;></textarea>
            <img title=图片上传 src=/images/image.png /><input type=file name=image />
            <img src=/images/imageUpload.png height=20 /><br>
            <img tilte=视频上传 src=/images/video.png /><input type=file name=video />
            <img src=/images/videoUpload.png height=20 /><br>
            <input type=submit value=提交 />&nbsp;&nbsp;
            <input type=reset value=清空 />
            <input type=hidden name=run value=yes />
            </form>
        ''' % self.action
        # 保存视频文件
        now = datetime.datetime.today()
        tmpStr = str(now)
        nowStr = tmpStr[:4] + tmpStr[5:7] + tmpStr[8:10] + tmpStr[11:13] + tmpStr[14:16] + tmpStr[17:19] + tmpStr[20:26] 
        video = ""
        if "video" in self.postDict and self.postDict["video"]["filename"] :
            uploadfileName = self.postDict["video"]["filename"]
            head,tail = os.path.splitext(uploadfileName)
            videoDir = "upload/videos/"
            if not os.path.exists(videoDir):
                os.mkdirs(videoDir) # 创建必要的文件夹
            video = videoDir + nowStr + tail
            output = open(video,"wb+",10000)
            output.write(self.postDict["video"]["bValue"])
            output.close()
        # 保存图片文件
        now = datetime.datetime.today()
        tmpStr = str(now)
        nowStr = tmpStr[:4] + tmpStr[5:7] + tmpStr[8:10] + tmpStr[11:13] + tmpStr[14:16] + tmpStr[17:19] + tmpStr[20:26] 
        image = ""
        if "image" in self.postDict and self.postDict["image"]["filename"] :
            uploadfileName = self.postDict["image"]["filename"]
            head,tail = os.path.splitext(uploadfileName)
            imageDir = "upload/images/"
            if not os.path.exists(imageDir):
                os.mkdirs(imageDir) # 创建必要的文件夹
            image = imageDir + nowStr + tail
            output = open(image,"wb+",10000)
            output.write(self.postDict["image"]["bValue"])
            output.close()

        if "title" in self.postDict: # update the database
            sqlString = ""
            sqlString += " INSERT INTO `微博`"
            sqlString += " (`标题`,`摘要`,`附图`,`视频`)"
            sqlString += " VALUES('%s','%s','%s','%s')" % (self.postDict["title"]["value"],self.postDict["summary"]["value"],image,video)
            md = ilv.MyData.MyData()
            md.execute(sqlString)
            md.close()
        return addHtml
    def getFirstLeft(self): # 第一行左栏        
        query = ("SELECT `编号`,`标题` FROM `版块` WHERE `权限`=1")
        md = ilv.MyData.MyData()
        md.executeQuery(query)
        cursor = md.getData()
        md.close()
        p = "1"
        if "p" in self.urlDict:
            p = self.urlDict["p"]
        html = '''
          <div id=div_firstLeft><!--第一行左栏-->
            <!--首页、消息、收藏、@我-->
            <div class=iconsOuterDiv onmouseover=icons_index.style.left="-25px";div_iconsText.style.color="red"; onmouseout=icons_index.style.left="0px";div_iconsText.style.color="black";><!--首页-->
              <a href=/index.py?p=%s>
                <div class=iconsDiv><img id=icons_index src=/images/icons.png style=position:relative;left:0px;top:-25px; /></div>
                <div id=div_iconsText style=position:relative;left:20px;top:-20px;>&nbsp;首&nbsp;页&nbsp;</div>
              </a>
            </div><!--/首页-->
            <div class=iconsOuterDiv \
             onmouseover=div_iconsMessage.style.left="-25px";div_iconsMessageText.style.color="red";\
             onmouseout=div_iconsMessage.style.left="0px";div_iconsMessageText.style.color="black";\
            ><!--消息-->
            <a href=/index.py?p=%s>
              <div class=iconsDiv><img id=div_iconsMessage src=/images/icons.png style=position:relative;left:0px;top:-250px; /></div>
              <div id=div_iconsMessageText style=position:relative;left:20px;top:-20px;>&nbsp;消&nbsp;息&nbsp;</div>
            </a>
            </div><!--/消息-->
            <div class=iconsOuterDiv \
             onmouseover=div_iconsFavor.style.left="-25px";div_iconsFavorText.style.color="red";\
             onmouseout=div_iconsFavor.style.left="0px";div_iconsFavorText.style.color="black";\
            ><!--消息-->
            <a href=/index.py?p=%s>
              <div class=iconsDiv><img id=div_iconsFavor src=/images/icons.png style=position:relative;left:0px;top:-125px; /></div>
              <div id=div_iconsFavorText style=position:relative;left:20px;top:-20px;>&nbsp;收&nbsp;藏&nbsp;</div>
            </a>
            </div><!--/收藏-->
            <div class=iconsOuterDiv\
             onmouseover=div_iconsAtme.style.left="-25px";div_iconsAtmeText.style.color="red";\
             onmouseout=div_iconsAtme.style.left="0px";div_iconsAtmeText.style.color="black";\
            ><!--消息-->
            <a href=/index.py?p=%s>
              <div class=iconsDiv><img id=div_iconsAtme src=/images/icons.png style=position:relative;left:0px;top:-150px; /></div>
              <div id=div_iconsAtmeText style=position:relative;left:20px;top:-20px;>&nbsp;@我&nbsp;</div>
            </a>
            </div><!--/@我-->
            <hr>       
            ''' % (p,p,p,p)
        for (id,title) in cursor:
            html = '''
            %s
                <a href=?c=%s target=_blank>
                  %s
                </a><br>
            ''' % (html,str(id),str(title))
        html = '''
        %s
        </div><!--/第一行左栏-->
        ''' % html
        return html
    def getFirstRight(self): # 第一行右栏
        cnx = mysql.connector.connect(user='root',database='ilvbobing_db')
        cursor = cnx.cursor()
        query = ("SELECT `kid`,`title` FROM `user` WHERE `level`=1")
        cursor.execute(query)
        html = "  <div id=div_firstRight><!--第一行右栏-->\n"
        p = "1"
        if "p" in self.urlDict:
            p = self.urlDict["p"]
        for (id,title) in cursor:
            html += "<a href=?w=%s&p=%s target=_blank>" % (str(id),p)
            html += str(title)
            html += "</a>"
            html += "<br>\n"
        html += "    </div><!--/第一行右栏-->\n"
        return html
    def getFirstMiddle(self): # 第一行中栏
        htmlFirstMiddle = ""
        c = ""
        if "c" in self.urlDict:
            c = self.urlDict["c"]
        if c: # 如果地址栏中的栏目是合法的
            query = '''\
            SELECT `编号`,`标题`,`视频`,`附图`,`附件`,`摘要`,`帐户`,`IP`,`时间`,`微秒` 
            FROM `微博` WHERE `上级`=11 AND `权限`=1 ORDER BY `编号` DESC
            '''
        else:
            query = "SELECT `kid`,`title`,`video`,`image`,`attach`,`summary`,`user`,`ip`,`datetime`,`microseconds` FROM `microblog` WHERE `level`=1 ORDER BY `kid` DESC LIMIT 5"
        query = "SELECT `编号`,`标题`,`视频`,`附图`,`附件`,`摘要`,`帐户`,`IP`,`时间`,`微秒` FROM `微博` WHERE `级别`=1 ORDER BY `编号` DESC LIMIT 15"
        htmlFirstMiddle += "  <div id=div_firstMiddle><!--第一行中栏-->\n"
        htmlFirstMiddle += self.addRecord()
        md = ilv.MyData.MyData()
        md.executeQuery(query)
        results = md.getData()
        for (id,title,video,image,attach,summary,user,ip,datetime,microseconds) in results:
            # 显示会员名称
            queryUser = "SELECT `编号`,`昵称` FROM `帐户` WHERE `编号`='%s' LIMIT 1" % user
            md.executeQuery(queryUser)
            resultsUsr = md.getData()
            for userId,userTitle in resultsUsr:
                htmlFirstMiddle += '''\
                <div class=userTitle onmouseover=this.style.color="red"; onmouseout=this.style.color="black";><!--微博作者-->
                  <a href=/index.py?p=",userId,">%s----%s----%s----%s</a>
                </div>
                ''' % (userTitle,ip,datetime,microseconds)
            htmlFirstMiddle += "<div class=summary><!--微博内容-->"
            htmlFirstMiddle += "<a href=?clm=%s target=_blank>" % str(id)
            htmlFirstMiddle += "[%s]%s" % (title,summary)
            htmlFirstMiddle += "</a>"
            htmlFirstMiddle += "<br>\n"
            htmlFirstMiddle += "<div style=white-space:nowrap;text-overflow:hidden;><!--所有上传外框-->"
            if video and False:
                htmlFirstMiddle += '''\
                <embed src="/video/Flvplayer.swf?fid=%s" style="width:296px;height:200px;overflow:hidden;border:1px solid #888;" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" scale="exactfit" menu="false" wmode="transparent" autostart=false></embed>
                ''' % video
            if video:
                htmlFirstMiddle += '''
    <embed src=/video/Flvplayer.swf allowfullscreen=true flashvars=vcastr_file=%s&LogoText=WWW.DLTZG.QH.LZ&BufferTime=30 quality=high pluginspage=http://www.macromedia.com/go/getflashplayer type=application/x-shockwave-flash width=296 height=200></embed>
                ''' % video
            if image:
                htmlFirstMiddle += '''\
                <a href=%s target=_blank><img width=296 height=200 src=%s /></a><br>\n
                ''' % (image,image)
            if attach:
                htmlFirstMiddle += '''\
                <a href=%s target=_blank>下载附件</a>
                ''' % attach
            htmlFirstMiddle += "</div><!--/所有上传外框-->";
            htmlFirstMiddle += "</div><!--/微博内容-->"
        htmlFirstMiddle += "    </div><!--/第一行中栏-->\n"
        md.close()
        return htmlFirstMiddle
    ###################################################################################################
    # getHtml
    ###################################################################################################
    def getHtml(self):
        html = ""
        html += "(测试microblog.getHtml)urlDict=" + str(urlDict) + "<br>"
        return html
        if "TEST" in self.urlDict :
            html += "(测试microblog.getHtml)" + "<br>"
        html += "<div id=div_first><!--第一行-->"
        html += self.getFirstLeft()
        html += self.getFirstRight()
        html += self.getFirstMiddle()
        html += "</div><!--/第一行-->"
        return html
