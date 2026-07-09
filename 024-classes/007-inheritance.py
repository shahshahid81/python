class Vehicle:
    def __init__(self, colour: str, power: int):
        self.colour = colour
        self.power = power

    def print_power(self):
        print(f"Power is {self.power}")

    def __str__(self):
        return f"Colour: {self.colour}, Power: {self.power}"


# MotorBike extends Vehicle
class MotorBike(Vehicle):
    def __init__(self, colour: str, power: int, max_speed: int):
        # Calling super().__init__() is optional.
        # Python does not automatically invoke the parent class's __init__(),
        # even if it takes no arguments. Call super().__init__() if the parent
        # class performs initialization that should also run.
        super().__init__(colour, power)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", Max Speed: {self.max_speed}"


bike = MotorBike("red", 125, 100)
print(vars(bike))
bike.print_power()
print(bike)


class Battery:
    def __init__(self, capacity, charges=0):
        self.capacity = capacity
        self.charges = charges

    def __repr__(self):
        return f"Battery({self.capacity}, {self.charges})"


class ElectricCar:
    def __init__(self, model):
        self.model = model
        self.battery = Battery(100.0)

    def drive(self):
        if self.battery.capacity < 10:
            print("Not Enough Charge!")
            return
        self.battery.capacity -= 10

    def charge_car(self, cycles):
        for _ in range(cycles):
            if self.battery.capacity == 100:
                break
            self.battery.capacity += 10


tesla = ElectricCar("Model S")
print(vars(tesla))
tesla.drive()
print(vars(tesla))
tesla.charge_car(2)
print(vars(tesla))

for _ in range(20):
    tesla.drive()
print(vars(tesla))


class ComputerSystem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name


class Laptop(ComputerSystem):
    def __init__(self, name, price, ports):
        super().__init__(name, price)
        #  {"usb": 3, "usb-c": 2}
        self.ports = ports

    def __eq__(self, other):
        return self.ports == other.ports


a = ComputerSystem("dell", 100)
b = ComputerSystem("dell", 150)
print(vars(a), vars(b), a == b)

a = Laptop("dell", 100, {"usb": 3, "usb-c": 2})
b = Laptop("dell", 150, {"usb-c": 2, "usb": 3})
print(vars(a), vars(b), a == b)


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def neat_print(self):
        return f"street_address: {self.street_address}\ncity={self.city}\ncountry={self.country}\n"


class Employee:
    def __init__(self, fname, lname, address, pay):
        self.fname = fname.title()
        self.lname = lname.title()
        self.address = Address(*address)
        self.pay = pay

    def __str__(self):
        return (
            f"Name: {self.fname} {self.lname}\nPay: {self.pay}\n"
            + self.address.neat_print()
        )


class Manager(Employee):
    def __init__(self, fname, lname, address, pay, years_as_manager):
        super().__init__(fname, lname, address, pay)
        self.years_as_manager = years_as_manager


class Engineer(Employee):
    def __init__(self, fname, lname, address, pay, specialism):
        super().__init__(fname, lname, address, pay)
        self.specialism = specialism


address = Address("1 main street", "London", "UK")
print(address.neat_print())

emp = Employee("John", "jones", ["1 main street", "London", "UK"], 10000)
print(emp)

manager = Engineer(
    "Michael", "scott", ["1 Condo", "Pennsylvania", "USA"], 230000, "Gaming"
)
print(manager)

engineer = Engineer("John", "Carmack", ["side road", "London", "UK"], 230000, "Gaming")
print(engineer)


class Boat:
    def __init__(self, length, location):
        self.length = length
        self.location = location

    def __str__(self) -> str:
        return f"{self.length} {self.location}"


class SpeedBoat(Boat):
    def __init__(self, length, location, power):
        super().__init__(length, location)
        self.power = power

    def __str__(self):
        return super().__str__() + f" {self.power}"
