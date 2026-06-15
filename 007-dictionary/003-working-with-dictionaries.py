data = {"open": 100, "high": 110, "low": 95, "close": 110}

# check if key in dictionary
print("open" in data)

print("open" not in data)

print("x" not in data)

# list is taking O(n) time for in operation, dict takes O(1)
l = [1, 2, 3, 4]
print(3 in l)
print(10 not in l)

print(data)
print(data.clear())
print(len(data))

data = {"open": 100, "high": 110, "low": 95, "close": 110}
print(len(data))

data_copy = data.copy()
print(data)
print(data_copy)
# reference is different, internal references are same
print(data is data_copy)

data_copy["x"] = 100
print(data)
print(data_copy)

from copy import deepcopy

deep_copy = deepcopy(data)
print(data_copy is data)

d = {
    "a": [1, 2, 3],
    "b": {
        "x": 0,
        "y": 0,
    },
}
d_copy = d.copy()
print(d_copy is d)
d["b"] = 100
print(d)
print(d_copy)

d = {
    "a": [1, 2, 3],
    "b": {
        "x": 0,
        "y": 0,
    },
}
d_copy = d.copy()
d["a"].append(4)
print(d)
print(d_copy)

d = {
    "a": [1, 2, 3],
    "b": {
        "x": 0,
        "y": 0,
    },
}
d_copy = deepcopy(d)
d["a"].append(4)
print(d)
print(d_copy)

d = dict(a=1, b=2)
print(d)

d = {3.14: "pi", 2: "even"}
# below constructor won't work like above literal since it has to follow variable name rules like not starting with digit etc
# d = dict(2='even')

data = {"open": 0, "high": 0, "low": 0, "close": 0}
print(type(d))

# create all keys with value 10
d = dict.fromkeys(["open", "high", "low", "close"], 10)
print(d)

# create all keys from iterable, below case string
d = dict.fromkeys("python", 1)
print(d)

# keys are unique, only one key will be created
d = dict.fromkeys(["a", "a"], 100)
print(d)

symbols = ["AAPL", "MSFT", "AAPL", "MSFT"]
d = dict.fromkeys(symbols, 0)
# create dict with 2 unique keys and value 0
print(d)
# converting the list to dict and then list gave us unique keys
print(list(d))

# empty dictionaries
d1 = {}
d2 = dict()
print(d1, d2)

transactions = [
    {"item": "widget", "trans_type": "sale", "quantity": 10},
    {"item": "widget", "trans_type": "sale", "quantity": 5},
    {"item": "widget", "trans_type": "refund", "quantity": 2},
    {"item": "license", "trans_type": "sale", "quantity": 1},
    {"item": "license", "trans_type": "sale", "quantity": 1},
    {"item": "license", "trans_type": "refund", "quantity": 1},
]
total_sold = {}
for transaction in transactions:
    item = transaction["item"]
    is_sale = True if transaction["trans_type"] == "sale" else False
    quantity = transaction["quantity"]

    if is_sale:
        if item in total_sold:
            total_sold[item] += quantity
        else:
            total_sold[item] = quantity
print(total_sold)

net_sales = {}
for transaction in transactions:
    item = transaction["item"]
    is_sale = True if transaction["trans_type"] == "sale" else False
    quantity = transaction["quantity"]

    if not is_sale:
        quantity = -quantity

    if item in net_sales:
        net_sales[item] += quantity
    else:
        net_sales[item] = quantity
print(net_sales)

total_sold = {}
for transaction in transactions:
    item = transaction["item"]
    is_sale = True if transaction["trans_type"] == "sale" else False
    quantity = transaction["quantity"]

    if is_sale:
        if item not in total_sold:
            total_sold[item] = 0
        total_sold[item] += quantity
print(total_sold)

total_sold = {}
for transaction in transactions:
    item = transaction["item"]
    is_sale = True if transaction["trans_type"] == "sale" else False
    quantity = transaction["quantity"]

    if is_sale:
        total_sold[item] = total_sold.get(item, 0) + quantity
print(total_sold)

net_sales = {}
for transaction in transactions:
    item = transaction["item"]
    is_sale = True if transaction["trans_type"] == "sale" else False
    quantity = transaction["quantity"]

    if not is_sale:
        quantity = -quantity

    net_sales[item] = net_sales.get(item, 0) + quantity
print(net_sales)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "b": 4}
d1.update(d2)
print(d1)
print(d2)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "b": 4}
d2.update(d1)
print(d1)
print(d2)

d1 = {"a": 1, "b": 2, "c": 100}
d2 = {"c": 3, "b": 4}
d1.update(d2)
print(d1)
print(d2)

d1 = {"a": 1, "b": 2, "c": 100}
d2 = {"c": 3, "b": 4}
d2.update(d1)
print(d1)
print(d2)