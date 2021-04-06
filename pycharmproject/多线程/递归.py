class AbC():
    def v(a):
        print(f'my name is {a}')

class Digui():
    def dd(self,n):
        if n==1:
            return 1
        return n * self.dd(n-1)

a=Digui()
x=a.dd(7)
print(x)