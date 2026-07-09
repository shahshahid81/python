import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


class Person:
    def __init__(self, name, age=45):
        print("called")
        self.name = name.title()
        self.age = int(age)
        self.hometown = "London"


# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# john = Person()

john = Person("john")
print(john.name, john.age, john.hometown)

john = Person("john", 55)
print(john.name, john.age, john.hometown)
# vars get the attributes of instance in dictionary
print(vars(john))


class Car:
    """
    A template to resemble a Car.
    """

    def __init__(self, colour: str, power: str) -> None:
        if colour.lower() not in ["blue", "red", "yellow"]:
            self.colour = "white"
        else:
            self.colour = colour.title()
        self.power = power

    def change_colour(self, new_colour: str) -> None:
        """Change the color of the given car instance
        Params:
            new_colour(str): The new colour of the Car
        """
        self.colour = new_colour.title()

    def write_details_to_text_file(self) -> None:
        """Write details of colour and power to file."""
        write_string = f"Colours: {self.colour}, Power: {self.power}\n"
        with open(get_file_path("carlog.txt"), "a") as f:
            f.write(write_string)
        print("Written to file")


car_a = Car("red", "650HP")
print(vars(car_a))
car_a.write_details_to_text_file()

car_a.change_colour("blue")
print(vars(car_a))
car_a.write_details_to_text_file()


car_a.change_colour("purple")
print(vars(car_a))
car_a.write_details_to_text_file()


class Computer:
    def __init__(self, ram: int, platform: str, processor: str) -> None:
        self.ram = ram
        self.platform = platform
        self.processor = processor


computer = Computer(1, "linux", "intel")
print(vars(computer))


climbers = []


class Climber:
    def __init__(self, name: str, height: int):
        self.name = name.title()
        self.height = height
        climbers.append(self.name)


john = Climber("John", "168")
mary = Climber("mary", "165")

print(vars(john), vars(mary))


class Climber:
    def __init__(self, name: str, max_ability: str, style: str) -> None:
        self.name = name.title()
        self.max_ability = max_ability
        self.style = style
