import urllib
import chardet
from urllib import request
if __name__=="__main__":
    url="https://movie.douban.com/top250"
    rsp=urllib.request.urlopen(url)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    html=rsp.read()
    html=html.decode()

    #print(html)