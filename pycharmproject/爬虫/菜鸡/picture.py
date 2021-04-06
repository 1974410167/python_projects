import requests
from lxml import etree
import time
from urllib import error
from concurrent.futures import as_completed,thread,ThreadPoolExecutor
def get_url(list):
    xpath1 = "/html/body/div[@class='main']/div[@class='main_cont']/div[@class='pic_main']/div[@class='meinv-content clearfix']/div[@class='col-main']/div[@class='main-wrap']/div[@id='pic-meinv']/a/img[@class='pic-large']/@data-original"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    n=1
    for i in  range(120001,180000):
        for j in range(1,10):
            url1 = "http://www.win4000.com/meinv"
            url2 = ".html"
            url3="_"
            url=url1+str(i)+url3+str(j)+url2
            try:
                r=requests.get(url)
            except error.URLError as e1:
                print(e1.reason)
            except error.HTTPError as e2:
                print(e2.reason)
            else:
                if r.status_code==200:
                    html=etree.HTML(r.text)
                    r1=html.xpath(xpath1)
                    list.append(r1[0])
                    print(r1[0])
                    print(f"第{n}个URL请求成功!")
                    n=n+1
                    if n==1000:
                        break
        if n==1000:
            break
def down_picture(url):
    root="D://picture_threading//"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    try:
        r1=requests.get(url,headers=headers)
    except error.URLError as e1:
        print(e1.reason)
    except error.HTTPError as e2:
        print(e2.reason)
    else:
        if r1.status_code == 200:
            path = root + url.split("/")[-1]
            with open(path, "wb") as f:
                f.write(r1.content)

if __name__ == '__main__':
    start1=time.time()
    list=[]
    get_url(list)
    print(f"get_url总用时{time.time()-start1}!")
    n=0
    start2=time.time()
    for i in list:
        down_picture(i)

    executor=ThreadPoolExecutor(max_workers=5)
    executor.map(down_picture,list)
    print(f"down_picture总用时{time.time()-start2}")





























"""
xpath1="/html/body/div[@class='main']/div[@class='main_cont']/div[@class='pic_main']/div[@class='meinv-content clearfix']/div[@class='col-main']/div[@class='main-wrap']/div[@id='pic-meinv']/a/img[@class='pic-large']/@data-original"
url="http://www.win4000.com/meinv181411.html"
r=requests.get(url)
print(r.text)
html=etree.HTML(r.text)
r1=html.xpath(xpath1)
print(r1[0])
"""