import datetime

print(datetime.date(2026, 6, 1))
print(datetime.date.today())

import time

print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.fromisoformat("2026-02-01"))

dt = datetime.date(2026, 3, 1)
print(dt.isoformat())
print(dt.year)
print(dt.month)
print(dt.day)

t = datetime.time(15, 25, 40)
print(t)

t = datetime.time(0, 0, 0)
print(t)

t = datetime.time(15, 25, 40, 135)
print(t)

t = datetime.time.fromisoformat("13:42:51:123")
print(t)

# micro seconds has to be 3 or 6 characters only as per iso format
# ValueError: Invalid isoformat string: '13:42:51:1234'
# t = datetime.time.fromisoformat('13:42:51:1234')
# print(t)

t = datetime.time.fromisoformat("13:42:51:123456")
print(t)

print(t.hour)
print(t.minute)
print(t.minute)
print(t.microsecond)


dt = datetime.datetime(2026, 4, 2, 13, 30, 45, 421)
print(dt)
print(dt.isoformat())

dt = datetime.datetime.fromisoformat("2026-04-03T16:30:45.000421")
print(dt)
print(dt.isoformat())
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

# local timezone date time
print(datetime.datetime.now())
# utc date time
print(datetime.datetime.utcnow())
print(datetime.datetime.now(datetime.timezone.utc))

s = "2025-04-02T21:30:00+05:30"
dt = datetime.datetime.fromisoformat(s)
print(dt)
print(dt.tzinfo)