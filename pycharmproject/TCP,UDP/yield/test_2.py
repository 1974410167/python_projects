



r=open('C:/Users/19744/Desktop/pet.txt','r',encoding='utf-8')

print(type(r))
print(r)
print('-----------------')
r1=open('test_2_1.txt','w')

r.seek(40,0)
print(type(r))
print(r)
print('------------------')
a=r.read()

# b=r1.write(a)

print(a)

print(type(a))

#a=r1.write()

r1.close()
r.close()
