a = "hello"
b = "world"

a = "Python's best features:"
print(a)

a = "Python's best features:"
print(a)

s = "Python rocks!"
print(s)
print(s[0])
print(s[1])
print(s[len(s) - 1])
print(s[-1])
print(s[-2])

# TypeError: 'str' object does not support item assignment
# s[0] = "X"


a = ""
b = ""
print(type(a), len(a), type(b), len(b))
print(type(s), len(s))

t = (1, 2, 3)

s = str(t)
print(s)
print(len(s))
print(s[0])

s = "Python"
t = tuple(s)
print(t)

l = list(s)
print(l)

l = list("abcdef")
print(l)

s = "=" * 30
print(s)

print("ab" * 3)           # ababab
print(["ab"] * 3)         # ['ab', 'ab', 'ab']
print([("ab" * 3)])       # ['ababab']

# note that since the inner element is multiplied,
# reference is same for all the elements
s = ["ab"] * 3
print(s)
print(s[0] is s[1])       # True
print(s[0] is s[2])       # True
print(s[1] is s[2])       # True