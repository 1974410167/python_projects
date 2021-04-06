
import time

def fun(f):

    def res(*args,**kwargs):

        sign = kwargs.get("sign")
        if sign == True:

            p_time = time.time()
            print(f"start_time:{p_time}")

            f(*args,**kwargs)

            l_time = time.time()
            print(f"end_time:{l_time}")
        else:
            p_time = time.localtime()
            print(f"start_time:{p_time}")

            f(*args, **kwargs)

            l_time = time.localtime()
            print(f"end_time:{l_time}")
    return res

@fun
def fun1(sign):

    print("hello world!")

s = fun1(True)
print(s)