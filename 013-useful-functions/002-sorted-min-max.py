l = [1, 2, 9, 3, 8]
t = (1, 2, 9, 3, 8)
s = {1, 2, 9, 3, 8}

# sorted return a list
print(sorted(l))
print(l)

print(sorted(t))
print(t)

print(sorted(s))
print(s)
print(sorted(s, reverse=True))

print(ord("a"))
print(ord("A"))
# unicode character is compared
print("A" < "a")

print(sorted(["a", "b", "c"]))
print(sorted("abc"))
print(sorted("aAbBcC"))
print(ord("X"))
print(sorted(["Zebra", "apple", "atom"]))

l = [1, 10, 2, 9, 8]
sorted_ascending = sorted(l)
print(sorted_ascending)

print(min(l))
print(max(l))
# ValueError: min() arg is an empty sequence
# print(min([]))

print(min([], default=0))
print(max([], default=0))
