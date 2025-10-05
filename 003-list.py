squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list

print(squares + [36, 49, 64, 81, 100])  # concatenate list

# lists are mutable
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4**3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)

cubes.append(216)  # add the cube of 6
cubes.append(7**3)  # and the cube of 7
print(cubes)

rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb))
print(id(rgba))
print(id(rgb) == id(rgba))  # they reference the same object
rgba.append("Alph")
print(rgb)

# Creating shallow copy of the list, if objects, the reference is same
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)

# replace some values of the slice, modifies original array
letters[2:5] = ["C", "D", "E"]
print(letters)

# remove some values of the slice, modifies original array
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list, modifies original array
letters[:] = []
print(letters)

letters = ["a", "b", "c", "d"]
print(len(letters))

a = ["a", "b", "c"]
n = [1, 2, 3]
# creating a list of lists
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

list = [1]
# add item to end of list
list.append(2)
print(list)

# add other iterable to the lsit
list.extend(a)
print(list)
# tuple is also iterated
list.extend((True, 2))
print(list)
m = {}
m['ab'] = 1
print(m)
# Note that extending m is only adding the keys
list.extend(m)
print(list)

# Insert at specific index
list.insert(0, 'first')
print(list)

# remove first occurence of the value
list.remove(2)
print(list)

# remove and return value at specific index, by default index is -1
last = list.pop()
print(list)
print(last)

second_last = list.pop(-2)
print(list)
print(second_last)

# finds and returns 0 based index of first occurence or raise ValueError if not found
idx = list.index('first')
print(idx)

# find and returns index based on start and end range, end is exclusive, same as slice
idx = list.index('a', 0, 3)
print(idx)

# count occurence
print(list.count(1))

list = [12, 11, 4, 31, 8]
# sorts and modifies the original list, note that elements must be comparable
list.sort()
print(list)
list.sort(reverse=True)
print(list)

# returns shallow copy, same as list[:]
shallow_copy = list.copy()
print(shallow_copy)

# empties the list, same as del list[:]
list.clear()
print(list)
