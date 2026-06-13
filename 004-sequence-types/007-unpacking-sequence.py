rate = 5.0, 5.12
print(rate[0])
print(rate[1])

apr = rate[0]
apy = rate[1]
print(apr)
print(apy)

# note that lhs and rhs must have equal elements
apr, apy = rate
print(apr)
print(apy)

a, b, c = 10, 3.14, "abc"
print(a)
print(b)
print(c)

# ValueError: too many values to unpack (expected 2)
# a, b = 10, 3.14, "abc"

# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = 10, 3.14

x, y, z = "abc"
print(x)
print(y)
print(z)

s = "abcdef"
# note that rhs is evaulated first
a, b, c = (1 + 1, s[::-1], 3.14)

print(a)
print(b)
print(c)

a = 100
b = 3.14
print(a)
print(b)

temp = a
a = b
b = temp
print(a)
print(b)

a = 100
b = 3.14
print(a)
print(b)
t = b, a
a, b = t
print(a)
print(b)

a = 100
b = 3.14
print(a)
print(b)
# first rhs creates tuple and then unpacking
a,b = b,a
print(a)
print(b)