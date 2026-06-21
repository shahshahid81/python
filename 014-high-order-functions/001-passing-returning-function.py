def add(a, b):
    return a + b


def greet(name):
    return f"Hello, {name}!"


print(add(2, 3), greet("John"))


def apply(func, *args):
    result = func(*args)
    return result


print(apply(add, 2, 3))
print(apply(greet, "John"))
print(apply(lambda a, b, c: a + b + c, 10, 20, 30))


def mul(a, b):
    return a * b


def power(a, n):
    return a**n


def choose_operator(name):
    if name == "add":
        return add
    if name == "mul":
        return mul
    if name == "power":
        return power


op = choose_operator("power")
print(op)
print(op(2, 3))


def choose_operator(name):
    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    def power(a, n):
        return a**n

    if name == "add":
        return add
    if name == "mul":
        return mul
    if name == "power":
        return power


op = choose_operator("power")
print(op)
print(op(2, 3))


def choose_operator(name):
    if name == "add":
        return lambda a, b: a + b
    if name == "mul":
        return lambda a, b: a * b
    if name == "power":
        return lambda a, n: a**n


op = choose_operator("power")
print(op)
print(op(2, 3))


def in_list(l, element):
    return element in l


def in_tuple(t, element):
    return element in t


def in_set(s, element):
    return element in s


n = 10_000_000
l = list(range(n))
t = tuple(range(n))
s = set(range(n))
x = 5_000_000

from time import perf_counter

start = perf_counter()
in_list(l, x)
end = perf_counter()
print(end - start)

start = perf_counter()
in_tuple(t, x)
end = perf_counter()
print(end - start)

start = perf_counter()
in_set(s, x)
end = perf_counter()
print(end - start)


def time_it(func, *args):
    start = perf_counter()
    result = func(*args)
    end = perf_counter()
    print(end - start)
    return result


print(time_it(in_list, l, x))
print(time_it(in_tuple, t, x))
print(time_it(in_set, s, x))
