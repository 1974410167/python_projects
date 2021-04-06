import threading
import queue
import time
import requests
import lxml
from bs4 import BeautifulSoup
from urllib import error
"""
url="https://www.69aud.com/xiazai/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
r=requests.get(url,timeout=3)
r.encoding="utf-8"
soup=BeautifulSoup(r.text,"lxml")
a=soup.select("tbody tr td a")
for i in a:
    print(i.get("href"))
print(r.text)
"""

def geturl(q):
    n=0
    for i in range(30000,50000):
        url = "https://www.69aud.com/xiazai/"
        url=url+str(i)+".html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        try:
            r = requests.get(url, timeout=3,headers=headers)
        except error.HTTPError as e1:
            print(e1.reason)
        except error.URLError as e2:
            print(e2.reason)
        else:
            if r.status_code==200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, "lxml")
                a = soup.select("tbody tr td a")
                for j in a:
                    q.put(j.get("href"))
                    n=n+1
                    print(f"成功入队第{n}个！")
def down_url(q):
    x=0
    root = "D://yellow_video//"
    while not q.empty():
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        m=q.get()
        r2=requests.get(m,headers=headers)
        path = root + m.split("/")[-1]
        with open(path, "wb") as f:
            x=x+1
            print(f"第{x}个正在下载中......")
            f.write(r2.content)
            print(f"第{x}个下载完毕！")
if __name__ == '__main__':
    q = queue.Queue()
    geturl(q)
    down_url(q)










