a = 1
b = 0
# Exception raised by below code
#     result = a / b
#              ~~^~~
# ZeroDivisionError: division by zero
# result = a / b
# print(result)

# Exception Sub Class
ex = ValueError("Name must be at least 5 characters long")
print(type(ex))
print(ex)
# repr used to print more details
print(repr(ex))
print(str(ex))

# below raises an exception
# raise ex

name = input("Enter name(5 chars min):")
if len(name) < 5:
    raise ValueError(f"{name} is not 5 characters or more...")

print(f"Hello {name}")

print(issubclass(KeyError, LookupError))
print(issubclass(KeyError, Exception))
print(issubclass(IndexError, Exception))

ex = KeyError("some message")
print(type(ex))
print(isinstance(ex, KeyError))
print(isinstance(ex, LookupError))
print(isinstance(ex, Exception))
print(isinstance(ex, IndexError))
