from collections import Counter

c = Counter("gallad")
print(c)
c = Counter(["a", "a", "b", "c", "c"])
print(c)
print(c.most_common(2))
c = Counter({"a": 1, "b": 2})
print(c)
print(list(c.elements()))
c = Counter(cats=4, dogs=5)
print(c)
print(c["cats"])
# no key error
print(c["pet"])
print(list(c.elements()))

c = Counter(a=4, b=2, c=0, d=-2)
print(c)
d = ["a", "b", "b", "c"]
c.subtract(d)
print(c)
c.update(d)
print(c)

d = Counter(d)
c = c - d
print(c)
c = c + d
print(c)
