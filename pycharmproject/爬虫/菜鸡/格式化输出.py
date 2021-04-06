


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(f"{self.name} is eat")
    def sleep(self):
        print(f"{self.name} is sleep")

class dog1(Dog):
    name="ss"
    def __init__(self,scoure):
        self.scoure=scoure

    def play(self):
        print(self.name + " is paly")


a=dog1("ss")
b=[1,3,4]
c=[2,33,44]
for i in zip(b,c):
    print(i)