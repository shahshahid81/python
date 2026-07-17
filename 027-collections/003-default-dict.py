from collections import defaultdict


my_dict = dict()
# KeyError: 'age'
# print(my_dict['age'])

# give default value of int which is 0, note that a callable (int in example) is needed else there is key error
my_dict = defaultdict(int)
print(my_dict["age"])
my_dict["some-value"] += 10
print(my_dict)

# defaultdict accepts any callable as its default factory.
# Whenever a missing key is accessed, it calls the factory and uses the returned value.
# Here, the lambda returns 18.
my_dict = defaultdict(lambda: 18)
print(my_dict["age"])
my_dict["some-value"] += 10
print(my_dict)

data = [1, 2, 4, 1, 2, 3, 4, 5, 3, 5, 1, 51]
frequency: dict[int, int] = defaultdict(int)
for value in data:
    frequency[value] += 1
print(frequency)

words = ["apple", "oranges", "banana", "cherry", "avacado", "berries"]
grouped_words = defaultdict(list)
for word in words:
    grouped_words[word[0]].append(word)
print(grouped_words)

tuple_list = [("A", 10), ("B", 4), ("A", 5), ("C", 7), ("B", 1)]
grouped_data = defaultdict(list)
for key, value in tuple_list:
    grouped_data[key].append(value)
print(grouped_data)
agg_grouped_data = {k: sum(v) for k, v in grouped_data.items()}
print(agg_grouped_data)
