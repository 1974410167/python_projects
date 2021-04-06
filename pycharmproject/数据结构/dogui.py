



def a(n):
    if n<=2:
        return n
    return a(n-1)+a(n-2)

def b(n):
    if n==1:
        return 1
    return n*b(n-1)

print(b(5))
