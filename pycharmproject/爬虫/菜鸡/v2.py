import urllib
import chardet
from urllib import request
if __name__=="__main__":
    url="https://movie.douban.com/top250"
    rsp=urllib.request.urlopen(url)
    html=rsp.read()
    #利用chardet自动检测
    cs=chardet.detect(html)
    print(cs)
    #如果是"encoding"则用，否则用"utf-8"
    html=html.decode(cs.get("encoding","utf-8"))
    print(html)