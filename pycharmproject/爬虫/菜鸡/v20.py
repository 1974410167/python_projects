from urllib import request
import json
url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20"
rsp=request.urlopen(url)
data=rsp.read().decode()
data=json.loads(data)
print(data)