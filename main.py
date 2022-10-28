class Mytry:

    def __init__(self, a, aname):
        self.name = aname
        self.a = a

    def print_obj(self):
        print(self.name, self.a)

obj = Mytry(aname="lol", a=3)
Mytry.print_obj(object)