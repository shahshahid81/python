import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
print(data)
# converts list into min heap, internally calls the less than operator to maintain the comparison
# for node i, left child = 2 * i + 1, right child = 2 * i + 2, parent = (i - 1) // 2
# i = 0, left child = 1, right child = 2
# i = 1, parent = 0; i = 2, parent = 0
heapq.heapify(data)
print(data)

copy = data[:]
# this will remove and maintain the min heap as well
print(heapq.heappop(data))
# this will just remove the data, min heap won't be maintained
print(copy.pop(0))

print(data)
heapq.heapify(copy)
print(copy)

print(data)
# this will add and maintain min heap as well
heapq.heappush(data, 4)
heapq.heappush(data, 19)
heapq.heappush(data, 21)
print(data)


class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}({self.priority})"

    def __repr__(self):
        return self.__str__()


low = Task(1, "Low")
medium = Task(2, "Medium")
high = Task(3, "High")
data = [medium, low, high]

print(data)
heapq.heapify(data)
print(data)
print(heapq.nsmallest(2, data))
print(heapq.nlargest(2, data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))


class Reverse(Task):
    def __lt__(self, other):
        # flip the lt operator to make max heap
        return self.priority > other.priority


print()
data = [medium, low, high]
data = [Reverse(el.priority, el.name) for el in data]
print(data)
heapq.heapify(data)
print(data)
print(heapq.nsmallest(2, data))
print(heapq.nlargest(2, data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
