import datetime

dt1 = datetime.datetime.now()
dt2 = datetime.datetime.fromisoformat("2026-01-01T00:00:00")

print(repr(dt1))
print(repr(dt2))

time_delta = dt1 - dt2
print(repr(time_delta))

# only below 3 data stored
print(time_delta.days)
print(time_delta.seconds)
print(time_delta.microseconds)

SECONDS_IN_HOUR = 24 * 60 * 60
SECONDS_IN_MICROSECONDS = 1 / 10**6

total_seconds = (
    time_delta.days * SECONDS_IN_HOUR
    + time_delta.seconds
    + time_delta.microseconds * SECONDS_IN_MICROSECONDS
)
print(total_seconds)
print(time_delta.total_seconds())

time_delta = datetime.timedelta(hours=2, minutes=30)
print(time_delta)
print(time_delta.days, time_delta.seconds, time_delta.microseconds)

dt = datetime.datetime.now(datetime.timezone.utc)
print(dt)
print(dt + time_delta)

s = "2020-02-15T13:35:00"
dt = datetime.datetime.fromisoformat(s)
print(dt)
start = datetime.datetime(year=dt.year, month=dt.month, day=1)
print(start)
start = datetime.date(year=dt.year, month=dt.month, day=1)
print(start)

delta = datetime.timedelta(hours=50, minutes=30)
print(start + delta)

if start.month == 12:
    new_year = start.year + 1
    new_month = 1
else:
    new_year = start.year
    new_month = start.month + 1

print(start, new_year, new_month)

end = datetime.date(year=new_year, month=new_month, day=1)
print(end)

print(end - datetime.timedelta(days=1))

end = end + datetime.timedelta(days=-1)
print(end)


def get_first_late(dt):
    start = datetime.date(year=dt.year, month=dt.month, day=1)
    if start.month == 12:
        new_year = dt.year + 1
        new_month = 1
    else:
        new_year = dt.year
        new_month = dt.month + 1
    end = datetime.date(year=new_year, month=new_month, day=1) + datetime.timedelta(
        days=-1
    )
    return start, end


s = "2020-02-15T13:35:00"
print(get_first_late(datetime.datetime.fromisoformat(s)))

for year in (2020, 2021):
    for month in range(12):
        dt = datetime.date(year=year, month=month + 1, day=15)
        print(dt, *get_first_late(dt))

t1 = datetime.time(9, 30, 0)
t2 = datetime.time(11, 0, 0)

print(t1 <= t2)

d1 = datetime.date(2022, 3, 8)
d2 = datetime.date(2022, 5, 1)
print(d1 < d2)

# TypeError: '<' not supported between instances of 'datetime.date' and 'datetime.time'
# print(d1 < t1)
