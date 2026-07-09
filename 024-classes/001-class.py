class Person:
    pass


john = Person()
john.name = "John"
john.age = 30

print(john)
print(dir(john))
print(john.name, john.age)
# AttributeError: 'Person' object has no attribute 'names'
# print(john.names)
john.name = "John!"
print(john.name, john.age)


class House:
    bedrooms = 4
    doors = 16


my_house = House()
my_house_v2 = House()
print(my_house.doors)
print(my_house_v2.doors)
print(my_house, my_house_v2)

my_house.doors += 1
my_house.bedrooms -= 1
print(my_house.doors, my_house.doors)
print(my_house_v2.doors, my_house_v2.doors)


class Person:
    name = "John"
    age = 25

    def print_age(self):
        print("Called", self, self.age)

    def set_new_age(self, new_age):
        self.age = new_age


john = Person()
john_b = Person()
john.print_age()
john_b.print_age()

john.age = 100
john.print_age()
john_b.print_age()

john.set_new_age(64)
john.print_age()


#  This is a sample class which can be used as a reminder for the syntax.
class SampleClass:
    """A sample class to be used as a helper for the exercise."""

    sample_string = "Hello World!"
    sample_integer = 123


class Camera:
    focal_length = 50
    brand = "Canon"


class CodeBreaker:
    name = "Alan Turing"
    workplace = "Bletchley Park"


class FruitBowl:
    """A class to keep track of fruit in a bowl!"""

    apples = 5


my_fruitbowl = FruitBowl()
my_fruitbowl.apples = 4
my_fruitbowl.bananas = 1


class Rectangle:
    """A class to represent a rectangle, with associated methods."""

    height = 30
    width = 4

    def area(self) -> int:
        """Return the area, given the height * width attributes."""
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2
