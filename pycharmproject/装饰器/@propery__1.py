class Person(object):
    def __init__(self):
        self._name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age>=18:
            raise ValueError('请输入小于18的数字')
        else:
            self.__age = age


t = Person()
t.age = 12






