l = [10, 20, 30, 40, 50]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[4])
print(len(l))
# Out of range error
# print(l[5])

print(l[-1])
print(l[-2])
print(l[-5])
# Out of range error
# print(l[-6])

l = []
print(len(l))
print(type(l))

l = list()
print(l, type(l))

l = [10, 20, 30, 40, 50]
print(l[2])

l[2] = 3.14
print(l)

l[-1] = "Hello"
print(l)

# Out of range error
# l[5] = "World!"

# note that * duplicates the elements within the list
print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2]
print([[1, 2]] * 3)  # [[1, 2], [1, 2], [1, 2]]
print([[1, 2] * 3])  # [[1, 2, 1, 2, 1, 2]]

# note that since the inner element is multiplied, reference is same for all the elements
l = [[0, 0, 0]] * 3
print(l)
l[0][0] = 1
print(l)
print(l[0] is l[1])
print(l[0] is l[2])
print(l[1] is l[2])
