

class test1():
    age = 10
    def __init__(self):
        self.name = "xx"
    def fun(self):
        print(self.age)

cc=test1()
a=dir(cc)
print(a)

print(cc.__dict__)