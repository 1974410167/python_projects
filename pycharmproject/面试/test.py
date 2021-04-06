

n = 0

def fn1():
    global n
    print(n)

def fn2():
    global n
    n += 9
    print(n)

def main():

    fn2()
    fn1()

main()
print(n)