# There are three basic sequence types: lists, tuples, and range objects

# Following are common sequence operations, sorted in priority from lowest to highest

# List Operations
# 1. Membership test: in, not in
lst = [1, 2, 3]
print("1. Membership test:")
print(2 in lst)         # True
print(5 not in lst)     # True
print()

# 2. Identity test: is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("2. Identity test:")
print(a is b)           # True
print(a is c)           # False
print()

# 3. Comparison: <, >, ==, etc.
# Comparison is lexographical
# Lexicographical comparison compares sequences element by element from left to right, using the first unequal pair to determine the result
# if all items are equal but lengths differ, the shorter sequence is considered smaller.
a = [1, 2]
b = [1, 2, 3]
print("3. Comparison:")
print(a < b)            # True
print([1, 2] == [1, 2])  # True
print()

# 4. Boolean logic: and, or, not
# Empty sequences ([], (), '', range(0)) are Falsy
# Non-empty sequences are Truthy
# and returns the first falsy sequence or the last sequence if all truthy.
# or returns the first truthy sequence or the last sequence if all falsy.
a = [1]
b = [2]
print("4. Boolean logic:")
print(not a)            # False
print(a or [])          # [1]
print(a and [])          # []
print(a and b)          # [2]
print()

# 5. Indexing and slicing
lst = [10, 20, 30, 40, 50]
print("5. Indexing and slicing:")
print(lst[2])           # 30
print(lst[1:4])         # [20, 30, 40]
print(lst[::-1])        # [50, 40, 30, 20, 10]
print()

# 6. Concatenation: +
a = [1, 2]
b = [3, 4]
print("6. Concatenation:")
print(a + b)            # [1, 2, 3, 4]
print()

# 7. Repetition: *
a = [0]
print("7. Repetition:")
print(a * 4)            # [0, 0, 0, 0]
print()

# 8. Function call, method call
lst = [1, 2, 3]
print("8. Function and method calls:")
print(len(lst))         # 3
lst.append(4)
print(lst)              # [1, 2, 3, 4]

# Tuple Operations
# 1. Membership test: in, not in
tpl = (1, 2, 3)
print("1. Membership test:")
print(2 in tpl)         # True
print(5 not in tpl)     # True
print()

# 2. Identity test: is, is not
a = (1, 2, 3)
b = a
c = (1, 2, 3)
print("2. Identity test:")
print(a is b)           # True
print(a is c)           # False
print()

# 3. Comparison: <, >, ==, etc.
a = (1, 2)
b = (1, 2, 3)
print("3. Comparison:")
print(a < b)            # True
print((1, 2) == (1, 2))  # True
print()

# 4. Boolean logic: and, or, not
a = (1,)
b = (2,)
print("4. Boolean logic:")
print(a and b)          # (2,)
print(not a)            # False
print(a or ())          # (1,)
print()

# 5. Indexing and slicing
tpl = (10, 20, 30, 40, 50)
print("5. Indexing and slicing:")
print(tpl[2])           # 30
print(tpl[1:4])         # (20, 30, 40)
print(tpl[::-1])        # (50, 40, 30, 20, 10)
print()

# 6. Concatenation: +
a = (1, 2)
b = (3, 4)
print("6. Concatenation:")
print(a + b)            # (1, 2, 3, 4)
print()

# 7. Repetition: *
a = (0,)
print("7. Repetition:")
print(a * 4)            # (0, 0, 0, 0)
print()

# 8. Function call, method call
tpl = (1, 2, 3)
print("8. Function calls:")
print(len(tpl))         # 3
print(tpl.count(2))     # 1
print(tpl.index(3))     # 2

# Range Operations
# 1. Membership test: in, not in
r = range(5)  # 0,1,2,3,4
print("1. Membership test:")
print(3 in r)           # True
print(5 not in r)       # True
print()

# 2. Identity test: is, is not
a = range(5)
b = a
c = range(5)
print("2. Identity test:")
print(a is b)           # True
print(a is c)           # False (different objects)
print()

# 3. Comparison: <, >, ==, etc.
a = range(3)
b = range(5)
print("3. Comparison:")
print(list(a) < list(b))   # True (compare by converted lists)
print(range(2) == range(2))  # True
print()

# 4. Boolean logic: and, or, not
a = range(0)
b = range(1)
print("4. Boolean logic:")
print(a and b)           # range(0,0) (a is falsy, returns a)
print(b and a)           # range(0,0) (a is falsy, returns a)
print(b or a)            # range(0,1) (b is truthy, returns b)
print(a or b)            # range(0,1) (a is falsy, returns b)
print()

# 5. Indexing and slicing
r = range(10, 21)        # 10 to 20 inclusive
print("5. Indexing and slicing:")
print(r[2])              # 12
print(r[1:5])            # range(11, 15)
print(list(r[1:5]))      # [11, 12, 13, 14]
print(r[::-1])           # reversed range (step negative)
print(list(r[::-1]))     # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
print()

# 6. Concatenation: Not supported directly for range (will error)
print("6. Concatenation:")
try:
    print(r + r)
except TypeError as e:
    print("Error:", e)
print()

# 7. Repetition: Not supported directly for range (will error)
print("7. Repetition:")
try:
    print(r * 3)
except TypeError as e:
    print("Error:", e)
print()

# 8. Function call, method call
r = range(1, 6)
print("8. Function calls:")
print(len(r))             # 5
print(min(r))             # 1
print(max(r))             # 5
print(sum(r))             # 15
print()

# Extra: convert to list or tuple
print("Extra:")
print(list(r))            # [1, 2, 3, 4, 5]
print(tuple(r))           # (1, 2, 3, 4, 5)
