"""
访问一个网址
更改自己的UserAgent进行伪装
"""
from urllib import request,error
if __name__=="__main__":
    url="https://www.baidu.com"
    try:
        headers={}
        headers['User-Agent']="Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
        #第一种设置UA方式，用add_header
        req=request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
        #第二种设置UA方式，直接在Request类里面
        #req=request.Request(url,headers=headers)
        # 正常访问
        rep=request.urlopen(req)
        html=rep.read().decode("utf-8")
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    print("DOWN>.....")
