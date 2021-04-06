import re

#compile函数，用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
#group()返回符合正则的全部，group(1)返回符合正则的第一个，以此类推
s=re.compile(r'([a-z]+) ([a-z]+)')
b="hello world ge hao yuan4123"

a=s.match(b)
print(a.group())

a1=s.search(b)
print(a1)

a2=s.findall(b)
print(a2)

a3=s.finditer(b)
for i in a3:
    print(i.group())

a4=s.split(b)
print(a4)


"""
中文编码
"""


