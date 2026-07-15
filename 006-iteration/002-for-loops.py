suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

for suit in suits:
    print(f"{suit[0].upper()} = {suit}")

for c in "python":
    print(c)

print(suit)  # note that suit is persisted after the loop ends
print(c)  # note that c is persisted after loop ends

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

for suit in suits:
    # suit is a copy, original is not modified
    suit = f'{suit[0].upper()}'
    print(suit)
print(suits)

for i in range(2, 11, 2):
    print(i)

print(list(range(2, 11, 2)))

for i in range(3):
    for j in range(3):
        print(f"i={i} j={j}")
    print("-" * 10)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row_idx in range(3):
    for col_idx in range(3):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")

print(len(m))
print(len(m[0]))

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")

m = [[0, 1], [2, 3, 4, 5, 6], [7, 8, 9], [10]]

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")

n = 5
matrix = []

for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print(matrix)

n = 3
matrix = []

for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print(matrix)


data = [10, 20, 30]
print(enumerate(data))
print(list(enumerate(data)))

for t in enumerate(data):
    idx, el = t
    print(idx, el)

for idx, el in enumerate(data):
    print(idx, el)

m = [[0, 1], [2, 3, 4, 5, 6], [7, 8, 9], [10]]
for row in m:
    for element in row:
        print(element)

for row_idx, row in enumerate(m):
    for col_idx, element in enumerate(row):
        print(f"[{row_idx}, {col_idx}] = {element}")

data = [10.5, 11.2, 9.8, None, 11.5, None]
count = 0
total = 0

for i in range(len(data)):
    if data[i] is not None:
        count = count + 1
        total = total + data[i]
average = total / count
print(average)

count = 0
total = 0
for val in data:
    if val is not None:
        count += 1
        total += val
average = total / count
print(average)

for i in range(len(data)):
    if data[i] is None:
        data[i] = average
print(data)

data = [10.5, 11.2, 9.8, None, 11.5, None]
for index, val in enumerate(data):
    if val is None:
        data[index] = average
print(data)
