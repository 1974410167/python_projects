from urllib import request
"""
使用urllib.request请求一个网页内容，并把内容打印出来
"""
if __name__=="__main__":
    url="https://movie.douban.com/top250"
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)

    #把返回结果读取出来
    #读取出来的内容类型为bytes
    html=rsp.read()
    #print(html)

    #如果要把bytes内容转换成字符串，需要解码
    html=html.decode()
    print(html)


