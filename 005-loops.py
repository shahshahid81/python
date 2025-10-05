a, b = 0, 1
while a < 1000:
    # use comma as separator instead of new line
    print(a, end=',')
    a, b = b, a+b

# Measure some strings:
words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))

# Create a sample collection
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}
print(users)

# Strategy:  Iterate over a copy because we are modifying the items of original
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)

# Strategy:  Create a new collection because it is tricky to modify the original while iterating
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)

# 0 to 4
for i in range(5):
    print(i)

# 5 to 9
print(list(range(5, 10)))
# 0 to 10 with 3 as step, 0 3 6 9
print(list(range(0, 10, 3)))

# -10 to -100 with -30 as step, -10 -40 -70
print(list(range(-10, -100, -30)))

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

seasons = ["Spring", "Summer", "Fall", "Winter"]
# create a tuple with index and value
print(list(enumerate(seasons)))
# create a tuple with index and value, start index value with 1, note that we are including 0th element, but using 1 instead of 0.
print(list(enumerate(seasons, start=1)))

# prints an iterator string format
print(range(10))

# sum accepts iterator and returns a value
print(sum(range(4)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # only executed if break was not called
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.


class MyEmptyClass:
    pass


def initlog(*args):
    pass   # Remember to implement this!


while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
