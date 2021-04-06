

class a():

    def __init__(self):
        self.age = 19

    def name(self):
        print("name")


s = a()
q = s.__dict__
print(q)