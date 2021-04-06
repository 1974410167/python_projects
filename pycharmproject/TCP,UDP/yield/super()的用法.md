---

title: super()的用法

tags: 
- Python语法

categories:
- 类

---

本来很多教程,博客已经把这件事说的很清楚了，但总感觉自己不解释一边不踏实(笑哭)

- super()多用于钻石继承问题

如下代码，D继承B,C。B,C又同时继承A
 
'''
    
    class A:
        def m(self):
            print("m of A called")
    
    class B(A):
        def m(self):
            print("m of B called")
            A.m(self)
        
    class C(A):
        def m(self):
            print("m of C called")
            A.m(self)
    
    class D(B,C):
        def m(self):
            print("m of D called")
            B.m(self)
            C.m(self)
'''

此时若调用D().m(),输出如下       
'''

    m of D called
    m of B called
    m of A called
    m of C called
    m of A called
'''     
那么如何避免A.m被执行两次呢      

用super()     
'''

    class A(object):
        def m(self):
            print("m of A called")
    
    class B(A):
        def m(self):
            print("m of B called")
            super().m()
        
    class C(A):
        def m(self):
            print("m of C called")
            super().m()
    
    class D(B,C):
        def m(self):
            print("m of D called")
            super().m()
'''     
此时调用D的m方法输出
'''

    m of D called
    m of B called
    m of C called
    m of A called
'''

那么super()是如何避免某个方法被多次执行呢

其实super()本质是个类，内部记录着MRO(Method Resolution Order)信息,
由于C3算法(基本思想时在避免同一类被调用多次的前提下，使用广度优先和从左到右的原则去寻找需要的属性和方法)确保同一个类只会被搜寻一次，这样就避免了顶层父类中的方法被多次执行了


- super()可以避免直接在使用父类的名字     
如     
'''

    class A:
     def m(self):
      print('A')
     
    class B:
     def m(self):
      print('B')
     
    class C(A):
     def m(self):
      print('C')
      super().m()
     
'''    
如果要改变子类继承的父类(由A改为B)，只需一行代码(class(A):-->class(B):)，而不是在class C的大量代码中去查找,修改基类名。另外一方面代码的可移植性和重用性也更高


### super()用法

- 如果子类(Puple)继承父类(Person)不做初始化，那么会自动继承父类(Person)属性name。   
- 如果子类(Puple_Init)继承父类(Person)做了初始化，且不调用super初始化父类构造函数，那么子类(Puple_Init)不会自动继承父类的属性(name)。    
- 如果子类(Puple_super)继承父类(Person)做了初始化，且调用了super初始化了父类的构造函数，那么子类(Puple_Super)也会继承父类的(name)属性   

如    
'''


    import requests
    class Person(object):
        def __init__(self,name = "person"):
            self.name = name
     
    class Pupel(Person):  # 不做初始化 会自动继承父类属性 name
        pass
     
    class Puple_init(Person):  # 做初始化  且不调用super初始化父类构造函数 不会继承父类属性 name
        def __init__(self,age):
            self.age = age
     
    class Puple_super(Person):  # 做初始化  也调用super().__init__(name)初始化父类构造函数  会继承父类属性 name
        def __init__(self,name,age):
            self.age = age
            super().__init__(name)
     
    pp = Pupel()
    pp_i = Puple_init(10)
    pp_s = Puple_super("supder_person", 10)



'''