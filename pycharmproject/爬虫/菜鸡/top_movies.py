import re

text="阿萨飒飒<<葛浩源>>sasasa(《sadsadasd》)sasasadafas《sa》2222《1111》《sa》"
pattern = re.compile('《(.*?)》')

a=pattern.findall(text)
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
b=sorted(dict.items(),key=lambda item:item[1],reverse=True)

print(b)