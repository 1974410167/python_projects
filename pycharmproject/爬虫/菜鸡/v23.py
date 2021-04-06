import requests
baseurl="http://fanyi.baidu.com/sug"

data={
    "kw":'girl'
}
headers={
    #使用post,至少应该包含content-length字段
    "Content-Length":"len(data))"
}
req=requests.post(baseurl,data=data,headers=headers)
print(req.text)



