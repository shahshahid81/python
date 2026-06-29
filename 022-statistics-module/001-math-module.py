import math

print(sum([1, 2, 3, 4]))
print(sum([1.5, 2, 3, 4]))

values = [0.1] * 10
print(values)
print(format(sum(values), "0.20f"))
# note that 0.1 sum 10 times is equal to 1 only for fsum, others are not exact
print(format(math.fsum(values), "0.20f"))
print(format(0.1, "0.20f"))
print(format(0.1 + 0.1, "0.20f"))
print(format(0.1 + 0.1 + 0.1, "0.20f"))

values = [1, 2, 3, 4]
print(math.prod(values))
print(math.prod(values, start=10))
print(math.prod(values, start=0))
