import math

print(math)

# help(math)
# help(math.factorial)

print(math.factorial(4))
# TypeError: math.factorial() takes no keyword arguments
# print(math.factorial(x=4))

print(math.pi)
print(math.e)
print(math.gcd(15, 25))

import cmath

cmath.sqrt(-4)

# ValueError: expected a nonnegative input, got -4.0
# math.sqrt(-4)

import math as m

print(m)

print(m is math)

# finds module, loads it in memory and assign it to symbol rnd, instead of random because of renaming
import random as rnd

print(rnd)
print(rnd.randint(3, 10))
print(rnd.randint(3, 10))
print(rnd.randint(3, 10))

import os

print(os.path.curdir)

import os.path as os_path

print(os_path.curdir)

import os.path as path

print(path.curdir)
print(path.abspath(path.curdir))

import fractions

f1 = fractions.Fraction(1, 2)
print(f1)

f2 = fractions.Fraction(1, 4)

print(f1 + f2)
print(f1 * f2)

f = fractions.Fraction(0.1)
print(f)
