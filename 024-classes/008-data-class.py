from dataclasses import dataclass, field

# Below syntax is invalid since name is not defined anywhere
# class Test:
#     name


# Below syntax is valid since we are saying that if name is ever created, mark it's type as string, which will store some metadata for name key
class Test:
    name: str


a = Test()
print(vars(a))


# Below syntax is normal, we are creating a class attribute here. We just pass this to data class.
# Note that dataclass creates instance attribute instead of class attribute
class Test:
    name = "Test"


a = Test()
print(vars(a))
print(a.name)


# implements init, str, repr and eq method for us
@dataclass(frozen=False)
class Person:
    # type hinting doesn' enforce types
    # Person(1, "john") will set name to 1 and age to "john"
    name: str
    age: int


john = Person("john", 25)
john_b = Person("john", 26)
# note that str and repr is implemented for us
print(john)
print(john == john_b)
john_b.age = 25
print(john == john_b)

# To avoid the below error, remove frozen or set it to false
# dataclasses.FrozenInstanceError: cannot assign to field 'age'
john.age += 4

# Below doesn't work, only the defined attributes work
john.city = "London"
print(john)


@dataclass
class Car:
    make: str
    year: str
    mileage: int = 0  # default!


car_a = Car("Honda", 2020)
print(car_a)

car_b = Car("Honda", 2020)
car_b.mileage = 1000
print(car_b)


@dataclass
class Shape:
    height: int
    width: int
    area: int = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height


a = Shape(10, 7)

# Below error occurs without post_init since we don't define area and then print which tries to access area
# AttributeError: 'Shape' object has no attribute 'area'
print(a)


@dataclass
class Dog:
    breed: str
    colour: str

    def bark(self):
        print(f"Woof! I am a {self.breed.title()}")

    def __eq__(self, other):
        return self.breed == other.breed


gromit = Dog("Beagle", "Brown")
print(gromit)
gromit.bark()
gromit_v2 = Dog("Beagle", "Biege")
print(gromit == gromit_v2)


@dataclass
class Employee:
    name: str
    role: str
    # default_factory uses the method to create a default value
    skills: list = field(default_factory=list)


mary = Employee("Mary", "Engineer")
mary.skills.append("Cyber Security")
print(mary)


@dataclass
class Animal:
    name: str
    species: str

    def hello(self):
        print("Hello!")


@dataclass
class Cat(Animal):
    lives: int


c = Cat("Felix", "Siamese", 9)
print(c)
c.hello()


@dataclass
class Camera:
    brand: str
    lens: int
    shots_taken: int = 0


c = Camera("Canon", "50mm")
print(c)
c.shots_taken += 30
print(c)


@dataclass
class Climber:
    name: str
    grades_climbed: set = field(default_factory=set)

    def max_grade(self):
        return (
            f"{self.name} as climbed a {max(self.grades_climbed)}, nice!"
            if self.grades_climbed
            else "Nothing yet!"
        )


adam = Climber("Adam")
print(adam)
adam.grades_climbed.add(10)
print(adam)
adam.grades_climbed.add(1)
adam.grades_climbed.add(8)
adam.grades_climbed.add(6)
adam.grades_climbed.add(14)
print(adam.max_grade())
adam.grades_climbed.clear()
print(adam.max_grade())

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    published_year: int = 2020
    genre: str = "Fiction"

    def name_and_author(self):
        return f"{self.title} by {self.author}"


from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Person:
    first_name: str
    last_name: str
    nickname: Optional[str] = None
    full_name: str = field(init=False)

    def __post_init__(self):
        if self.nickname is None:
            self.nickname = self.first_name
        self.full_name = f"{self.first_name} {self.last_name}"
