import requests
import queue
import time
from bs4 import BeautifulSoup
import threading
def g_url(q1):
    number=0
    for i in range(46300,46391):
        if number==10:
            break
        for j in range(0,10):
            if number==10:
                break
            url = "https://www.youquba.net/xieedongtaitu/2017/1217/"
            url=url+str(i)+"_"+str(j)+".html"
            headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            }
            r=requests.get(url,headers=headers)
            r.encoding = "utf-8"
            if r.status_code==200:
                soup=BeautifulSoup(r.text,"lxml")
                b=soup.select("p a img")
                for n in b:
                    q1.put(n.get("src"))
                    number=number+1
                    print(f"获得第{number}个URL成功!")
                    if number==10:
                        break
    print(f"获取{number}个URL完毕")
def down_gif(q1):
    number2=0
    root = "D://gif//"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    while not q1.empty():
        m=q1.get()
        try:
            r1=requests.get(m,headers=headers,timeout=0.3)
        except error.URLError as e1:
            print(e1.reason)
        except error.HTTPError as e2:
            print(e2.reason)
        else:
            if r1.status_code == 200:
                path = root + m.split("/")[-1]
                with open(path, "wb") as f:
                    f.write(r1.content)
                    number2=number2+1
                    print(f"写入第{number2}个文件成功!")
if __name__=="__main__":
    q1=queue.Queue()
    t1=threading.Thread(target=g_url,args=(q1,))
    t2=threading.Thread(target=down_gif,args=(q1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
