try:
    print(1 / 0)
# we have except instead of catch, we use as to store the value in variable
# heirarchy from most to least specific has to be maintained, same as catch block
except ZeroDivisionError as ex:
    print(f"Exception occured: {type(ex)}, {ex}")
print("Code continues running normally.....")

l = [1, 2, 3, 4, 5]
while len(l) > 0:
    print(l.pop())
print("all done")


l = [1, 2, 3, 4, 5]
try:
    while True:
        print(l.pop())
# note that we didn't use as variable, it is optional
except IndexError:
    print("all done")
print("code resumes here")


l = [1, 2, 3, 4, 5]
try:
    while True:
        print(l.pop())
# note that we didn't use as variable, it is optional
except Exception:
    print("something unexpected happen")
print("code resumes here")

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(10 + "abc")

data = [10, 20, 10, 10, 5]
sum_data = 0
count_data = 0

for element in data:
    sum_data += element
    count_data += 1

average = sum_data / count_data
print(average)


data = []
sum_data = 0
count_data = 0

for element in data:
    sum_data += element
    count_data += 1
# ZeroDivisionError: division by zero
# average = sum_data / count_data
# print(average)


data = []
if len(data) == 0:
    average = 0
else:
    sum_data = 0
    count_data = 0

    for element in data:
        sum_data += element
        count_data += 1
    average = sum_data / count_data
    print(average)


# data = [10, 20]
# data = []
data = [10, 20, "abc"]
sum_data = 0
count_data = 0
try:
    for element in data:
        try:
            sum_data += element
            count_data += 1
        except TypeError:
            pass
    average = sum_data / count_data
except ZeroDivisionError:
    average = 0
except TypeError:
    average = 0
print(average)


try:
    print(1 / 0)
except Exception as ex:
    print(f"logging error: {ex}")
    # re raise the error
    # raise

print("program still running....")


try:
    raise ValueError("custom message")
except ValueError as ex:
    print(f"handled a ValueError: {ex}")
finally:
    print("this is always executed")

try:
    raise TypeError("custom message")
except ValueError as ex:
    print(f"handled a ValueError: {ex}")
finally:
    print("this is always executed")

try:
    print('nothing to see here')
except ValueError as ex:
    print(f"handled a ValueError: {ex}")
finally:
    print("this is always executed")


try:
    raise TypeError("custom message")
except ValueError as ex:
    print(f"handled a ValueError: {ex}")
    raise
finally:  # executed even when exception is re raised
    print("this is always executed")

