#!/usr/local/bin/python3
#-*-code:utf8-*-

'''
Env 环境变量类
1 读取表单参数
2 读取地址参数
'''

# 1 引入官方库
import os # 系统：文件　路径
import datetime # 时间
import re # 正则表达式
# 2 引入用户库
#import ilv.config

####################################################################################################
# Environ 环境变量控制类
# 1 读取并保存表单参数
# 2 读取并保存地址参数
####################################################################################################
class Env:
    formDicts = None # 表单字典集
    environ = None # 环境变量
    host = None # HTTP_HOST
    client = None # REMOTE_ADDR
    def __init__(self,environ):
        self.environ = environ
        return
    ################################################################################################
    # II prepare method
    ################################################################################################
    ############################################################################################
    # 1 getHost returned value maybe localhost or 24.71.66.15
    ############################################################################################
    def getHost(self):
        if self.host is None:
            self.host = self.environ["HTTP_HOST"]
        return self.host
    ############################################################################################
    # 2 getClient returned value of the remote address,also is the client's ip
    ############################################################################################
    def getClient(self):
        if self.client is None:
            self.client = self.environ["REMOTE_ADDR"]
        return self.client
    ################################################################################################
    # 1 getFormDicts 获取表单参数集(enctype=multipart/form-data)
    # 1.1 一般参数直接存入字典集
    # 1.2 文件存入字典并保存到tmpDiv/image(video、attach)下
    # 1.3 如果文件没有传入，字典不做记录，防止记录不必要的地址,此时node["filename"]=""
    # 1.4 为确保数据读取一致，保存文件结点时设置node["value"]=node["filename"]
    # postStream输入流 tmpDir文件保存位置 isCheck是否调试
    ################################################################################################
    def getFormDicts(self,tmpDir=None,isCheck=False):
        postStream = self.environ["wsgi.input"]
        formDicts = self.formDicts
        if formDicts is not None:
            return formDicts
            pass
        # 1 初始化表单参数集
        if postStream is None:
            return None # 如果没有输入流返回None
            pass
        if tmpDir is None:
            tmpDir = "upload/"
        # 2 建立必要的文件夹
        if not os.path.exists(tmpDir):
            os.makedirs(tmpDir) # 上传文件夹
        if not os.path.exists(tmpDir+"image/"):
            os.mkdir(tmpDir+"image/") # 图片文件夹
        if not os.path.exists(tmpDir+"video/"):
            os.mkdir(tmpDir+"video/") # 视频文件夹
        if not os.path.exists(tmpDir+"attach/"):
            os.mkdir(tmpDir+"attach/") # 附件文件夹
        # 1.3 设置调试文本文件
        if isCheck:
            now = datetime.datetime.now()
            tmpStr = str(now)
            nowStr = ""
            nowStr += tmpStr[:4]+"-"+tmpStr[5:7]+"-"+tmpStr[8:10]
            nowStr += tmpStr[11:13]+tmpStr[14:16]+tmpStr[17:19]
            ms = tmpStr[20:]
            if len(ms)>2:
                ms = ms[:-3]
            else:
                ms = "000"
            while len(ms)<3:
                ms = "0"+ms
            nowStr += "."+ms
            output = open(tmpDir+nowStr+".txt","wb+",1) # 1表示用行缓冲区
        # 4 设置开始结束标志
        data = postStream.readline()
        start = data # b'-----------------------------11271650311059970388103151456\r\n'
        # end = b'-----------------------------11271650311059970388103151456--\r\n'
        end = start.replace(b"\r\n",b"--\r\n")
        # 5 设置初始变量
        if data: # 有表单数据
            formDicts = {} # 表单字典集
            node = {} # 单个参数字典
            imageTypes = [".jpg",".png",".gif"] # 图片类型
            videoTypes = [".avi",".wmv",".flv"] # 视频类型
            attachTypes = [".rar",".zip",".tar"] # 附件类型
        # 5 循环读取数据       
        while data: 
            # 5.1 写入调试文件           
            if isCheck: 
                output.write(data)
            # 5.2 开始标志或结束标志
            if data==start or data==end: 
                # 5.2.1 保存上一结点
                if node and "name" in node and node["name"]:
                    if node["name"] not in formDicts:
                        formDicts[node["name"]] = []
                    formDicts[node["name"]].append(node)
                # 5.2.2 关闭文件
                if node and "filename" in node:
                    if node["filename"]:
                        node["output"].close()
                    node["value"] = node["filename"] # 保存结点引用一致
                # 5.2.3 清空结点
                node = {}
                # 5.2.4 读取下一行
                data = postStream.readline()
            # 5.3 结点开始，读取name filename   
            elif data.startswith(b"Content-Disposition"):
                # 5.3.1 读取name
                idxStart = data.find(b'name="')
                if idxStart != -1:
                    idxStart += 6 # 将索引移到name="之后
                    idxEnd = data.find(b'"',idxStart)
                    if idxEnd != -1:
                        node["name"] = data[idxStart:idxEnd].decode(encoding="utf-8")
                        node["value"] = ""
                # 5.3.2 读取filename
                filename = "" # 如果决定应该为假
                idxStart = data.find(b'filename="')
                if idxStart != -1:
                    idxStart += 10
                    idxEnd = data.find(b'"',idxStart)                    
                    if idxEnd != -1:
                        filename =  data[idxStart:idxEnd].decode(encoding="utf-8")
                        filename = re.sub(pattern=r"[\w\W]*\\",repl="",string=filename,flags=re.IGNORECASE)
                        filename = re.sub(pattern=r"[\W\w]*/",repl="",string=filename,flags=re.IGNORECASE)
                        node["filename"] = "" # 说明这是一个文件结点，但不一定有数据
                # 5.3.3 设置文件结点
                if filename: # 如果文件在存在的
                    # 5.3.3.1 分解扩展名
                    head,tail = os.path.splitext(filename) # 分解文件和扩展名
                    # 5.3.3.2 设置文件位置
                    fileDir = tmpDir
                    for fileType in imageTypes:
                        if fileType == tail:
                            fileDir += "image/" # 图片位置
                    for fileType in videoTypes:
                        if fileType == tail:
                            fileDir += "video/" # 视频位置
                    for fileType in attachTypes:
                        if fileType == tail:
                            fileDir += "attach/" # 附件位置
                    node["filename"] = filename
                    # 5.3.3.3 设置文件路径
                    filePath = fileDir + head + tail
                    fileNum = 0
                    while os.path.exists(filePath):
                        fileNum += 1
                        filePath = fileDir + head + "("+str(fileNum)+")" + tail
                    # 5.3.3.4 新建文件
                    node["filename"] = filePath
                    node["output"] = open(filePath,mode="wb+",buffering=1)
                # 5.3.4 过滤多出的一行，结点数据从第二行开始
                data = postStream.readline()
                if isCheck: # 写入调试文件
                    output.write(data)
                # 5.3.5 文件结点多过滤一行Content-Type: 行
                if data.startswith(b'Content-Type: '):
                    data = postStream.readline()
                    if isCheck: # 写入调试文件
                        output.write(data)
                # 5.3.6 读取正式内容，即第二行
                data = postStream.readline()   
                pass # 测试会不会不再读
            # 5.4 保存数据
            else:
                data2 = postStream.readline()
                # 5.4.1 配置数据，如果是最后一行，去掉多余的换行符
                if data2 == start or data2 == end:
                    if data.endswith(b'\r\n'):
                        data = data[:len(data)-len(b'\r\n')]
                # 5.4.2 写入文件
                if node and "filename" in node:
                    if node["filename"]:
                        node["output"].write(data)
                # 5.4.3 写入一般结点
                elif node and "name" in node and node["name"]:
                    node["value"] += data.decode(encoding="utf-8")
                # 5.4.4 转入下一行
                data = data2
        # 6 关闭调试文件
        if isCheck:
            output.close()
        self.formDicts = formDicts
        return formDicts
        formDicts = {"ss":"tt"}
        pass
    ##################################################
    # 2 demo 演示
    ##################################################
    def getDemo(self):
        html = """
        <form method=post enctype=multipart/form-data action=%s?demo=form>
          登录帐号：<input type=text name=account value="aa" /><br>
          登录密码：<input type=text name=password value ="ss" /><br>
          个人头像：<input type=file name=ico /><br>
          再输一次：<input type=text name=password value="dd" /><br>
          提示问题：<input type=text name=ask value="ff" /><br>
          提示答案：<input type=text name=answer value="gg" /><br>
          文本:<textarea name=txt style=width:300px;height:300px;>text\r\n</textarea><br>
          <input type=submit value=提交 />
          <input type=reset value=清空 />
          <input type=cancel value=取消 />
        </form>
        """ % self.action
        html += '''
        %s
        ''' % self.getFormDicts(isCheck=True)
        return html 
    ##################################################
    # To get parameters from form when 
    ##################################################
    #正文开始
    # getPostDict() 获得表单中的参数
    # environ 环境变量
    # tmpDir 测试文件位置 如：tmpDir,如果不传入参数，则表示不生成中间文件
    # 例如：getPostDict(environ, "tmp/")
    def getPostDict(self,postStream = None, tmpDir = None):
        if not postStream: #如果没有传入参数，返回None
            return {}
        #读取数据
        postDict = {}
        if tmpDir: # 如果需要调试，设置了临时文件夹
            if not os.path.exists(tmpDir):
                os.makedirs(tmpDir) #创建必要的文件夹
            now = datetime.datetime.today()
            nowStr = str(now)
            output = open(tmpDir+nowStr+".txt",'wb+',10000)
        data = postStream.readline()
        start = data
        #end = b'-----------------------------11271650311059970388103151456--\r\n'
        end = start.replace(b"\r\n", b"--\r\n")
        nodeName = None
        node = None
        while data:
            if tmpDir: # 如果需要调试，设置了临时文件夹
                output.write(data)
            if data == end or data == start:
                if node and  node["bValue"]:
                    if "filename" not in node:
                        bVal = node["bValue"]
                        if bVal.endswith(b"\r\n"):
                            bVal = bVal[0:len(bVal)-len("\r\n")]
                        val = bVal.decode(encoding="utf8")
                        node["value"] = val
                # 将节点加入到字典
                if node and node["name"]:
                    if node["name"] in postDict: # 如果结点已经存在
                        if type(postDict[node["name"]]) is list:
                            postDict[node["name"]].append(node)
                        else :
                            postDict[node["name"]] = [postDict[node["name"]],node]
                    else :
                        postDict[node["name"]] = node
                node = None
            elif data.startswith(b"Content-Disposition:"):
                #获得结点名字
                idxStart = data.find(b"name=\"")
                if idxStart != -1 :
                    idxStart += 5
                    idxEnd = data.find(b"\"",idxStart+1)
                    if idxEnd != -1 :
                        nodeName = data[idxStart+1:idxEnd].decode(encoding="utf-8")                    
                        node = {}
                        node["name"] = nodeName
                #获得文件名字
                idxStart = data.find(b"filename=\"")
                if idxStart != -1 :
                    idxStart += 9
                    idxEnd = data.find(b"\"",idxStart+1)
                    if idxEnd != -1 :
                        if not nodeName : # 如果没有定义名字，则返回错误信息
                            postDict["ERROR"] = "The nodeName havenot gotten when read Content-Type"
                            break
                        fileName = data[idxStart+1:idxEnd].decode(encoding="utf-8")                     
                        node["filename"] = fileName
            elif data.startswith(b"Content-Type:") :
                #获得文件类型
                idxStart = data.find(b":")
                idxEnd = data.find(b"\r\n")
                if idxStart != -1 and idxEnd != -1 :
                    node["content_type"] = data[idxStart+2:idxEnd].decode(encoding="utf-8")
                else :
                    postDict["ERROR"] = "The Content-Type cannot get idxStart=%s,idxEnd=%s." % (idxStart,idxEnd)
                    break
            else : # 获得变量值
                if not nodeName : # 如果没有定义名字，则返回错误信息
                    postDict["ERROR"] = "The nodeName havenot gotten content"
                    break
                if "bValue" not in node:
                    node["bValue"] = b""
                    # 去除第一行的空行
                    data = postStream.readline()
                node["bValue"] += data
            data = postStream.readline()
        #/while
        if tmpDir: # 如果需要调试，设置了临时文件夹
            output.close()
        # 恢复environ["wsgi.input"]
        return postDict
        
    # demo() 演示方法
    # environ 环境变量
    # tmpDir 测试文件位置 如：tmpDir,如果不传入参数，则表示不生成中间文件
    # action post的页面，没有实际意义
    # 例如：demo(environ,"tmp/","index.py")
    def getDemoHtml(self,environ = None, tmpDir = None, action = "index.py"):
        demoHtml = """
        <form method=post enctype=multipart/form-data action=%s>
          登录帐号：<input type=text name=account value="aa" /><br>
          登录密码：<input type=text name=password value ="ss" /><br>
          个人头像：<input type=file name=ico /><br>
          再输一次：<input type=text name=password value="dd" /><br>
          提示问题：<input type=text name=ask value="ff" /><br>
          提示答案：<input type=text name=answer value="gg" /><br>
          <input type=submit value=提交 />
          <input type=reset value=清空 />
          <input type=cancel value=取消 />
        </form>
        """ % action
        postDict = getPostDict(environ,tmpDir)
        if postDict:
            multiKeys = postDict.keys()
            multivalues = postDict.values()
            for val in multivalues:
                if type(val) is list:
                    for node in val:
                        demoHtml += "name:" + str(node["name"]) + "<br>"
                        if "filename" in node:
                            demoHtml += "filename:" + str(node["filename"]) + "<br>"
                        if "filename" in node and tmpDir: # 如果上传文件，且设置了临时文件夹
                            if not os.path.exists(tmpDir):
                                os.mkdirs(tmpDir) # 创建必要的文件夹
                            now = datetime.datetime.today()
                            nowStr = str(now)
                            head,tail = os.path.splitext(node["filename"])
                            output = open(tmpDir+nowStr+tail,"wb+",10000)
                            output.write(node["bValue"])
                            output.close()
                        if "value" in node:
                            demoHtml += "value:" + str(node["value"]) + "<br>"
                        if "content_type" in node:
                            demoHtml += "content-type:" + str(node["content_type"]) + "<br>"
                else :    
                    demoHtml += "name:" + str(val["name"]) + "<br>"
                    if "filename" in val:
                        demoHtml += "filename:" + str(val["filename"]) + "<br>"
                    if "filename" in val and tmpDir: # 如果上传文件，且设置了临时文件夹
                        if not os.path.exists(tmpDir):
                            os.mkdirs(tmpDir) # 创建必要的文件夹
                        now = datetime.datetime.today()
                        nowStr = str(now)
                        head,tail = os.path.splitext(val["filename"])
                        output = open(tmpDir+nowStr+tail,"wb+",10000)
                        output.write(val["bValue"])
                        output.close()
                    if "value" in val:
                        demoHtml += "value:" + str(val["value"]) + "<br>"
                    if "content_type" in val:
                        demoHtml += "content-type:" + str(val["content_type"]) + "<br>"
        return demoHtml

    ##################################################
    # To get parameters in the URL
    ##################################################
    # 显示环境
    # 获得地址栏参数
    def getUrlDict(self):
        urlString = self.environ["QUERY_STRING"]
        if not urlString:
            return {}
        remainingString = urlString
        queryData = {}
        idxStart = None
        idxEnd = None
        queryName = None
        nodeString = None
        nodeName = None
        nodeValue = None
        while remainingString : # 仍然有参数待读取
            idxStart = 0
            idxEnd = remainingString.find("&")
            if idxEnd != -1 :
                nodeString = remainingString[idxStart:idxEnd]
                remainingString = remainingString[idxEnd+1:]
            else :
                nodeString = remainingString
                remainingString = ""
            if nodeString :
                idxNameEnd = nodeString.find("=")
                if idxNameEnd != -1 :
                    nodeName = nodeString[idxStart:idxNameEnd]
                    nodeValue = nodeString[idxNameEnd+1:]
                else :
                    nodeName = nodeString
                    nodeValue = ""
            if nodeName in queryData : # 参数名字已经存在
                if type(queryData[nodeName]) is list : # 如果已经是列表，直接加入
                    queryData[nodeName].append(nodeValue)
                else : # 不是列表
                    queryData[nodeName] = [queryData[nodeName], nodeValue] # 转化成列表数组            
            else : # 参数是新的
                queryData[nodeName] = nodeValue
        return queryData
                
                
        

    
