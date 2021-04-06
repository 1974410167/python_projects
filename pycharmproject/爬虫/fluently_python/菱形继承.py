
class a:
    def __init__(self,name):
        self.name=name
    def aa(self):
        print(f"{self.name}")
class b:
    def __init__(self,age):
        self.age=age
    def bb(self):
        print(f"{self.age}")

class c(a,b):
    print(a)

d=c("name")
print(d.cc())

