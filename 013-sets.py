# unordered collection, no duplicates
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # show that duplicates have been removed
print("orange" in basket)  # fast membership testing
print("crabgrass" in basket)

# Demonstrate set operations on unique letters from two words

# string is iterable, all characters are added
a = set("abracadabra")
b = set("alacazam")
print(a)  # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# don't use {} since it will be dictionary
empty_set = set()

# set comprehension, same as list
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
