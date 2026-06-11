print(1 + 0.5)
print(1.0 + 0.5)

print(2 * 1.125)

print(10 / 4)

print(2**8)
print(2 ** (-8))
print(1 / (2**8))
print(4.0**0.5)

# square root of -4 is not real, hence we get complex number
c = (-4) ** 0.5
print(c)
print(type(c))
print(type(10))
print(type(10.0))
print(c.real)
print(c.imag)

# real and imaginary number
c = 10 + 2j

print(1 + 2)
a = 1
print(a.__add__(2))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 1)
v2 = Vector(2, 3)
print(v1)
print(v2)
# if no __add__ method, we get TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
print(v1 + v2)
