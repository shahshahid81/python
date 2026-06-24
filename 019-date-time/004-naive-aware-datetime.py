# naive are ones without timezone and aware are ones with timezone

from datetime import datetime, timedelta, timezone

s = "2020-03-15T13:30:00-07:00"

print(repr(datetime.fromisoformat(s)))

td = timedelta(days=-1, seconds=61200)
print(td.total_seconds() // 60 // 60)

tz_EDT = timezone(timedelta(hours=-4), "EDT")
print(repr(tz_EDT))
print(repr(timezone.utc))
tz_CDT = timezone(timedelta(hours=-5), "CDT")

# aware date time
dt = datetime(year=2020, month=5, day=15, hour=22, minute=30, tzinfo=tz_EDT)
print(repr(dt))

print(repr(dt.astimezone(tz_CDT)))
dt_utc = dt.astimezone(timezone.utc)
print(repr(dt_utc))
print(repr(dt_utc.replace(tzinfo=None)))

s = "2020-03-15T13:30:00-04:00"

dt_aware = datetime.fromisoformat(s)
dt_utc = dt_aware.astimezone(timezone.utc)
dt_naive = dt_utc.replace(tzinfo=None)
print(repr(dt_naive))

dt_naive = datetime.fromisoformat("2020-03-15T13:30:00")
dt_aware = dt_naive.replace(tzinfo=timezone.utc)
print(repr(dt_aware))


tz_EDT = timezone(timedelta(hours=-4), "EDT")
tz_CDT = timezone(timedelta(hours=-5), "CDT")
print(repr(dt_aware.astimezone(tz_EDT)))
print(repr(dt_aware.astimezone(tz_CDT)))
