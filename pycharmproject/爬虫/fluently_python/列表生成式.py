
# colors = ['black','white']
# sizes = ['S','M','L']
# # for i in ([a,b] for a in colors for b in sizes if a=='black'):
# #     print(i)
#
# a = divmod(3,4)
# print(a)
#
# list = [1,2,3,4,5,3]
# first,second,*other,last=list
# print(*other)
from collections import namedtuple

m = [1,2,3,4]

t = namedtuple("ta",'a b c d')

a = t._make(m)

print(a)

