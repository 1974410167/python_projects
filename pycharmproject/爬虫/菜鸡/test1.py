import requests
from lxml import etree
from urllib import error
from concurrent.futures import as_completed,thread,ThreadPoolExecutor

"""
url1="https://www.933cf.com/xiazai/39543.html"
xpath1="/html/body/div[@class='maomi-content']/main[@id='main-container']/div[@class='hy-layout active clearfix']/div[@class='tab-content']/div[@id='list2']/div[@id='downlist']/div[@class='panel']/div[@id='downlist1']/table[@class='table ']/tbody/tr[2]/td[1]/input[@id='lin1k1']/@value"
r=requests.get(url1)
r.encoding="utf-8"
html=etree.HTML(r.text)
r1=html.xpath(xpath1)
print(r1[0])
"""
def g_url(i):
    url1="https://www.933cf.com/xiazai/"
    url2=".html"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    xpath1 = "/html/body/div[@class='maomi-content']/main[@id='main-container']/div[@class='hy-layout active clearfix']/div[@class='tab-content']/div[@id='list2']/div[@id='downlist']/div[@class='panel']/div[@id='downlist1']/table[@class='table ']/tbody/tr[2]/td[1]/input[@id='lin1k1']/@value"
    url=url1+str(i)+url2
    try:
        r=requests.get(url,headers=headers)
    except error.URLError as e1:
        print(e1.reason)
    except error.HTTPError as e2:
        print(e2.reason)
    else:
        html = etree.HTML(r.text)
        r1 = html.xpath(xpath1)
        if len(r1)>=0:
            for i in r1:
                print(i)
                print(f"URL请求成功！")
        else:
            print("无效URL！")
if __name__ == '__main__':
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    list1=[]
    executor=ThreadPoolExecutor(max_workers=20)
    executor.map(g_url,range(25000,40000))


