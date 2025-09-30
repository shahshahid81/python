# del is a statement, which removes references for variables and items in list or dictionary

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

a = 10
print(a)
del a
# print(a) # Reference error, a is not defined
