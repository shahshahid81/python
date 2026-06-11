print(100 - 20 + 50)
print((100 - 20) + 50)
print((100 + 50) - 20)
print(10 * 4 + 5 * 5)
# ** power operator has higher precedence
print(10 * 2**3)

# note here that unary minus is applied to 8 first then power is calculated even when unary minus has less precedence, this is expected
print(2**-8)
# note here that first power is calculated first then unary minus is applied, same as -(4 ** 0.5)
print(-(4**0.5))
print((-4) ** 0.5)
n = 10
print(n * n - 1)
print(n * (n - 1))
