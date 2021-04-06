class Student(object):

    score = 60

    def run(self):
        print("跑步贼快")

    @classmethod
    def fun(cls):
        print(cls.score)
        cls().run()

    @staticmethod
    def f1():
        print('sssssss')

Student.fun()



Student.f1()
