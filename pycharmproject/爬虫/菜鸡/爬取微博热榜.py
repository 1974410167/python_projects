import requests
from lxml import etree
url="https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"
r=requests.get(url)
r.encoding="utf-8"
print(r.text)
html=etree.HTML(r.text)
n=0
for index in range(1,52):
    a="/html/body[@class='wbs-hotrank']/div[@class='m-main']/div[@id='plc_main']/div[@id='pl_top_realtimehot']/table/tbody/tr["+str(index)+"]/td[@class='td-02']/a/text()"
    r1=html.xpath(a)
    print(f"{n}.{r1[0]}")
    n=n+1





