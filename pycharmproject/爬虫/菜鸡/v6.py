"""
利用request的类Request让整个过程更简洁，功能更强大
"""
from urllib import request,parse
import json
baseurl='http://fanyi.baidu.com/sug'

data={
    "kw":'girl'
}
#对data进行编码
data=parse.urlencode(data).encode("utf-8")
headers={
    #使用post,至少应该包含content-length字段
    "Content-Length":len(data)
}
req=request.Request(url=baseurl,data=data,headers=headers)

#发出请求
rsp=request.urlopen(req)
#解码
json_data=rsp.read().decode("utf-8")
print(type(json_data))


data=json.loads(json_data)
print(data)