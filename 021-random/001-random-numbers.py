import random

for _ in range(5):
    # value between 0.00 to 0.99
    print(random.random())
print("#" * 50)

random.seed(0)
for _ in range(5):
    print(random.random())
print("#" * 50)

random.seed(0)
for _ in range(5):
    print(random.random())
print("#" * 50)

random.seed(1)
for _ in range(5):
    print(random.random())
print("#" * 50)

random.seed(1)
for _ in range(5):
    print(random.random())
print("#" * 50)

random.seed(None)
for _ in range(5):
    print(random.random())
print("#" * 50)

random.seed(None)
for _ in range(5):
    print(random.random())
print("#" * 50)

random.seed(0)
for _ in range(5):
    # random between 1 and 5
    print(random.randrange(1, 6))
print("#" * 50)


random.seed(0)
for _ in range(5):
    # random between 1 and 6
    print(random.randint(1, 6))
print("#" * 50)

random.seed(0)
for _ in range(3):
    print(random.randint(1, 6))
    print(random.randrange(1, 6))

for _ in range(3):
    print(random.randint(1, 3))

for _ in range(3):
    print(random.random())
print("#" * 50)

data_1 = [(1, 12.3), (2, 30.7), (3, 20.5), (4, 36.5)]
data_2 = [("a", 12.3), ("b", 30.7), ("c", 20.5), ("d", 36.5)]

for k, v in data_2:
    print(f"{k}|{'*' * round(v)}")
print()

data_3 = [("abc", 12.3), ("d", 30.7), ("ef", 20.5), ("ghij", 36.5)]
for k, v in data_3:
    print(f"{k}|{'*' * round(v)}")

s = "abc"
print(s.rjust(10))
print(s.rjust(10, "-"))

for k, v in data_3:
    print(f"{k.rjust(3)}|{'*' * round(v)}")

for k, v in data_3:
    print(f"{k.rjust(4)}|{'*' * round(v)}")

for k, v in data_3:
    print(f"{k.rjust(15)}|{'*' * round(v)}")

keys = [str(el[0]) for el in data_3]
print(keys)

key_lengths = [len(str(el[0])) for el in data_3]
pad = max(key_lengths)

print(pad)

for k, v in data_3:
    print(f"{k.rjust(pad)}|{'*' * round(v)}")


def chart_freq(data):
    pad = max([len(str(el[0])) for el in data])
    for k, v in data:
        print(f"{str(k).rjust(pad)}|{'*' * round(v)}")


chart_freq(data_1)
chart_freq(data_2)
chart_freq(data_3)

random.seed(0)

data = [random.randint(1, 10) for _ in range(5)]
print(data)

freq = {}
for elem in data:
    freq[elem] = freq.get(elem, 0) + 1
print(freq)


def freq_distribution(data):
    freq = {}
    for elem in data:
        freq[elem] = freq.get(elem, 0) + 1
    return freq


freq = freq_distribution(data)
print(freq)

sum_freq = sum(freq.values())
print(sum_freq)

relative_freq = freq.copy()

for k in relative_freq:
    relative_freq[k] = relative_freq[k] / sum_freq * 100

print(relative_freq)

relative_freq = {k: v / sum_freq * 100 for k, v in freq.items()}
print(relative_freq)


def relative_frequency(freq_dist):
    sum_freq = sum(freq_dist.values())
    return {k: v / sum_freq * 100 for k, v in freq_dist.items()}


print(data)
freq = freq_distribution(data)
print(freq)
relative_freq = relative_frequency(freq)
print(relative_freq)
chart_freq(relative_freq.items())
sorted_items = sorted(relative_freq.items(), key=lambda x: x[0])
print(sorted_items)
chart_freq(sorted_items)


def analyze_randint(n, a, b):
    data = [random.randint(a, b) for _ in range(n)]
    freq = freq_distribution(data)
    rel = relative_frequency(freq)
    sorted_items = sorted(rel.items(), key=lambda x: x[0])
    chart_freq(sorted_items)


print("#" * 50)
random.seed(0)
analyze_randint(10_000, 1, 10)

print(random.gauss(0, 1))


def analyze_normal(n, mean, standard_deviation):
    data = [round(random.gauss(mean, standard_deviation) * 10) for _ in range(n)]
    freq = freq_distribution(data)
    rel = relative_frequency(freq)
    sorted_items = sorted(rel.items(), key=lambda x: x[0])
    chart_freq(sorted_items)


print("#" * 50)
random.seed(0)
analyze_normal(100_000, 0, 1)


def analyze_normal(n, mean, standard_deviation):
    data = [round(random.gauss(mean, standard_deviation) * 10) for _ in range(n)]
    freq = freq_distribution(data)
    rel = relative_frequency(freq)
    filtered_items = {k: v for k, v in rel.items() if round(v) > 0}
    sorted_items = sorted(filtered_items.items(), key=lambda x: x[0])
    chart_freq(sorted_items)


print("#" * 50)
random.seed(0)
analyze_normal(100_000, 0, 1)
