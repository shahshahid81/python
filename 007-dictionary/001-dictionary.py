d = {"a": 1, "b": 2, "c": 3}
print(d)

person = {"first_name": "John", "last_name": "Doe", "year_born": 2016}
print(person["year_born"])
person["year_born"] = 1950
print(person)
person["month_born"] = "March"
print(person)

d = {3.14: "pi", 2: "even", 7: "prime"}
print(d[3.14])
print(d[2])

l = [1, 2, 3]
# list are not hashable since they are mutable, in general, mutable data is not hashable
# TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# d = {l: 100}


print(hash(100))
print(hash(3.14))
# TypeError: unhashable type: 'list'
# print(hash(l))

# tuple may or may not be hashable depending on if it has mutable elements
# below is hashable since all members are hashable
t = 1, 2, 3, 4
print(hash(t))

# below is not hashable since all members are not hashable
# t = [1,2], 3, 4
# print(hash(t))


d = {
    (0, 0): "origin",
    (1, 0): "unit-x",
    (0, 1): "unit-y",
}
print(d)
print(d[(0, 0)])

d = {"a": 1, "b": 2, "c": 3}
print(id(d))
print(d)
del d["a"]
print(id(d))
print(d)

# Below error occured since no x key
# KeyError: 'x'
# print(d['x'])

# Below error occured since no x key
# KeyError: 'x'
# del d['x']

# stores all the variables used in dictionary
print(globals())
print(type(globals()))

p = globals()["person"]
print(person)
print(p)
print(p is person)
