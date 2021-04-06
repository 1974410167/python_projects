import requests
url="http://www.baidu.com"
kw={
    "kw":"土豆"
}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
rsp=requests.get(url,params=kw,headers=headers)
print(rsp.text)
