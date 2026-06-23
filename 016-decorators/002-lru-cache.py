def cache(func):
    def inner(*args):
        result = func(*args)
        return result

    return inner


cache_dict = {}


def cache(func):
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return inner


@cache
def add(a, b):
    return a + b


@cache
def mul(a, b):
    return a * b


print(add(1, 2))
# note that it will return 3 since we are using same cache for add and mul
print(mul(1, 2))


def cache(func):
    def inner(*args):
        print("Initializing cache...")
        cache_dict = {}
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return inner


@cache
def add(a, b):
    return a + b


print(add(1, 2))
# cache is initialized again since inner is called again
print(add(1, 2))


def cache(func):
    print("Initializing cache...")
    cache_dict = {}

    def inner(*args):
        if args in cache_dict:
            print("cache hit")
            return cache_dict[args]
        print("cache miss")
        result = func(*args)
        cache_dict[args] = result
        return result

    return inner


@cache
def add(a, b):
    return a + b


@cache
def mul(a, b):
    return a * b


# different dictionaries in closure for different functions
print(add.__closure__, mul.__closure__)

print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
print(add(1, 2))
print(add(2, 3))
print(mul(1, 2))
print(mul(3, 4))
print(mul(1, 2))
print(mul(3, 4))

from functools import lru_cache


@lru_cache(maxsize=2)
def add(a, b):
    print("add called...")
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))
print(add(1, 2))
print(add(3, 4))


def fib(n):
    print(f"fib({n}) called...")
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(5))
print(fib(8))


@lru_cache(maxsize=3)
def fib(n):
    print(f"fib({n}) called...")
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(5))
print(fib(8))
print(fib(10))
print(fib(40))


@lru_cache()
def my_func(l):
    print("calling my_func")
    return l


my_func(10)
# list cannot be hashed since they are immutable, hence error
# TypeError: unhashable type: 'list'
# my_func([1, 2, 3])
