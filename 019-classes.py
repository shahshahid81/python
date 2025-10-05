def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  # don't create a new local spam variable, refer spam from outside scope
        spam = "nonlocal spam"

    def do_global():
        global spam  # don't create a new local spam variable, refer spam from global scope
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):  # constructor
        self.data = []

    def f(self):
        return 'hello world'


x = MyClass()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
