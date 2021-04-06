

class fun1():

    instance = None
    def __new__(cls, *args, **kwargs):

        if not cls.instance:
            cls.instance = object.__new__(cls,*args,**kwargs)

        return cls.instance

    def __init__(self):
        self.name = 'sss'

    def f1(self):
        return self.name

s = fun1()

print(id(s))

s1 = fun1()

print(id(s1))
