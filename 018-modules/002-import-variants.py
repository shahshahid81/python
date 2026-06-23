import math

print(math)

import random as rnd

print(rnd)

print(math.sqrt(4))

# only creates single symbol sqrt
from math import sqrt

print(sqrt(4))

import math

# imports whole math module even when not needed
sqrt = math.sqrt
print(sqrt)

from fractions import Fraction

print(Fraction)
# NameError: name 'fractions' is not defined.
# print(fractions)

import math
# math is not reimported, it is cached above and used again
from math import sqrt, sin, pi

print(math.gcd(3, 7))
print(math.sqrt(4))
print(sqrt(4))
