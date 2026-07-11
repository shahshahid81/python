# Remember to close the file once done
# f = open("sample.txt", "w")
# f.write("Hello World!")
# f.close()

# File is closed automatically once block is executed
from contextlib import contextmanager
import os


with open("sample.txt", "w") as f:
    f.write("Hello World!")


# Better to use class when we might have multiple helper methods or complex code not expressable in single function
class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()


# Internally, something like this happens
# manager = OpenFile("sample.txt", "w")
# f = manager.__enter__()

# try:
#     f.write("Hello World!")
# finally:
#     manager.__exit__(...)
with OpenFile("sample.txt", "w") as f:
    f.write("Hello World!")
print(f.closed)


@contextmanager
def open_file(file, mode):

    # statements before yield is the enter method code
    # f = open(file, mode)
    # yield f
    # statements after yield is the exit method code
    # f.close()

    try:
        # note that we didn't need init method because init was storing the data as instance attribute and then using them in enter
        # those same attributes are directly passed to function instead
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file("sample.txt", "w") as f:
    f.write("Hello World!")
print(f.closed)

# We store old cwd, change dir, list files and revert back to the old cwd
cwd = os.getcwd()
os.chdir("026-context-manager/Sample-Dir-One")
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir("026-context-manager/Sample-Dir-Two")
print(os.listdir())
os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        # empty yield is fine, since we don't need any object
        yield
    finally:
        os.chdir(cwd)


with change_dir("026-context-manager/Sample-Dir-One"):
    print(os.listdir())

with change_dir("026-context-manager/Sample-Dir-Two"):
    print(os.listdir())
