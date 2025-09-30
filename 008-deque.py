# use deque since list is not optimized to remove from beginning
from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue)

queue.popleft()  # The first to arrive now leaves
queue.popleft()  # The second to arrive now leaves
print(queue)  # Remaining queue in order of arrival
