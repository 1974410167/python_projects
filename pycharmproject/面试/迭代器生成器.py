

def it(f):
    isinstance = None

    def c(*args,**kwargs):
        nonlocal isinstance
        if isinstance:
            return isinstance
        else:
            isinstance = f(*args,**kwargs)
            return isinstance
    return c
@it
class a():
    def __init__(self):
        pass

x = a()
print(id(x))

qq = a()
print(id(qq))