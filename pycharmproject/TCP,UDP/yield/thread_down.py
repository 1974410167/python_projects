
## 这是一个基于threading的下载器,支持断点续传。

import threading
import requests
import os
from urllib import error

class MyTherding():
    def __init__(self,url,location):
        self.url = url
        self.location = location
        self.num_th = 10
        self.headers={
            'Accept':"*/*",
            'Connection':'keep-alive',
            'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 Edg/79.0.309.47',
        }

    def file_size(self):
        try:
            r=requests.get(self.url,headers=self.headers)
        except (error.HTTPError,error.URLError,error.ContentTooShortError) as f:
            return f.reason
        else:
            file_len=r.headers.get('Content-Length')
            return file_len

    def one_file(self):

        current_part_size = self.file_size() // self.num_th + 1

        return current_part_size

class Down_file(MyTherding):

        def down_file(self):

            for j in range(self.num_th):

            r=requests.get(url)
            with open(self.location,'ab',) as f:
                f.write(r.content)
                print('successful!!!')


if __name__=='__main__':

    for i in range(MyTherding.num_th):
        t=threading.Thread(target=Down_file.down_file())
        t.start()

url='http://b.hiphotos.baidu.com/image/h%3D300/sign=92afee66fd36afc3110c39658318eb85/908fa0ec08fa513db777cf78376d55fbb3fbd9b3.jpg'
locla='D:/pycharm/pycharmproject/TCP,UDP/yield/picture/aa.jpg'

a=Down_file(url,locla)

print(a.file_size())








