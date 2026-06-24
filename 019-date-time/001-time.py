from time import perf_counter, sleep

start = perf_counter()
print(start)
end = perf_counter()
print(end)
print(start - end)

start = perf_counter()
sleep(3)
end = perf_counter()
elapsed = end - start
print(elapsed)

# note that gmtime is timezone and UTC is a standard, both are not same
from time import gmtime

print(gmtime(1_000_000_000))
print(gmtime(0))
print(gmtime(-1_000_000_000))

import time

# time in seconds since epoch
print(time.time())
print(gmtime(time.time()))

from time import time


current = gmtime(time())
print(current[0:2])
print(current.tm_year)

now = time()
tomorrow = now + (24 * 60 * 60)

print(gmtime(now), gmtime(tomorrow))
print(tomorrow - now)

from calendar import timegm

now_epoch = time()
print(now_epoch)

now_struct = gmtime(now_epoch)
print(now_struct)
# note that it truncates will seconds and doesn't return fraction after second.
print(timegm(now_struct))


now = gmtime(time())

from time import strftime

print(strftime("%Y/%m/%d", now))
print(strftime("%Y-%m-%d", now))
print(strftime("%A is the best day of the week!", now))

d = "12/11/10"
d = '2012-11-10'

from time import strptime
print(strptime(d, '%Y-%m-%d'))

s = 'Monday, April 18, in the year 2020 CE'
fmt = '%A, $B %d, in the year %Y CE'

print(strptime(s, fmt))

# ValueError: time data 'Monday, April 18, in the year 2020 CE' does not match format '%A, $B %d, in the year %Y CE'
# s = 'Monday, April 18, 2020'
# print(strptime(s, fmt))
