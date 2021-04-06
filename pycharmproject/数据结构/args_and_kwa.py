def a(*args,**kwargs):
    for i in args:
        print(i)
    for j in kwargs:
        print(kwargs.get(j))
    print(type(kwargs))
    return args

c=1

print(repr(c))

print(repr(a))


print(a.__doc__)