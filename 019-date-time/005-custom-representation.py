from datetime import time, date, datetime

t = time(22, 30, 45)
print(t.strftime("The time is: %I hours, %M minutes, and %S seconds, %p"))

d = date(2020, 5, 15)
print(d.strftime('%B %d, %Y'))

dt = datetime(2020, 5, 15, 22, 30, 45)
print(repr(dt.strftime('%I:%M %p on %B %d, %Y')))

dt = datetime.strptime('10:30 PM on May 15, 2020', '%I:%M %p on %B %d, %Y')
print(repr(dt))

print(repr(dt.isoformat()))
print(repr(dt.fromisoformat("2020-05-15T22:30:00")))
print(repr(dt.fromisoformat("2020-05-15T22:30:00-05:30")))
# Below is allowed by iso but not by python
# ValueError: Invalid isoformat string: '2020-05-15T22:30:00-0530'
# print(repr(dt.fromisoformat("2020-05-15T22:30:00-0530")))

