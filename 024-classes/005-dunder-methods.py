class Ship:
    def __init__(self, crew, length):
        self.crew = crew
        self.length = length

    def __str__(self):
        return f"Crew: {self.crew}, Length: {self.length}"

    # if no str is defined, repr is used for printing
    def __repr__(self):
        return f"Ship({self.crew},{self.length})"


ship = Ship(5, 45)
ship_b = Ship(10, 30)
print(ship)
print(dir(ship))
print(repr(ship))

ships = [ship, ship_b]
# printing list uses repr
print(ships)


class House:
    def __init__(self, bedroom):
        self.bedroom = bedroom

    def __str__(self):
        return f"bedroom: {self.bedroom}"

    def __repr__(self):
        return f"Ship({self.bedroom})"

    # used for == operator, default uses id method for comparison
    def __eq__(self, other):
        return self.bedroom == other.bedroom

    # used for <
    def __lt__(self, other):
        return self.bedroom < other.bedroom

    # used for >
    def __gt__(self, other):
        return self.bedroom > other.bedroom


house_a = House(4)
house_b = House(3)
house_c = House(4)

print(house_a)
print(house_b)
print(house_c)
print(house_a == house_b)
print(house_a == house_c)
print(house_a < house_b)
print(house_a < house_c)
print(house_a > house_b)
print(house_a > house_c)
print(sorted([house_a, house_b, house_c]))


class Plane:
    def __init__(self, seats, length):
        self.seats = seats
        self.length = length

    def __str__(self):
        return f"Seats: {self.seats}, Length: {self.length}"

    def __repr__(self):
        return f"Plane({self.seats},{self.length})"

    def __len__(self):
        return self.length


plane = Plane(240, 60)
print(plane)
print(len(plane))


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

    def __repr__(self):
        return f"Shape({self.width},{self.height})"


a = Shape(10, 3)
b = Shape(8, 2)
print(a)
print(b)
c = a + b
print(c)


class StoreIterator:
    def __init__(self, items):
        self.items = items
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > len(self.items) - 1:
            raise StopIteration
        current_counter = self.counter
        self.counter += 1
        return self.items[current_counter]


class Store:
    def __init__(self, items: list[str]):
        self.items = items

    def __iter__(self):
        return StoreIterator(self.items)


store = Store(["Cheese", "Ham", "Milk"])

for item in store:
    print(item)

for item1 in store:
    for item2 in store:
        print(f"{item1}, {item2}")


import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


class TextFileManager:
    def __init__(self, filename, mode="a"):
        self.filename = self.generate_file_name(filename)
        self.mode = mode
        self.file = None

    @staticmethod
    def generate_file_name(filename):
        if not isinstance(filename, str):
            return "default.txt"
        return filename if filename.endswith(".txt") else f"{filename}.txt"

    def __enter__(self):
        self.file = open(get_file_path(self.filename), self.mode)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
            print("Closed!")

        if exc_type:
            print(f"Error raised: {exc_type}\n{exc}")
            return False

        return True


with TextFileManager("hello.txt") as file:
    file.write("Hello!")


class Employee:
    company = "Apple"

    def __init__(self, name, age):
        # there is no private key in python, convention is to use _ in beginning to others know key is private but it can be accessed and modified by others
        self._data = {"name": name, "age": age, "company": Employee.company}

    def __getitem__(self, key):
        if key not in self._data:
            raise KeyError(f"{key} does not exists!")
        return self._data[key]

    def __setitem__(self, key, value):
        if key == "age" and not isinstance(value, int):
            raise ValueError("age must be an int")
        self._data[key] = value


john = Employee("John", 30)
print(vars(john))
# KeyError: 'names does not exists!'
# print(john["names"])
print(john["name"])

# ValueError: age must be an int
# john["age"] = "Fourty"
john["age"] = 40
print(vars(john))


class Actor:
    def __init__(self, first, last, movie):
        self.first = first
        self.last = last
        self.movie = movie

    def __str__(self):
        return f"{self.first} {self.last} - {self.movie}"

    def __repr__(self):
        return f"{self.first[0]} {self.last}"


class Plant:
    def __init__(self, leaf_width, colour):
        self.leaf_width = leaf_width
        self.colour = colour

    def __len__(self):
        return self.leaf_width

    def __eq__(self, other):
        return self.colour == other.colour

    def __gt__(self, other):
        return self.leaf_width > other.leaf_width


class ShoppingCart:
    def __init__(self):
        self._items = {}

    def __getitem__(self, key):
        return "n/a" if key not in self._items else self._items[key]

    def __setitem__(self, item_name, quantity):
        self._items[item_name] = quantity
