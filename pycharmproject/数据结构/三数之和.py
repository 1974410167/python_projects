from typing import Any, Union


def f(n):
    if n==1:
        return 1
    print('start:'+str(n))
    result = n*f(n-1)
    print('end:'+str(n))
    return result


c = f(3)
print(c)