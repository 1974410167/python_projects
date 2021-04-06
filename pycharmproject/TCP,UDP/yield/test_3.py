import requests

url='http://a3.att.hudong.com/35/34/19300001295750130986345801104.jpg'
rr=requests.get(url)

rr.iter_content()

a=rr.headers.get('Content-Length',0)


print(a)