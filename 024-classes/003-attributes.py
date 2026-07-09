class MotorBike:
    # note that this is class attribute and shared among instances and can be accessed by class
    # change by one instance or class is reflected in others
    wheels = 2

    in_stock = 0

    def __init__(self, power, colour):
        # these are instance attributes, each instance has it's own copy
        self.colour = colour
        self.power = power
        MotorBike.in_stock += 1

    # below decorator makes method of class instead of instance and passes class instead of instance as first arg
    @classmethod
    def set_new_wheel(cls, new_wheels: int) -> None:
        print(id(cls))
        if not isinstance(new_wheels, int):
            raise ValueError("Wheels needs to be int!")
        cls.wheels = new_wheels


bike_a = MotorBike(125, "Red")
bike_b = MotorBike(250, "Green")
print(MotorBike.in_stock)
print(bike_a.wheels, bike_b.wheels, MotorBike.wheels)
MotorBike.wheels = 3
print(bike_a.wheels, bike_b.wheels, MotorBike.wheels)
print(id(MotorBike))
# ValueError: Wheels needs to be int!
# MotorBike.set_new_wheel(3.4)
MotorBike.set_new_wheel(4)
print(bike_a.wheels, bike_b.wheels, MotorBike.wheels)


class Employee:
    company = "Apple"
    bonus_amount = 500
    pay_rise_percent = 1.1

    def __init__(self, name: str, pay: int, role: str) -> None:
        self.name = name
        self.pay = pay
        self.role = role

    def show_pay_with_bonus(self):
        print(f"{self.name} is paid {self.pay + Employee.bonus_amount} with bonus!")

    def increase_annual_pay(self):
        self.pay = round(self.pay * Employee.pay_rise_percent)

    @classmethod
    def change_bonus_amount(cls, new_bonus_amount):
        cls.bonus_amount = new_bonus_amount

    @classmethod
    def change_rise_pct(cls, new_rise_pct):
        cls.pay_rise_percent = new_rise_pct


john = Employee("John", 45000, "Software Engineer")
print(vars(john), john.company)
john.show_pay_with_bonus()
john.increase_annual_pay()
print(john.pay)

john.change_bonus_amount(1000)
print(john.bonus_amount)
print(Employee.bonus_amount)

Employee.change_bonus_amount(2000)
print(john.bonus_amount)
print(Employee.bonus_amount)
john.show_pay_with_bonus()


john.change_rise_pct(1.15)
print(john.pay_rise_percent)
print(Employee.pay_rise_percent)

Employee.change_rise_pct(1.25)
print(john.pay_rise_percent)
print(Employee.pay_rise_percent)


class Laptop:
    brand = "Dell"

    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor

    @classmethod
    def update_brand(cls, new_brand):
        if not isinstance(new_brand, str):
            raise ValueError("Brand must be str")
        if not new_brand.isalpha() or len(new_brand) > 10:
            raise ValueError(
                "Brand must be characters only with length no longer than 10"
            )
        cls.brand = new_brand


basic_laptop = Laptop("4GB", "Intel I3")
print(vars(basic_laptop), basic_laptop.brand)
basic_laptop.update_brand("Lenovo")
print(vars(basic_laptop), basic_laptop.brand)

from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = int(age)

    @classmethod
    def from_birth_year(cls, name, year):
        current_year = datetime.now().year
        # returning an instance of class, this is called alternate constructor
        return cls(name, current_year - year)


john = Person("John", 45)
print(vars(john))
mary = Person.from_birth_year("mary", 1985)
print(vars(mary))


class Employee:
    bonus = 5000
    all_names = []

    def __init__(self, name: str, pay: int):
        self.name = name
        self.pay = pay
        Employee.all_names.append(name)

    def pay_rise(self):
        self.pay += Employee.bonus


class Python:
    version = 3.9

    def __init__(self, libraries: list):
        self.libraries = libraries

    @classmethod
    def change_version(cls, new_version):
        if not isinstance(new_version, float):
            raise ValueError("Version must be float.")
        cls.version = new_version
