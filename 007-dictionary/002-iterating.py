d = {
    "key 1": 1,
    "key 2": 2,
    3.14: "pi",
}

# by default, keys are iterated
for k in d:
    print(k)

for k in d:
    print(f"d[{k}] = {d[k]}")

for k in d:
    print(d[k])

for v in d.values():
    print(v)

# note that items return tuple
for t in d.items():
    key, value = t
    print(key, value)

# note that insertion order of keys is maintained, this happened after python 3.6
for key, value in d.items():
    print(f"d[{key}] = {value}")

d["x"] = 100
for k in d:
    print(k)

# modifying value of key doesn't change key order
d["key 1"] = 100
for k in d:
    print(k)

# since key was deleted and added, insertion order changes
del d["key 1"]
d["key 1"] = 100
for k in d:
    print(k)
