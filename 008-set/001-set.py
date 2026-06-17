# type depends on first key, if it is key value pair, others must be too. If first is element, others has to be elements only, no key value pair
s = {"a", "b", "c"}
print(s)
print(type(s))

s = set(["a", "b", "c"])
print(s)
print(type(s))

s = set("abc")
print(s)
print(type(s))

s = set("python")
print(s)
print(type(s))

s = set(["a", "a", "b", "b"])
print(s)
print(type(s))

# this cannot be used for empty set, since it will be interpreted as empty dictionary
s = {}
print(s)
print(type(s), len(s))

s = set()
print(s)
print(type(s), len(s))

s = set("python")
print("p" in s)
print("x" in s)

for item in s:
    print(item)

s2 = s.copy()
print(s2)

from copy import deepcopy

s2 = deepcopy(s2)
print(s2)
