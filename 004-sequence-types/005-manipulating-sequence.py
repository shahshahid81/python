l = [10, 20, 3, 40, 50]
print(l)
l[2] = 30
print(l)

l = [1, 20, 30, 5, 6]
print(l[1:3])
# note that the length of slice is less than the length of the tuple
# here, we are replacing the slice with the rhs value, any iterable will work.
# this only works if step is not provided or is 1
l[1:3] = (2, 3, 4)
print(l)
l[1:3] = "python"
print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
print(l[1::2])
# here, since we have specified step, number of elements in slice and assignment should match exactly else error will be raised
l[1::2] = 20, 40, 60, 80
print(l)
print(l[1::2])

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
print(l[:-3:-1])
# note here that elements are assigned in reverse as well so 100 is assigned to last and 200 is assigned to second last element
l[:-3:-1] = 100, 200
print(l)
print(l[:-3:-1])

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
print(l[1:4])
# note that the elements in RHS are less than slice, effectively deleting the elements and reducing the length
l[1:4] = 10, 20
print(l)
del l[2]
print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
print(l[::2])
# deleting all the elements of slice from original list
del l[::2]
print(l)

l = [1, 2, 3, 4]
print(l)
l.append(5)
print(l)
# note that append will add the whole sequence as whole, instead of iterating the sequence while using slice
l.append("python")
print(l)
l.append((1, 2, 3))
print(l)

l = [1, 2, 3, 4]
print(l)
# extend takes sequence and iterate and add it to the calling collection
l.extend([5, 6, 7, 8])
print(l)
l.extend((10, 20))
print(l)
l.extend("python")
print(l)

l = [1, 2, 3, 4]
print(l)
print(l[2])
l.insert(2, "a")
print(l)
# inserted as whole instead of iterating character by character
l.insert(0, "abc")
print(l)
