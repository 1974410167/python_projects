import json
a = open('课程.json',"r")
s = a.read()

ss = json.dumps(s)
t = ss.split('},')
for i in t:
    print(i)
a.close()