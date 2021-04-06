import requests
from lxml import etree
import re
import json


def url_message(url):

    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': '*/*',
        'Cookie': 'VISITOR_INFO1_LIVE=bl4jG0T-Fc0; YSC=OK4FSA8JCkM; PREF=; GPS=1; ST-17pm9r8=itct=CBMQtSwYACITCJLFq9HPruoCFYEzYAoduuQDdzIJZy1jaGFubmVs&csn=Kdr9XsnZOYLngAO1gK-4DQ',
    }

    r = requests.get(url, headers)
    t = etree.HTML(r.text)

    xpath1 = "//meta[@property='og:title']/@content"
    xpath2 = "//meta[@property='og:description']/@content"
    result1 = t.xpath(xpath1)
    result2 = t.xpath(xpath2)

    file_name = result1[0]

    with open('D://video_res//2020.7.3//'+file_name+'.txt', 'w', encoding='utf-8') as f:
        f.write('url: ' + url + '\n')
        f.write('title: ' + result1[0] + '\n')
        f.write('description: ' + result2[0] + '\n')

url = "https://www.youtube.com/watch?v=ri5AyXzxb4o"


url_message(url)





