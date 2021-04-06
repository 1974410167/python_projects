import requests
from urllib import error
from lxml import etree
from bs4 import BeautifulSoup
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Cookie":'q_c1=75c0577aac734dfe97973615cf986074|1562224940|1562224940; _zap=bcc32cb5-d191-4b57-b12a-489797b88d17; _xsrf=EDKvfuiu5ljNv9MEn9jbxB4PjKbd6ocC; d_c0="AEDt0MYKrw-PThEo5Db4x5Ay6nFAy14GpGk=|1562224913"; tst=h; tshl=; q_c1=46eded4aada34fbe90557c85b663dca7|1563963885000|1563963885000; __utma=51854390.504786064.1563963883.1563963883.1563963883.1; __utmz=51854390.1563963883.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20171231=1^3=entry_date=20171231=1; tgw_l7_route=060f637cd101836814f6c53316f73463; capsion_ticket="2|1:0|10:1564906009|14:capsion_ticket|44:ZDczM2E4Y2Y2YmNiNGQxN2I5NGU0MzZlMjZiZmM5ZTA=|0f4d465eb0b3dbbf289a58287e4fe56fb6b9b410632c17e0cb33f542d84cfcd5"; z_c0="2|1:0|10:1564906043|4:z_c0|92:Mi4xT3p3YUJ3QUFBQUFBUU8zUXhncXZEeWNBQUFDRUFsVk5PaDl1WFFDZW1oYll2ODVzbDVMdi1vWW5TSWhPRlhNYlNB|d5059638984096cea5bc6330274943667859dbb5037c3beb7cad1fffdda3113d"'
}
url="https://www.zhihu.com/search?q=初中生书单"
r=requests.get(url,headers=headers)
xpath="//div//meta[@itemprop='url']/@content"
html = etree.HTML(r.text)
r1 = html.xpath(xpath)
print(type(r1))
print(r1)
soup=BeautifulSoup(r.text,"lxml")
print(soup.prettify())
