# This file contains the WSGI configuration required to serve up your
# web application at http://ilvbobing.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://help.pythonanywhere.com/pages/DebuggingImportError

# +++++++++++ CUSTOM WSGI +++++++++++
# If you have a WSGI file that you want to serve using PythonAnywhere, perhaps
# in your home directory under version control, then use something like this:
#
import sys
#
#path = '/home/ilvbobing/path/to/my/app
path ='/home/ilvbobing/ilv_web/lib'
if path not in sys.path:
    sys.path.append(path)
#
#from my_wsgi_file import application  # noqa
# import ilv.MyData
import ilv.Base
import ilv.User
import ilv.News
import ilv.Demo # 演示类
import ilv.Env # 环境类，必须引用，保持数据一致，因为getFormDict只能引用一次，之后就无效了。
import ilv.Column

# +++++++++++ HELLO WORLD +++++++++++
# A little pure-wsgi hello world we've cooked up, just
# to prove everything works.  You should delete this
# code to get your own working.


HELLO_WORLD = """<html>
<head>
    <title>PythonAnywhere hosted web application</title>
</head>
<body>
<h1>Hello, World2!</h1>
<p>
    This is the default welcome page for a
    <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>
    hosted web application.
</p>
<p>
    Find out more about how to configure your own web application
    by visiting the <a href="https://www.pythonanywhere.com/web_app_setup/">web app setup</a> page
</p>
</body>
</html>"""

'''
def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = HELLO_WORLD
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')
'''
###################################################################################################
# The entrance of uWSGI
###################################################################################################
def  application(environ,start_response):
    ###################################################################################################
    # 基本参数
    ###################################################################################################
    env = ilv.Env.Env(environ=environ)
    base = ilv.Base.Base(env=env)
    urlDict = base.urlDict
    ###################################################################################################
    # 获得参数集
    ###################################################################################################
    urlDict = base.urlDict
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
    #bHtml = b"" + response_body.encode(encoding="utf-8")
    bHtml = response_body # 不再使用二进制流
    response_headers = [("Content-Type","text/html"),("Content-Length",str(len(bHtml))),("charset","utf-8"),("Set-Cookie","session=12345")]
    start_response(status,response_headers)
    yield bHtml.encode('utf8')
    #return bHtml


# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.

# +++++++++++ VIRTUALENV +++++++++++
# If you want to use a virtualenv, set its path on the web app setup tab.
# Then come back here and import your application object as per the
# instructions below




# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/ilvbobing/mysite/mysite/settings.py'
## and your manage.py is is at '/home/ilvbobing/mysite/manage.py'
#path = '/home/ilvbobing/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()



# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
#import sys
#
## The "/home/ilvbobing" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/ilvbobing/myproject"
#path = '/home/ilvbobing/path/to/flask_app_directory'
#if path not in sys.path:
#    sys.path.append(path)
#
#from main_flask_app_file import app as application  # noqa
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.

