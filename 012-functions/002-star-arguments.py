def my_func(*args):
    print(type(args))
    print(args)


my_func()
my_func(1)
my_func(1, 2, 3, 4, [1, 2], "abc")


def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)


my_func(1, 2)
my_func(1, 2, 3, 4, 5)


def my_func(a, b, *args, c):
    print(a)
    print(b)
    print(c)
    print(args)


# note that after args, keyword only is required, else python won't to add 5 in either c or args
# TypeError: my_func() missing 1 required keyword-only argument: 'c'
# my_func(1, 2, 3, 4, 5)

my_func(1, 2, 3, 4, c=5)

# not allowed, only one * allowed
# def my_func(a, b, *args, *extras):
#     print(a)
#     print(b)
#     print(args)
#     print(extras)

# def average(*values):
#     try:
#         return sum(values) / len(values)
#     except ZeroDivisionError:
#         return 0


def average(*values):
    # below error if empty tuple, need to handle
    # ZeroDivisionError: division by zero
    if len(values) > 0:
        return sum(values) / len(values)
    return 0


print(average(1))
print(average(1, 2, 3))
print(average(1, 3, 5, 7, 9))
print(average())


def product(*values):
    print(values)
    if len(values) == 0:
        raise ValueError("Must provide at least one argument")
    prod = 1
    for value in values:
        prod *= value
    return prod


print(product(1, 2, 3))
print(product(1, 2, 3, 4))
# ValueError: Must provide at least one argument
# print(product())

l = [1, 2, 3, 4]  # noqa: E741
print(product(l))
# unpacks iterable
print(product(*l))

# note that just *l doesn't work, it needs to be in some list, set, tuple etc so that the object can hold it.
a, b, c, d = [*l]
print(a, b, c, d)
