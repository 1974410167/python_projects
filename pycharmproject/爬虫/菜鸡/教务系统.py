import hashlib

data = 'HYuan.5637'

s = '95d1322e-042d-4bf1-ab4d-c93cb49688b8-'

sh = hashlib.sha1()
data = data+s

sh.update(data.encode('utf-8'))

print(sh.hexdigest())
print(len(sh.hexdigest()))

sss = '6d7be41b4570c09b37072def5c421ab652bf3083'

print()
print(len(sss))