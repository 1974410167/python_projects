import requests
from lxml import etree
import json

'''

dict={"a":"aa","b":"bb"}

dict1=str(dict)
print(dict1)

print(type(dict1))

print(dict.values())

for i in dict.values():
    print(i)
    print(type(i))
if "a"  in dict:
    del dict["a"]
print("bb" in dict.values())
print(dict)
print(len(dict))

'''


headers={
#"Accept": "*/*",
#"Accept-Encoding": "gzip, deflate",
#"Accept-Language": "zh-CN,zh;q=0.9",
#"Connection": "keep-alive",
#"Content-Length": "42",
#"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie":"migu_cookie_id=963b271b-fe41-4fe9-89ef-72a040d92316-n41573887195933; migu_music_status=true; migu_music_uid=0554c735-1740-4d61-8a2d-d1d6994ab957; migu_music_avatar=%252F%252Fcdnmusic.migu.cn%252Fv3%252Fstatic%252Fimg%252Fcommon%252Fheader%252Fdefault-avatar.png; migu_music_nickname=%E5%92%AA%E5%92%95%E7%94%A8%E6%88%B7; migu_music_level=0; migu_music_credit_level=1; migu_music_platinum=0; migu_music_msisdn=15738698290; migu_music_email=; migu_music_passid=6101841419911; migu_music_sid=s%3AOP0G6tpomnLQRRPBpMFi5HfBbpkUPBJa.KGK3V99pOiFwXkmT5Uwm%2FSWXtKWn2HbJoYTnxvSdXMg; WT_FPC=id=2c2cd0d12fa075a03851573887196501:lv=1574068783604:ss=1574068783604; WT_FPC=id=2c2cd0d12fa075a03851573887196501:lv=1574068784112:ss=1574068777822",
#"Host": "music.migu.cn",
#"Origin": "http://music.migu.cn",
#"Referer": "http://music.migu.cn/v3/music/order/download/60054701923",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
#"X-Requested-With": "XMLHttpRequest",
}


url="http://music.migu.cn/v3/music/artist/112/song?page=2"

Xpth2 = "//a[@data-type='song-name-txt']/@title"

Xpth1 = "//a[@data-type='crbt']/@data-id"



r=requests.get(url,headers=headers)

heml=etree.HTML(r.text)

a=heml.xpath(Xpth1)

print(a)
print(len(a))
print(type(a))

