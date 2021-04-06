import requests
from bs4 import BeautifulSoup
def get_url():
    list1=[]
    for k in range(1,321):
        url = "http://www.umei.cc/meinvtupian/"
        url=url+str(k)+".htm"
        list1.append(url)
    return list1
def get_picture(list1):
    list2=[]
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    }
    for i in list1:
        r = requests.get(i, headers=headers,verify=False)
        soup = BeautifulSoup(r.text, "lxml")
        get_ima= soup.select("img")
        for j in get_ima:
            list2.append(j.get("src"))
    return list2
def down_picture(list2,c):
    root="D://picture//"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    }
    for j in list2:
        c=c-1
        if c==1:
            break
        path=root+j.split("/")[-1]
        r2=requests.get(j,headers=headers)
        with open(path,"wb") as f:
            f.write(r2.content)
if __name__=="__main__":
     c=input("Please enter the quantity you want: ")
     c=int(c)
     a=get_url()
     b=get_picture(a)
     down_picture(b,c)



