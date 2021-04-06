import requests
import threading
from concurrent.futures import ThreadPoolExecutor

## 总长度
res = 0

lock = threading.Lock()

def g_url(url):
    global res

    try:
        r=requests.get(url)
        content_len = len(r.content)

        # 加锁
        lock.acquire()

        res += content_len
        # 释放锁
        lock.release()

    except:
        pass
if __name__ == '__main__':
    url_list_input = [
        "https://miro.medium.com/max/700/0*8aY8pX5CoNGImZU4.png",
        "https://img-a.udemycdn.com/course/240x135/2150122_6aae_3.jpg",
        "http://www.w3big.com/python3/python3.png",
        "http://www.w3big.com/python3/python3.png",
        "https://baidu.com/",
        "https://udemycoupons.me/wp-content/uploads/2019/11/Udemy-Coupons-Comprehensive-Python3-Bootcamp-2020-From-A-to-Expert-100-OFF-696x436.jpg"
    ]

    ## 去重
    url_list_input = set(url_list_input)

    ## 转换为list
    url_list_input = list(url_list_input)

    picture_type = ['png','jpg']

    ## 遍历，去掉不合法url
    for url in url_list_input:
        t = url.split(".")
        if t[-1] not in picture_type:
            url_list_input.remove(url)

    ## 开启20个线程
    executor=ThreadPoolExecutor(max_workers=20)
    executor.map(g_url,url_list_input)

