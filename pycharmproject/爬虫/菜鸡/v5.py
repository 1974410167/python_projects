"""
利用parse模块模拟post请求
分 2.尝试输入单词girl,发现每敲一个字母后都有请求
    3.请求地址是 http://fanyi.baidu.com/sug
    4.利用NetWork-All-Hearders,查看发现FormData的值是kw:girl
    5.检查返回内容格式，发现返回的是json格式内容==》需用json包
大致流程是：
    1.利用data构造内容，然后urlopen打开
    2.返回一个json格式的结果
    3.结果应该就是girl的释义
"""
from urllib import request,parse
import json

baseurl='http://fanyi.baidu.com/sug'

data={
    "kw":'girl'
}

#对data进行编码
data=parse.urlencode(data)
f=baseurl+data
#发出请求
rsp=request.urlopen(f)
#解码
json_data=rsp.read()
print(json_data)


#data=json.loads(json_data)
#print(data)




