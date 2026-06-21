def func(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)


func(10, 20, 30, 40, c=50)
# it needs c else error
# TypeError: func() missing 1 required keyword-only argument: 'c'
# func(10, 20, 30, 40, 50)


# all keyword only after *, but doesn't accept * arguments in tuple
def func(a, b, *, c):
    print(a)
    print(b)
    print(c)


# TypeError: func() takes 2 positional arguments but 3 were given
# func(10, 20, 30)
func(a=10, b=20, c=30)


# c had to be default since it is positional, no subsequent default for keyword argument
def func(a, b=2, c=3, *, d=10, e, f=30):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)


func(1, e=20)
func(e=20, a=1)
func(1, c=3.5, d=100, e=200)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000],
]


def process_row(row, item_sep):
    return item_sep.join(str(elem) for elem in row)


def process_data(data, item_sep=",", line_sep="\n"):
    row_strings = [process_row(row, item_sep) for row in data]
    return line_sep.join(row_strings)


print(process_data(data, ":", "\n\n"))
print(process_data(data, item_sep=":", line_sep="\n\n"))


def process_data(data, *, item_sep=",", line_sep="\n"):
    row_strings = [process_row(row, item_sep) for row in data]
    return line_sep.join(row_strings)


print(process_data(data, item_sep=":", line_sep="\n\n"))
# TypeError: process_data() takes 1 positional argument but 3 were given
# print(process_data(data, ":", "\n\n"))


def coords_to_json(longitude, latitude):
    # use {{ and }} to print curly braces in f string
    return f'{{"longitude": {longitude}, "latitude": {latitude}}}'


print(coords_to_json(10, 20))


def coords_to_json(*, longitude, latitude):
    # use {{ and }} to print curly braces in f string
    return f'{{"longitude": {longitude}, "latitude": {latitude}}}'


print(coords_to_json(longitude=10, latitude=20))


def func(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


func(10, 20, 30, 40, 50, c=1, d=2, x=100, y=100)
func(a=10, b=20, c=1, d=2, x=100, y=100)


def to_json(arg1, *, kw1, **extras):
    formatted_extras = ", ".join([f"{key}: {value}" for key, value in extras.items()])
    return f'{{ "arg1": {arg1}, "kw1": {kw1}, "extras": {{{formatted_extras}}}}}'


print(to_json(10, kw1=20, a=1, b=2, c=3))
print(to_json(arg1=10, kw1=20, a=1, b=2, c=3))

# / means before parameters are positional only, no keyword
def to_json(arg1, /, *, kw1, **extras):
    formatted_extras = ", ".join([f"{key}: {value}" for key, value in extras.items()])
    return f'{{ "arg1": {arg1}, "kw1": {kw1}, "extras": {{{formatted_extras}}}}}'


print(to_json(10, kw1=20, a=1, b=2, c=3))
# TypeError: to_json() missing 1 required positional argument: 'arg1'
# print(to_json(arg1=10, kw1=20, a=1, b=2, c=3))

