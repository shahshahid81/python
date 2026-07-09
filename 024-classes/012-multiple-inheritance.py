class Person:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = int(age)

    def say_hello(self):
        return f"I am: {self.name}, {self.age} years old."

    def __str__(self):
        return self.say_hello()


class Londoner:
    def __init__(self, area):
        self.area = area

    def say_hello(self):
        return f"I live in {self.area}."

    def __str__(self):
        return self.say_hello()


# order of the class list matters for method resolution order
#
class LondonPerson(Person, Londoner):
    def __init__(self, name, age, area):
        # super refers to person, refer the printed output of mro to understand the chain
        super().__init__(name, age)
        Londoner.__init__(self, area)


john = LondonPerson("John", 30, "Chelsea")
# mro = method resolution order
# says the order of which method to use
print(LondonPerson.__mro__)
print(vars(john))

# mro is LondonPerson, Person, Londoner and object.
# say_hello is found in Person, it uses it first
print(john.say_hello())
print(john)


class Flyable:
    def fly(self):
        return "I can fly!"


class Swimmable:
    def swim(self):
        return "I can swim!"


class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"
