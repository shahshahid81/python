import statistics as stats

data = list(range(1, 11))
print(data)

print(stats.mean(data))
# fmean is faster but returns float
print(stats.fmean(data))

data = [1, 1, 2, 3, 4, 5, 6, 6]
# returns 3.5 which is (3+4)/2, following (a+b)/2, not present in the iterable
print(stats.median(data))
# returns a from median formula
print(stats.median_low(data))
# returns b from median formula
print(stats.median_high(data))

# returns the most common value, returns first in case of multiple
print(stats.mode(data))

# returns all of the most common value
print(stats.multimode(data))

data = ["one", "two", "three", "three", "four", "four"]
print(stats.mode(data))
print(stats.multimode(data))

import random

random.seed(0)

data = [random.gauss(0, 2) for _ in range(10_000)]
print(stats.fmean(data), stats.median(data))

print(stats.pstdev(data), stats.pvariance(data))
print(stats.stdev(data), stats.variance(data))
print(stats.quantiles(data, n=4))
print(stats.quantiles(data, n=4, method="inclusive"))

d1 = stats.NormalDist(0, 1)
print(d1)
print(d1.mean, d1.median, d1.mode, d1.stdev, d1.variance)
print(d1.cdf(0))
print(d1.cdf(3))

# increase mean
print(d1 + 10)
# increase sigma
print(d1 * 10)

d2 = 2 * d1 + 1
print(d2)

print(d1.overlap(d2))
print(d2.overlap(d1))
print(d1.quantiles(4))
print(d1, d2)
print(d1 + d2)
print(d1.variance, d2.variance, (d1 + d2).variance)

random.seed(0)
print(d1.samples(n=10))
