a = 100
print(a)
print(a + 11)
b = a + 11
print(b)
a = 3.14
print(a)

test = 100
test_1 = 10
_test_1 = 10
__test__ = 10
TEST = 10
print(test, TEST)
# 1_test = 10
# if = 10

a = float(10)
print(a)
print(float)
# below is reassigning float function to a number, making it non collable unless deleted
float = 100.5
print(float)
# a = float(10)
# print(a)
del float
print(float)  # noqa: F821

current_balance = 100.0
print(current_balance)
# non standard way, use snake case
currentBalance = 100.0
print(currentBalance)