def func(a=1):
    return a


print(func())
print(func(10))
print(func(a=10))


def func(a, b=10, c=20):
    return a, b, c


print(func(1))
print(func(1, 2))
print(func(1, 2, 3))
# b using default value
print(func(1, c=100))


def is_close(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol


print(is_close(1.255, 1.256))
print(is_close(1255, 1256))
print(is_close(1255, 1256, abs_tol=5))


def parse(s, sep=",", strip=True):
    items = s.split(sep)
    if strip:
        return [item.strip() for item in items]
    else:
        return items


print(parse("   a,   b  ,    c  "))
print(parse("   a,   b  ,    c  ", strip=False))
print(parse("   a:b  :    c:  d", sep=":"))
print(parse("a\n|b\n|c\n", sep="|", strip=False))

print("a")
print("a", "b", "c")
print("d")

print("a", "b", "c", sep="----")
print(*"abc", sep=",", end="***\n")
print("next print line")

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000],
]


def process_data(data, item_sep=",", line_sep="\n"):
    output = ""
    for row in data:
        for element in row:
            output = output + str(element) + item_sep
        output += line_sep
    return output


print(process_data(data))
print(process_data(data, item_sep="===="))
print("done")

print(",".join(["a", "b", "c"]))


def process_data(data, item_sep=",", line_sep="\n"):
    output = ""
    for row in data:
        for _ in row:
            row_str = item_sep.join([str(elem) for elem in row])
        output = output + row_str + line_sep
    return output


print(process_data(data, line_sep="==="))


def process_data(data, item_sep=",", line_sep="\n"):
    output = ""
    for row in data:
        # join is passed a generator
        row_str = item_sep.join(str(elem) for elem in row)
        output = output + row_str + line_sep
    return output


print(process_data(data, line_sep="==="))


def process_data(data, item_sep=",", line_sep="\n"):
    row_strings = [item_sep.join(str(elem) for elem in row) for row in data]
    return line_sep.join(row_strings)


print(process_data(data, line_sep="====="))
print(process_data(data))


def process_row(row, item_sep):
    return item_sep.join(str(elem) for elem in row)


def process_data(data, item_sep=",", line_sep="\n"):
    row_strings = [process_row(row, item_sep) for row in data]
    return line_sep.join(row_strings)


print(process_data(data, line_sep="====="))
print(process_data(data))


def process_data(data, item_sep=",", line_sep="\n"):
    # we are creating generator object and passing it to join
    row_strings = (process_row(row, item_sep) for row in data)
    return line_sep.join(row_strings)


print(process_data(data, line_sep="====="))
print(process_data(data))
