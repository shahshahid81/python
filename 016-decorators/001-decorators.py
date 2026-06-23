def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


def add(a, b, c):
    return a + b + c


def greet(name):
    return f"Hello {name}!"


def join(data, *, item_sep=",", line_sep="\n"):
    return line_sep.join([item_sep.join(str(item) for item in row) for row in data])


print(add(1, 2, 3))
print(greet("python"))
print(join([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

add_wrapper = wrapper(add)
greet_wrapper = wrapper(greet)
join_wrapper = wrapper(join)

print(add_wrapper(1, 2, 3))
print(greet_wrapper("python"))
print(join_wrapper([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def logged(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{__name__} called... result={result}")
        return result

    return inner


add_logged = logged(add)
greet_logged = logged(greet)
join_logged = logged(join)

print(add_logged(1, 2, 3))
print(greet_logged("python"))
print(join_logged([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

old_add_id = id(add)
print(old_add_id)
add = logged(add)
print(id(add))
print(add.__closure__)
# will be same as the function object address of above closure
print(hex(old_add_id))


def add(a, b, c):
    return a + b + c


add = logged(add)


def greet(name):
    return f"Hello {name}!"


greet = logged(greet)


def join(data, *, item_sep=",", line_sep="\n"):
    return line_sep.join([item_sep.join(str(item) for item in row) for row in data])


join = logged(join)

print(add(1, 2, 3))
print(greet("python"))
print(join([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s", level=logging.DEBUG
)
logger = logging.getLogger("Custom Log")
logger.debug("debug message")
logger.error("error message")
logger.warning("warning message")
logger.info("info message")

from time import perf_counter


def log(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logger.debug(f"called {func.__name__}, elapsed={end - start}")
        return result

    return inner


# @log is same as add = log(add)
@log
def add(a, b, c):
    return a + b + c


@log
def greet(name):
    return f"Hello {name}!"


@log
def join(data, *, item_sep=",", line_sep="\n"):
    return line_sep.join([item_sep.join(str(item) for item in row) for row in data])


result = add(1, 2, 3)
print(result)
print(join([range(10) for _ in range(10)]))
