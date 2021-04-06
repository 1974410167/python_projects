import json
import requests
import threading
import time

with open('config.json', 'r', encoding='utf-8') as f:
    conf = json.loads(f.read())
    print('获取配置成功\n')
def request(q,i):
    print("账号%s" % q)
    url = 'http://119.45.184.80:3633/main/main.php?account=' + i[q]["account"] + "&password=" + i[q]["password"]
    print(requests.get(url).text)

def main_handler():
    for i in conf.values():
        for q in range(len(conf["users"])):
            therad = threading.Thread(target=request, args=(q,i))
            therad.start()

main_handler()