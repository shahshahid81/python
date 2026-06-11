a = 10
b = 10.0
print(a == b)

c = 10.0
print(a == c)
print(a is b)
print(id(a), id(b))

a = 10
b = 10
# True since python internally caches some values that are most used
print(id(a), id(b))
print(a is b)

# It can be false for others, depends on implementation.
a = 100_000_000_000_000
b = 100_000_000_000_000
print(id(a), id(b))
print(a is b)

print(10 != 12)
print(10.5 != 10.5)
print(10 >= 5)
print(10.5 < 100)

a = 1 + 1j
b = 1 + 1j
c = 2 + 2j
print(a == b)
print(a is b, id(a), id(b))
# Below error because complex number doesn't support less than
# TypeError: '<' not supported between instances of 'complex' and 'complex'
# print(a < c)

# False because the numbers don't have the same IEEE 754 representation
print(0.1 * 3 == 0.3)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)

print(id(v1), id(v2), id(v3))
print(v1 is v2)
# False if no eq method because by default, id operator "is" is used if no eq method implemented else it will use the eq method
print(v1 == v2)
print(v2 == v3)
