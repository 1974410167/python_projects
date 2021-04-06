import requests
from lxml import etree
from concurrent.futures import as_completed,thread,ThreadPoolExecutor

url="http://zk8.malped.com/sscplay.php?u=?m=vod-detail-id-43646.html"

headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Cookie":"XSRF-TOKEN=eyJpdiI6IklTcXd5S2RjSlk3Q1c1RlpuZmtqTEE9PSIsInZhbHVlIjoiUFBLZlpHZnVQdnhPUjR5OGpOOWNyclFQKzJwSXZ0MTJmVWtqOEFxRVRsaDFna1pZbHJoc3I2S3FhbHJHdFJKRCIsIm1hYyI6ImY3NGRhZTQxMDZhMDg1N2NmZWIzNWMxM2RhYjMzNDBkOWJlMmQxY2Y2ZjMwMzQ3NDZjNjgyY2EyY2M3ODE4MWYifQ%3D%3D; laravel_session=eyJpdiI6Ik5kQllKaSs1dnVJeUtmTGo2SDBveEE9PSIsInZhbHVlIjoiTXlwWkNpaUdGYlFUWTUzZVRIdzNyd1BWZkpmWEJvRFRDWjYwaFJZdFZvdWhxRUE1Y0hXUUhOR3BpT1RUdnhoMiIsIm1hYyI6IjU1YjYyMDBiYzFkNGU4OWMwODRjMmE4MDZhY2U2ZDk5YmMzNjE0OWU5N2YzMjEzYWEwNmVmNjAwNWI4NDU5MTQifQ%3D%3D",
}
nums=[]
r=requests.get(url,headers = headers)
html = etree.HTML(r.text)
a = html.xpath("//div[@class='panel-body vido']//a/@href")
for i in a:
    nums.append(i)
print(len(nums))

def down_url(j):
    r1=requests.get(dict[j],headers=headers)
    cc=".txt"
    with open("D://庆余年全集//"+j+cc,'wb') as f:
        f.write(r1.content)
n=1
dict={}
while n<=46:
    strr = "第"+str(n)+"集"
    dict[strr]=nums[n-1]
    n += 1
print(dict)
with ThreadPoolExecutor(max_workers=10) as pool:

    results = pool.map(down_url, dict)

    print("进入队列一个")
    for mm in results:
        print(mm)



