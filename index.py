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
import ilv.pot
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
    
    base = ilv.pot.get_web(env=env)
    
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


