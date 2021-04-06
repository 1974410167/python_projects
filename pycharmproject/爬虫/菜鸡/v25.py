"""
中文编码
"""
import re

a=re.compile(r"[\u4e00-\u9fa5]+")
b="浩源，人俊"
m=a.findall(b)
print(m)
