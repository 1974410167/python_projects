import requests
import re
url="https://www.zhihu.com/question/342727398"
headers={
    "Cookie":'_zap=a2192c7a-a205-4579-be31-a93cd3609fe5; d_c0="ALDYpkFozxCPTnmA7UjC5hjzMpHheWxl5RM=|1581576771"; _xsrf=ciUev31457adTNHbLQGPnvlLtHm8cGhg; capsion_ticket="2|1:0|10:1581656199|14:capsion_ticket|44:OTRmY2ZhMzdjMjQ4NGZhZTk3NWVhMzZjYmUyZjM1MjI=|1e05102e5649a7db1a845e150beb55ff515c55bb859c39dfb87a477d5cbcaf0d"; z_c0="2|1:0|10:1581656225|4:z_c0|92:Mi4xT3p3YUJ3QUFBQUFBc05pbVFXalBFQ2NBQUFDRUFsVk5vYlZ0WGdDdVV2Q2g0Nkw4UDNDUU1kSkp4b0ExTGVud1JB|9b93db97b55653ab86e9b7c167d33d86cf81e123d54ad11ef6fd9d0551f1e5ad"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581742737,1581847825,1581943316,1582035805; tst=h; tshl=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1582038641; KLBRSID=ca494ee5d16b14b649673c122ff27291|1582038670|1582035802',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
}
r=requests.get(url,headers=headers)

print(r.text)
# pattern = re.compile('《(.*?)》')
# a=pattern.findall(r.text)
# dict={}
# for i in a:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# b=sorted(dict.items(),key=lambda item:item[1],reverse=True)
# for j in b:
#     with open("top__movies.txt","a",encoding="utf-8") as f:
#         f.write(str(j)+"\n")
