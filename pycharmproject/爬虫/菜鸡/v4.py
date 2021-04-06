from  urllib import request,parse
"""
掌握对url进行参数编码的方法
需要使用parse模块
"""
if __name__=="__main__":
    url="https://www.baidu.com/s?"
    wd=input("Input your keyword:")
    #要用data,需要使用字典结构
    qs={
        "wd":wd
    }
    #转换url编码
    qs=parse.urlencode(qs)

    #完整的url
    fullurl = url + qs
    #打开url
    rsp=request.urlopen(fullurl)
    html=rsp.read()
    #对html解码
    html=html.decode()
    print(html)


