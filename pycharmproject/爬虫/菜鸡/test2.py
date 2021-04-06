

from lxml import etree

url = 'https://www.baidu.com/'
import requests

a = requests.get(url)

print(a.text)
print(a.status_code)
print(type(a.status_code))