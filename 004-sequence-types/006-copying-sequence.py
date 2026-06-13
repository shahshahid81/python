l1 = [1, 2, 3]
l2 = l1[:]
print(l2)
print(l1 is l2)
l2.append(10)
print(l2)
print(l1)
l3 = l1.copy()
print(l1 is l3)
l3.append(10)

m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(m1)

m2 = m1.copy()
print(m2)
print(m1 is m2)
m2.append([10, 20, 30])
print(m1)
print(m2)

print(m1[0])
print(m2[0])
print(m1[0] is m2[0])
m2[0].append(-1)
print(m1)
print(m2)

from copy import deepcopy  # noqa: E402
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m2 = deepcopy(m1)

print(m1)
print(m2)
print(m1 is m2)
print(m1[0])
print(m2[0])
print(m1[0] is m2[0])
m2[0].append(-1)
print(m1)
print(m2)

a = (1,2,3)
b = a[:]
print(b)
# note that both are referencing the same tuple, this is an optimization since we cannot modify tuple so both can refer the same tuple
print(a is b)
