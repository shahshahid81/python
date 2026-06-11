print(not True)
print(not False)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

balance = 1000.00
withdrawl = 1200.00
withdrawl_limit = 500.0

print(withdrawl < withdrawl_limit and withdrawl <= balance)

a = 20
b = 0
# short circuit and no divide by zero error
print(b != 0 and a / b > 1)
