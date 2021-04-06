import time
import functools

def clock(func):

    @functools.wraps(func) #��������Դ�func���Ƶ�clocked��
    def clocked(*args,**kwargs):

        t0=time.time()
        result=func(*args,**kwargs)
        elapsed=time.time()-t0
        name= func.__name__
        arg_list =[]
        if args:
            arg_list.append(", ".join(repr(arg)for arg in args))
        if kwargs:
            pairs=["%s=%r"%(k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str=", ".join(arg_list)
        print('[%0.8fs]%s(%s)->%r'%(elapsed,name,arg_str,result))

        return result

    return clocked

def a(b):
    def c(*args):
        aa=b(*args)
        print("aaaaaaaaaaaa")
        return aa
    return c

def c(b):
    print("xxxx")
    return c


def time1(fun):

    def re_time(*args,**kwargs):
        r=fun(*args,**kwargs)
        print(time.time())

        return r
    return re_time
