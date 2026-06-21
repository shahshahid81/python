from pprint import pprint


def outer(a, b):
    print(hex(id(a)))
    sum_ = a + b

    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return "You just called a closure!"

    return inner


func = outer(2, 3)
print(func)
pprint(func.__closure__)
print(func())


def outer(a, b):
    def inner(c):
        return c**2

    return inner


func = outer(2, 3)
print(func(10))
print(func.__closure__)


def power(n):
    def inner(x):
        return x**n

    return inner


square = power(2)
print(square)
print(square.__closure__)
print(square(10))

cubes = power(3)
print(cubes)
print(cubes.__closure__)

print(cubes(3))


def execute(func):
    def inner(a, b):
        result = func(a, b)
        return result

    return inner


def add(a, b):
    return a + b


add_executor = execute(add)
print(add_executor.__closure__)
print(hex(id(add)))

print(add_executor(2, 3))


def execute(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


def add(a, b, c):
    print("add....")
    return a + b + c


def say_hello(name, *, formal=True):
    print("say_hello....")
    if formal:
        return f"Pleased to meet you, {name}"
    else:
        return f"Hi, {name}"


exec_add = execute(add)
exec_greet = execute(say_hello)

print(exec_add(1, 2, 3))
print(exec_greet("Michael", formal=False))


def factorial(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod


def diagonal_matrix(rows, cols, *, diagonal=1):
    return [
        [diagonal if row == col else 0 for col in range(cols)] for row in range(rows)
    ]


print(factorial(4))
print(diagonal_matrix(3, 4, diagonal=10))

from time import perf_counter

start = perf_counter()
result = factorial(10_00)
end = perf_counter()
print(f"elapsed: {end - start}")
print(f"result = {result}")

start = perf_counter()
result = diagonal_matrix(10, 10, diagonal=-1)
end = perf_counter()
print(f"elapsed: {end - start}")
print(f"result = {result}")


def time_it(func, *args, **kwargs):
    start = perf_counter()
    result = func(*args, **kwargs)
    end = perf_counter()
    print(f"elapsed: {end - start}")
    return result


result = time_it(factorial, 10_00)
print(result)

result = time_it(diagonal_matrix, 10, 10, diagonal=1)
print(result)


def time_it(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"elapsed: {end - start}")
        return result

    return inner


timed_fact = time_it(factorial)
timed_diagonal = time_it(diagonal_matrix)

result = timed_fact(5)
print(result)


result = timed_diagonal(10, 10)
print(result)
