import random

l = [1, 2, 3, 4, 5]
# mutates the collection, only works with mutable sequences
random.shuffle(l)
# l is mutated after shuffle
print(l)

# below 2 shuffle has same sequence because of random having seed of 0
l = [1, 2, 3, 4, 5]
random.seed(0)
random.shuffle(l)
print(l)


l = [1, 2, 3, 4, 5]
random.seed(0)
random.shuffle(l)
print(l)

l = [1, 2, 3, 4, 5]
random.seed(0)
for _ in range(5):
    # choose a value from sequence, values can be repeated
    print(random.choice(l))

l = [1, 2, 3, 4, 5]
random.seed(0)
for _ in range(5):
    # choose a value from sequence, values can be repeated
    print(random.choice(l))

s = sorted(set("abcdef"))
print(s)
random.seed(0)
for _ in range(5):
    print(random.sample(s, 3))

try:
    # sample size larger than sequence size will throw error
    print(random.sample(s, 10))
except ValueError as ex:
    print(ex)

random.seed(0)
for _ in range(5):
    print(random.randrange(2, 100, 2))

random.seed(0)
print([random.randrange(2, 100, 2) for _ in range(5)])

from time import perf_counter

start = perf_counter()
for _ in range(100):
    sample = random.sample(range(2, 1_000_000, 2), 10_000)
end = perf_counter()
print(f"elapsed = {end - start}")

start = perf_counter()
for _ in range(100):
    sample = [random.randrange(2, 1_000_000, 2) for _ in range(10_000)]
end = perf_counter()
print(f"elapsed = {end - start}")

s = 1, 2, 3, 4, 5, 6
random.seed(11)
for _ in range(5):
    # with repitition, numbers can be repeated
    print(random.choices(s, k=2))


def chart_freq(data):
    pad = max([len(str(el[0])) for el in data])
    for k, v in data:
        print(f"{str(k).rjust(pad)}|{'*' * round(v)}")


def freq_distribution(data):
    freq = {}
    for elem in data:
        freq[elem] = freq.get(elem, 0) + 1
    return freq


def relative_frequency(freq_dist):
    sum_freq = sum(freq_dist.values())
    return {k: v / sum_freq * 100 for k, v in freq_dist.items()}


def frequency_distribution_matrix(data):
    linearized = [el for row in data for el in row]
    return freq_distribution(linearized)


random.seed(0)
population = tuple("abcdefghij")
data = [random.choices(population, k=5) for _ in range(3)]
print(data)
print(frequency_distribution_matrix(data))


def analyze_choices(base_data, num_choices, choice_size, weights=None):
    data = [
        random.choices(base_data, k=choice_size, weights=weights)
        for _ in range(num_choices)
    ]
    freq = frequency_distribution_matrix(data)
    rel = relative_frequency(freq)

    sorted_items = sorted(rel.items(), key=lambda x: x[0])
    chart_freq(sorted_items)


random.seed(0)
base_data = tuple("abcdefghij")
analyze_choices(base_data, 10_000, 5)

weights = [1] * 10
weights[0] = 2
weights[1] = 3
weights[-1] = 4
print(weights)
analyze_choices(base_data, 10_000, 5, weights=weights)
