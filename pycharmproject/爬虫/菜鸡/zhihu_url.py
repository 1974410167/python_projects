import requests
from bs4 import BeautifulSoup
url="https://www.zhihu.com/hot"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Cookie":'_zap=a2192c7a-a205-4579-be31-a93cd3609fe5; d_c0="ALDYpkFozxCPTnmA7UjC5hjzMpHheWxl5RM=|1581576771"; _xsrf=ciUev31457adTNHbLQGPnvlLtHm8cGhg; capsion_ticket="2|1:0|10:1581656199|14:capsion_ticket|44:OTRmY2ZhMzdjMjQ4NGZhZTk3NWVhMzZjYmUyZjM1MjI=|1e05102e5649a7db1a845e150beb55ff515c55bb859c39dfb87a477d5cbcaf0d"; z_c0="2|1:0|10:1581656225|4:z_c0|92:Mi4xT3p3YUJ3QUFBQUFBc05pbVFXalBFQ2NBQUFDRUFsVk5vYlZ0WGdDdVV2Q2g0Nkw4UDNDUU1kSkp4b0ExTGVud1JB|9b93db97b55653ab86e9b7c167d33d86cf81e123d54ad11ef6fd9d0551f1e5ad"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581742737,1581847825,1581943316,1582035805; tst=h; tshl=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1582038641; KLBRSID=ca494ee5d16b14b649673c122ff27291|1582038670|1582035802',
}
#获取txt
r=requests.get(url,headers=headers)
#用两个参数初始化soup
soup=BeautifulSoup(r.text,"lxml")
#获取title
c=soup.find_all(attrs={"class":"HotItem-title"})
#获取title的url
d=soup.select("a")

def geturl(d):
    list=[]
    for i in d:
        if type(i.get("href"))==str and len(i.get("href"))>35:
            if i.get("href") not in list:
                list.append(i.get("href"))
    return list
def gettitle(c,list):
    n=0
    for i in c:
        n=n+1
        with open("zhihu.txt","a",encoding="utf-8") as g:
            g.write("{0}.{1}".format(n,i.string))
            g.write("-----{0}".format(list[n-1]))
            g.write("\n")
#soup.prettify()格式化输出html
print(soup.prettify())
if __name__=="__main__":
    list=geturl(d)
    gettitle(c,list)