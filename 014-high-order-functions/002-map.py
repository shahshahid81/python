data = ["a", "ab", "abc", "abcd"]
lengths = [len(element) for element in data]
print(lengths)
lengths = (len(element) for element in data)
print(lengths)
print(3 in lengths)


def my_len(x):
    return len(x)


lengths = (my_len(element) for element in data)
print(list(lengths))

# returns an iterator
lengths = map(len, data)
print(lengths)
print(list(lengths))
