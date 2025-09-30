t = 12345, 54321, "hello!"
print(t[0])
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
v[0].pop()
print(v)

# zero length tuple
empty = ()
print(empty)
print(len(empty))

singleton = ("hello",)  # <-- note trailing comma
print(singleton)
print(len(singleton))

x, y, z = t
print(x)
print(y)
print(z)
