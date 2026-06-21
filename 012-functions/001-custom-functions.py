# functions are objects
def say_hello():
    return "hello"


print(globals())
a = 100
print(globals())

result = say_hello()
print(result)

print(say_hello())
print(say_hello())

alias = say_hello
print(globals())
print(id(alias), id(say_hello))
print(alias is say_hello)
print(alias())

print(say_hello.__name__)
# alias is just a reference to function object hence both values are same
print(alias.__name__)


def add(a, b, c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    return a + b + c


result = add(1, 2, 3)
print(result)


# note that this overwrote the above definition
def add(a, b, c):
    print("inital namespace:", locals())
    sum_ = a + b + c
    print("inital namespace:", locals())
    return a + b + c


# called new function
result = add(1, 2, 3)
print(result)


def find_max(a, b, c):
    max_ = a
    if b > max_:
        max_ = b
    if c > max_:
        max_ = c
    return max_


print(find_max(10, 20, 30))

from datetime import datetime


# By default None was returned if no return statement
def log(message):
    curr_time = datetime.utcnow().isoformat()
    print(f"{curr_time} - [{message}]")


log("Log 1")

result = log("Log 1")
print(result, type(result))

log("Log 2")

data = [1, 2, 3, 4, 5, 6]

for element in data:
    if element < 0:
        break
else:  # no break
    print("processing all positive elements")

data = [1, 2, 3, 4, 5, 6, -1]

for element in data:
    if element < 0:
        break
else:  # no break
    print("processing all positive elements")


def is_all_positive(data):
    for element in data:
        if element < 0:
            return False
    return True


print(is_all_positive([1, 2, 3, 4]))
print(is_all_positive([10, 3, -4, 100]))
print(is_all_positive(range(1, 10)))
print(is_all_positive(range(10, -20, -2)))
d = {"a": 1, "b": 2, "c": -10}
print(is_all_positive(d.values()))


def gen_matrix(rows, columns, default_value):
    return [[default_value for _ in range(columns)] for _ in range(rows)]


# positional parameters, arguemnts sequence is matched by function parameters
print(gen_matrix(2, 2, 1))
print(gen_matrix(4, 8, 1))
# note that we can pass values using var names, this is called named arguments
print(gen_matrix(rows=4, columns=8, default_value=1))
# we dont need to follow the position of the arguments
print(gen_matrix(columns=8, rows=4, default_value=1))

# below error happens because we passed value for rows in both positional and keyword
# TypeError: gen_matrix() got multiple values for argument 'rows'
# print(gen_matrix(5, rows=4, default_value=10))

# after starting named arguments, we cannot use positional arguments
print(gen_matrix(5, columns=4, default_value=10))
