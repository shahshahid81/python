l = [1, 2, 3, 4, 5]
t = (10, 20, 30)

# zip returns an iterator
result = zip(l, t)
print(result)
print(next(result))
print(next(result))
print(next(result))
# StopIteration
# print(next(result))

combo = list(zip(l, t))
print(list(combo))
print(list(combo))

d = dict([("a", 1), ("b", 2), ("c", 3)])
print(d)

data = [("item1", 10, 100.0), ("item2", 5, 25.0), ("item3", 100, 0.25)]

schema = ("widget", "num_sold", "unit_price")

d = {
    "item1": {"num_sold": 10, "unit_price": 100.0},
    "item2": {"num_sold": 5, "unit_price": 25.0},
    "item3": {"num_sold": 100, "unit_price": 0.25},
}

for row in data:
    print(list(zip(schema, row)))

for row in data:
    widget_name = row[0]
    sub_dict = dict(zip(schema[1:], row[1:]))
    print(widget_name, sub_dict)

data_dict = {}
for row in data:
    widget_name = row[0]
    sub_dict = dict(zip(schema[1:], row[1:]))
    data_dict[widget_name] = sub_dict

print(data_dict)


data_dict = {}
for row in data:
    data_dict[row[0]] = dict(zip(schema[1:], row[1:]))

print(data_dict)

data_dict = {row[0]: dict(zip(schema[1:], row[1:])) for row in data}
print(data_dict)


from pprint import pprint

pprint(data_dict)
