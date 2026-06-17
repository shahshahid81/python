s1 = set("abc")
s2 = {True, False}
s3 = {"a", 100, 200}

# no common elements between sets
print(s1.isdisjoint(s2))
print(s1)
print(s3)
print(s1.isdisjoint(s3))

s = set()
s.add(100)
print(s)
s.add(200)
print(s)
s.add(200)
print(s)

s = set("abc")
s.remove("a")
s.discard("b")
s.discard("x")
# remove raises KeyError, discard doesn't
# KeyError: 'x'
# s.remove("x")


s1 = set("abc")
s2 = set("abcd")


# Proper subset: all elements of s1 are in s2 and s1 != s2 -> True
print(s1 < s2)

# Subset: all elements of s1 are in s2 (equality allowed) -> True
print(s1 <= s2)

# Superset: s2 contains all elements of s1 (equality allowed) -> True
print(s2 >= s1)

# Proper superset: s2 contains all elements of s1 and s2 != s1 -> True
print(s2 > s3)

s3 = set("abc")
# Proper subset: all elements of s1 are in s3 and s1 != s3 -> False (sets are equal)
print(s1 < s3)

# Subset: all elements of s1 are in s1 (equality allowed) -> True
print(s1 <= s1)

# Superset: s3 contains all elements of s1 (equality allowed) -> True
print(s3 >= s1)

# Proper superset: s3 contains all elements of s1 and s3 != s1 -> False (sets are equal)
print(s3 > s1)


s1 = set("abc")
s2 = set("bcd")

# below operations don't modify original set
print(s1 | s2)  # union
print(s1 & s2)  # intersection
print(s1 - s2)  # elements from s2 that are not present in s1
print(s2 - s1)  # elements from s1 that are not present in s2

print(s1)
print(s2)

str_1 = "python is an awesome language!"
str_2 = "a python is also a snake."
set_1 = set(str_1)
set_2 = set(str_2)

# characters present in both strings
print(set_1 & set_2)

s1 = {"FB", "AMZN", "AAPL", "NFLX", "GOOG", "MSFT"}
s2 = {"BABA", "WMT", "COST"}
s3 = {"TSLA", "F", "GM"}

consolidated = list(s1 | s2 | s3)

print(consolidated)


sold = {"w1", "w2", "w3", "w4"}
returned = {"w1"}

non_returned = sold - returned
print(non_returned)

alphabet = set("abcdefghijklmnopqrstuvwxyz")

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)

alphabet = set(string.ascii_letters)
text = "The quick brown fox jumps over the lazy dog"

print(set(string.ascii_letters) - set(text))
print(set(string.ascii_letters.casefold()) - set(text.casefold()))

text = "aBcDeFgHiJkKlLmMnNoOpPqQrRsStTuUvVwW"
print(set(string.ascii_letters.casefold()) - set(text.casefold()))
