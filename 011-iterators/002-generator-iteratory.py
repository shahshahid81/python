squares = []
for i in range(5):
    squares.append(i**2)
print(squares)

# note that the above loop is same as below comprehension, we add the items one by one in the list.
squares = [i**2 for i in range(5)]
print(squares)

# note that printing squares is giving us a generator iterator
# this is not tuple comprehension, it is not possible since we cannot append data to readonly tuple
squares = (i**2 for i in range(5))
print(squares)

# iterating through the generator iterator
for i in squares:
    print(i)

# note this is empty because generator iterator is empty
for i in squares:
    print(i)

# re creating generator to print data
squares = (i**2 for i in range(5))
for i in squares:
    print(i)

squares = (i**2 for i in range(5))
# lhs returns an iterator and rhs is an iterator hence same
print(iter(squares) is squares)

squares = (i**2 for i in range(5))
print(3 in squares)
# empty list because the above statement had to evaulate the complete generator object and it didn't found 3
print(list(squares))

squares = (i**2 for i in range(5))
print(4 in squares)
print(list(squares)) # all elements after 4 since it stopped iterating after 4 found
