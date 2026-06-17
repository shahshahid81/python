vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]

from math import sqrt

magnitudes = []

for vector in vectors:
    magnitude = sqrt(vector[0] ** 2 + vector[1] ** 2)
    magnitudes.append(magnitude)

print(magnitudes)

magnitudes = [sqrt(vector[0] ** 2 + vector[1] ** 2) for vector in vectors]
print(magnitudes)

strings = "Python is an awesome language".split(" ")
print(strings)

filtered = []
for item in strings:
    if len(item) >= 5:
        filtered.append(item)
print(filtered)

filtered = [item for item in strings if len(item) >= 5]
print(filtered)


sales = {"widget 1": 0, "widget 2": 5, "widget 3": 10, "widget 4": 2}
high_sales = []
for key, value in sales.items():
    if value >= 5:
        high_sales.append(key)
print(high_sales)

high_sales = [key for key, value in sales.items() if value >= 5]
print(high_sales)

m = [[0] * 3] * 3
print(m)
print(m[0] is m[1])
m[0][0] = 100
print(m)

#  single underscore variable is standard, use it to store something that is not going to be unused
# note that single variable works because it is available to all and can be assigned any data
m = [[0] * 3 for _ in range(3)]
print(m)
print(m[0] is m[1])
m[0][0] = 100
print(m)

m = [[0] * 3 for _ in range(3)]
for row in range(3):
    for col in range(3):
        if row == col:
            m[row][col] = 1
print(m)

m = [
    [   
        1 if row == col else 0 
        for col in range(3)
    ] 
    for row in range(3)
    ]
print(m)
