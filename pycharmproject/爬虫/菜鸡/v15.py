from  urllib import request,parse
from http import cookiejar

#创建filecookiejar的实例
filename="cookie.txt"
cookie=cookiejar.MozillaCookieJar(filename)
#生成cookie的管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler=request.HTTPHandler()
#创建https管理器
https_handler=request.HTTPSHandler()
#创建请求管理器
opener=request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    """
    负责初次登陆
    需要输入用户名密码，用来获取登陆cookie凭证
    :return:
    """
    url="http://www.renren.com/PLogin.do"
    data={
        "email":"15738698290",
        "password":"wsghy.5637"
    }
    #对数据进行编码
    data=parse.urlencode(data)
    #创建一个请求对象
    req=request.Request(url,data=data.encode())
    #使用opener发起请求
    rep=opener.open(req)
    #保存cookie的文件
    #ignor_discard表示即使cookie将要被丢弃也要保存下来
    #ignore_expire表示如果该文件中的cookie即使已经过期，也要保存
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__=="__main__":
    login()