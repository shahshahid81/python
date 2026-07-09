class Car:
    # __slots__ replaces the instance __dict__ with fixed storage, so only declared attributes can be assigned.
    # CPython internally allocates fixed storage for __slots__ attributes.
    __slots__ = ["colour", "make", "model"]

    def __init__(self, colour, make, model):
        self.colour = colour
        self.make = make
        self.model = model


car_a = Car("Red", "GMC", "S100")

# AttributeError: 'Car' object has no attribute 'seats'
# car_a.seats = 5

# TypeError: vars() argument must have __dict__ attribute
# print(vars(car_a))
