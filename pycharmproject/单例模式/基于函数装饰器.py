

def f1(f):

    instance = None

    def inner(*args,**kwargs):
        nonlocal instance

        if not instance:
            instance = f(*args,**kwargs)
        return instance

    return inner

@f1
class cls():
    def __init__(self,num):
        self.num = num

c = cls(10)

c1 = cls(10)

print(id(c))
print(id(c1))