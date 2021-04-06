from urllib import request
if __name__=="__main__":
    url="https://qzone.qq.com/"

    rsp=request.urlopen(url)
    html=rsp.read().decode()

    with open("rsp.html","w") as f:
        f.write(html)
