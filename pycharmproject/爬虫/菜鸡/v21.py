import requests
url="http://www.baidu.com"
#两种方式请求
#使用get请求
rsp=requests.get(url)
print(rsp.text)

#使用request请求
rsp=requests.request("get",url)
print(rsp.text)
