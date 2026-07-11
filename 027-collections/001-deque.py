from collections import deque
from typing import Any

d: deque[Any] = deque("hello")
print(d)

d.append("4")
# add to start in O(1) because internal it is doubly linked list
d.appendleft(5)
print(d)

print(d.pop())
# remove from start in O(1) because internal it is doubly linked list
print(d.popleft())
print(d)

d.clear()
print(d)

d.extend("456")
print(d)
# note that things are added in reverse so output is 1 2 3
d.extendleft([3, 2, 1])
print(d)

# shift all elements one to the left
d.rotate(-1)
print(d)

# shift all elements one to the right
d.rotate(1)
print(d)

d = deque("hello", maxlen=5)
print(d)

d.append(1)
print(d)

d.append([1, 2, 3])
print(d)
print(d.maxlen)
