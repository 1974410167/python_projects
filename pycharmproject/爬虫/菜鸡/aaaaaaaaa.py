import requests
from lxml import etree
import threading
from urllib import error


def get_url(list):
    n=1
    for j in range(51220):
        url2="https://www.869ut.com/xiazai/"
        url=url2+str(j)+".html"
        xpth1 = "/html/body/div[@class='maomi-content']/main[@id='main-container']/div[@class='hy-layout active clearfix']/div[@class='tab-content']/div[@id='list2']/div[@id='downlist']/div[@class='panel']/div[@id='downlist1']/table[@class='table ']/tbody/tr[@class='app_hide']/td[1]/input/@value"
        try:
            r = requests.get(url, headers=headers,timeout=2)
            r.encoding = "utf-8"
            html = etree.HTML(r.text)
            r1 = html.xpath(xpth1)
            for i in r1:
                print(f"{n}.{i}请求完毕！")
                list.append(i)
                n = n + 1
        except error.ContentTooShortError as e1:
            print(e1.reason)
        except error.URLError as e2:
            print(e2.reason)
        except error.HTTPError as e3:
            print(e3.reason)
        except requests.exceptions.ReadTimeout as e4:
            print(e4)
        except requests.exceptions.ConnectTimeout as e5:
            print(e5)
def down(list):
    n1=1
    root = "D://spider_video//"
    for m in list:
        try:
            r1=requests.get(m,headers=headers)
            path = root + m.split("/")[-1]
            with open(path, "wb") as f:
                f.write(r1.content)
                print(f"写入第{n1}个文件成功!")
                n1=n1+1
        except error.ContentTooShortError as e1:
            print(e1.reason)
        except error.URLError as e2:
            print(e2.reason)
        except error.HTTPError as e3:
            print(e3.reason)
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    list = []
    get_url(list)






