import requests
from lxml import etree
import threading
import time

headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
url1='https://www.adw98.com/xiazai/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1-'
url2='.html'
# thread_nums=20
#
# for n in range(1,10):
#     url=url1+str(n)+url2
#     r = requests.get(url,headers)
#     html = etree.HTML(r.text)
#     a = html.xpath('//div[@id="tpl-img-content"]//li//a/@href')
#     for i in a:
#         print(i)
















# url='https://www.adw98.com/xiazai/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1-1.html'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
# }
#
# r=requests.get(url,headers)
#
# html=etree.HTML(r.text)
#
# a=html.xpath('//div[@id="tpl-img-content"]//li//a/@href')
#
# print(type(a))
# print(len(a))
# for i in a:
#     print(i)
# print(r.status_code)
