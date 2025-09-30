from math import pi

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# note that x is still in scope, there is no block scope in python
print(x)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# syntax: expression, for clause, optional for or if clause
squares = [x**2 for x in range(10)]
print(squares)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])

print([x for x in vec if x >= 0])

print([abs(x) for x in vec])

freshfruit = ["  banana", "  loganberry ", "passion fruit  "]
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]
#   File "<stdin>", line 1
#     [x, x**2 for x in range(6)]
#      ^^^^^^^
# SyntaxError: did you forget parentheses around the comprehension target?

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print([str(round(pi, i)) for i in range(1, 6)])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))

for item in zip([1, 2, 3], ["sugar", "spice", "everything nice"]):
    print(item)
