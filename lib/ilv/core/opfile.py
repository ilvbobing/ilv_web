#!/usr/local/env python3.3
#-*-code:utf8-*-

"""file administrator of file and directory(s)

The full import path of this module is ilv.file
Programs that import and use 'file' stand a better chance of bening
portable between different platforms. Of course,they must then only use
functions that are defined by all paltforms (e.g.,unlink and opendir),
and leave all path name manipulation to ilv.path(e.g.,split and join).

"""

# Note: more names are added to __all__ later.
__all__ = []

import os
########################################################################
# ilv.core.file.File
# 单个文件操作类
########################################################################
class Opfile:
    """File manipulate files
    
    This class 
    
    """
    dir_static = None # 静态文件地址
    plat = None # 运行平台
    mode = None # 风格
    
    #*******************************************************************
    # 1 ilv.core.htm.Htm.__init__()构造函数
    # dir_static 静态文件位置
    # plat 代码平台
    # mode 用户模式
    #*******************************************************************
    def __init__(self, dir_static="static/", plat="core", mode="default"):
        self.dir_static = dir_static
        self.plat = plat
        self.mode = mode
        pass

    #*******************************************************************
    # 1 get_path 获得指定文件路径
    # file_name 加载的文件 默认为 static/core/default/error.htm
    #*******************************************************************
    def get_path(self, file_name="error.htm"):
        path = ""
        path += self.dir_static
        path += self.plat + "/"
        path += self.mode + "/"
        if os.path.exists(path+file_name):
            path += file_name
            return path
            pass
        # 从static/core/default/下寻找
        path = ""
        path += self.dir_static
        path += self.plat + "/"
        path += "default/"
        if os.path.exists(path+file_name):
            path += file_name
        else:
            path = "static/core/default/error.htm"
        return path
        pass

    ################################################################
    # 2 get_templet 获得模板文件
    # name 模板文件的名字（不含扩展名）
    # 使用时机：当我们需要读取一个模板文件时，比如head
    ################################################################
    def get_templet(self,name=None):
        html = None
        path = self.get_path(file_name=name+".html")
        if path is not None:
            output = open(path,mode='r',buffering=1)
            data = output.readline()
            while data and data.find("<!--ilv_%s-->" % name) == -1:
                data = output.readline()
            if data:
                html = data
            while data and data.find("<!--/ilv_%s-->" % name) == -1:
                data = output.readline()
                html += data
            output.close()             
        else:
            self.add_msg("ilv.core.Opfile.get_templet:name=%s"\
                         % (str(name)) )
        return html























    pass
