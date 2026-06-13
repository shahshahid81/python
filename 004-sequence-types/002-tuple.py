# tuple → Immutable because it is a built-in type implemented in CPython, not in Python code. Once created, its elements cannot be reassigned.

# namedtuple → A tuple with named fields (p.x instead of p[0]). Same immutability as a tuple, but more readable and self-documenting.
# from collections import namedtuple
# Point = namedtuple("Point", ["x", "y"])
# p = Point(10, 20)
# print(p.x)   # 10
# print(p[0])  # 10
# p.x = 30     # AttributeError

# @dataclass(frozen=True) → A normal Python object that blocks attribute assignment by generating a custom __setattr__, but it can be bypassed.
# from dataclasses import dataclass
# @dataclass(frozen=True)
# class Point:
#     x: int
# p = Point(10)
# p.x = 20  # FrozenInstanceError
# object.__setattr__(p, "x", 20)  # Bypass

# Custom __setattr__ → Same idea as a frozen dataclass: block writes through a custom method, but still bypassable.
# class Point:
#     def __init__(self, x):
#         object.__setattr__(self, "x", x)
#     def __setattr__(self, name, value):
#         raise AttributeError("Immutable")
# p = Point(10)
# p.x = 20  # AttributeError
# object.__setattr__(p, "x", 20)  # Bypass


t = (1, 2, 3)
print(t, type(t))

print(t[0])
print(t[1])
print(t[-1])
print(len(t))
print(len(t) - 1)
print(t[2])

# TypeError: 'tuple' object does not support item assignment
# tuple[2] = 40

t = ([1, 2], [3, 4])
print(t[0], type(t[0]))
# TypeError: 'tuple' object does not support item assignment
# tuple[0] = 100
l = t[0]
print(l)
l[0] = 100
print(l)
t[1][1] = 400
print(t[1][1])

# parantheses optional, but good to keep to avoid some edge case
another_tuple = 1, 2, 3
print(another_tuple, type(another_tuple))

a = 10
b = 20
res = a, b, a + b
print(res)

# empty tuple, cannot add anything
t = ()
print(type(t), len(t))

t = tuple()
print(t, type(t), len(t))

l = [1, 2, 3]
t = tuple(l)
print(t)

t = 10, 20, 30
l = list(t)
print(l)


t = 10, 20, 3, 40
print(t)
l = list(t)
l[2] = 30
print(l)
t = tuple(l)
print(t)


t = [1, 2], 30, 40
print(t)
t[0][1] = 20
print(t)

l = list(t)
print(l)
# note that the first element of tuple and the list created from tuple refer to the same object and change in list is reflected in tuple as well
l[0][0] = 10
print(l)
print(t)

t = (1, 2, 3) * 3
print(t)

print((1, 2) * 3)         # (1, 2, 1, 2, 1, 2)
print(((1, 2),) * 3)      # ((1, 2), (1, 2), (1, 2))
print(((1, 2) * 3))      # ((1, 2, 1, 2, 1, 2))

# note that since the inner element is multiplied,
# reference is same for all the elements
# also, note that for tuple with only element, we need to add "," at the end
# else here ((1,2)) will evaluate to (1,2) and ((1,2),) will add tuple within tuple
# x = (1)      # int
# y = (1,)     # tuple
t = ((1, 2),) * 3
print(t)
print(t[0] is t[1])       # True
print(t[0] is t[2])       # True
print(t[1] is t[2])       # True