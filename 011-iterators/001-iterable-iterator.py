l = [1, 2, 3]
# iter used to create an iterator from iterables
iterator = iter(l)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# StopIteration exception, iterator is empty
# print(next(iterator))

iterator = iter(l)
print(id(iterator))
iterator = iter(l)
print(id(iterator))
print(next(iterator))


l = [1, 2, 3, 4, 5]
# for loop creates a iterator and looping through it
for element in l:
    print(l)

iterator = iter(l)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    pass

r = range(10)
print(r)
r_iter = iter(r)
print(next(r_iter))
print(next(r_iter))
# create list of only the pending items
print(list(r_iter))

# range is lazy iterable, computed only when next is called
r = range(100_000_000)

for i in range(100_000_000):
    print(i)
    if i > 4:
        break

r = range(10)
print(list(r))
print(list(r))

enum = enumerate("abc")
print(list(enum))
print(list(enum))
# StopIteration
# print(next(enum))

print(list(enumerate("abc")))
print(iter(enum) is enum)
