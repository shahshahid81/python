# 0000000000111
# 0123456789012
# Python rocks!
s = "Python rocks!"

# slicing returns new object of the same type
print(s[5])  # n
print(s[0:5])  # Pytho
print(s[0 : 5 + 1])  # Python

t = (1, 2, 3, 4, 5)
print(t[1:4], type(t[1:4]))

l = [1, 2, 3, 4, 5]
print(l[1:4], type(l[1:4]))

l1 = [1, 2, 3, 4, 5]
l2 = l1[0:3]
print(l1 is l2)
l2 = [100]
print(l1)
print(l2)

l = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
print(l)

# here, we get a new reference to the sliced object
sub = l[0:2]
print(sub)
print(sub is l)

sub[1] = "Python"
print(l)
print(sub)

print(sub[0] is l[0])
# slice gives  new reference, but to existing object, this is shallow copy
sub[0][0] = 100
print(sub)
print(l)


# 0000000000111
# 0123456789012
# Python rocks!
s = "Python rocks!"

print(s[7:])
print(s[0:6])
print(s[:6])


l = [1, 2, 3, 4, 5]
l2 = l[:]

print(l2)
print(l is l2)

# reference is pointing to new int object of 100
l2[0] = 100
print(l2)
print(l)

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(s[1:8])
print(s[1:8:2])
print(
    s[1::2]
)  # default to end if no value and step is positive. For negative, default is tart
print(s[0::2])
print(
    s[::2]
)  # default start if not specified if step is positive. For negative, default is end.

s = "abcdef"
print(s[-1])
print(s[-4])
print(s[-4:-1])
print(s[-1:-4])
print(s[-1:-4:-1])
print(s[2::-1])
print(s[::-1])

m = [1, 2, 30, 100]
print(m[::-1])

a = "racecar"
print(a == a[::-1])

a = "hello"
print(a == a[::-1])
