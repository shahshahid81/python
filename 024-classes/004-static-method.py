class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.calculate_area(self.width, self.height)
        self.perimeter = self.calculate_perimeter(self.width, self.height)

    @staticmethod
    def calculate_area(width, height):
        return height * width

    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (height + width)


rectangle = Shape(10, 5)
print(vars(rectangle))

import random


class Employee:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname.title()
        self.lname = lname.title()
        self.email = self.generate_email_address(self.fname, self.lname)
        self.user_id = self.generate_user_id(self.lname)

    @staticmethod
    def generate_email_address(fname: str, lname: str) -> str:
        return f"{fname.lower()}.{lname.lower()}@mail.com"

    @staticmethod
    def generate_user_id(lname: str) -> str:
        return f"{random.randint(100, 999)}{lname.lower()}"


john = Employee("john", "smith")
print(vars(john))

from datetime import datetime


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return "Vroom! The engine is now running."

    @staticmethod
    def is_classic(car_year):
        current_year = datetime.now().year
        age = current_year - car_year
        return age > 25
