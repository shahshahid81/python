import decimal
from decimal import Decimal

d = Decimal(100)
print(repr(d))

# float is passed, so this is not exact representation
d = Decimal(0.1)
print(repr(d))

d = Decimal("0.1")
print(repr(d))

print(repr(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3")))

print(repr(Decimal("0.1") * Decimal("0.3")))
print(repr(Decimal("1") / Decimal("8")))
# infinite numbers are maxed at some precision, default is 28
print(repr(Decimal("1") / Decimal("3")))
print(decimal.getcontext())

# round internally proxies to the type of value, so both float and decimal works, internally, their round is called
print(repr(round(0.1234, 3)))
print(repr(round(Decimal("0.1234"), 3)))
print(repr(round(Decimal("0.135"), 2)))
print(repr(round(Decimal("0.145"), 2)))

# note that 1.20 is preserved as is, not converted to 1.2
d1 = Decimal("1.20")
print(repr(d1))

# note that 2.00 is preserved as is, not converted to 2 or 2.0
d2 = Decimal("2.00")
print(repr(d2))

print(repr(d1 * d2))

# note that decimal stores the exact representation that was passed as string, even if it is more than precision
d1 = Decimal("1.123456789012345678901234567890")
print(len("1.123456789012345678901234567890"))
print(repr(d1))

# note that precision is not same as defined
print(repr(+d1))
# below is output of above, note the len, precision is 28
print(len("1.123456789012345678901234568"))

print(repr(Decimal(10) // Decimal(3)))
print(repr(Decimal(10) % Decimal(3)))
print(repr(Decimal("0.1") ** Decimal(5)))

print(
    repr(
        sum(
            [
                Decimal("0.1"),
                Decimal("0.1"),
                Decimal("0.1"),
            ]
        )
    )
)

import math

d1 = Decimal("2.0")

result = math.sqrt(d1)
print(result)
print(type(result))
# internal methods available that returns Decimal instead of float returned by math library
print(repr(d1.sqrt()))


import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


dexuseu = get_file_path("DEXUSEU.csv")
with open(dexuseu) as f:
    for _ in range(5):
        print(next(f).strip())

import csv

with open(dexuseu) as f:
    reader = csv.reader(f)
    for _ in range(5):
        print(next(reader))

from datetime import datetime


def load_data(f_name, dt_format, use_decimal=False):
    with open(f_name) as f:
        reader = csv.reader(f)
        next(reader)

        data = [
            (
                datetime.strptime(row[0], dt_format),
                Decimal(row[1]) if use_decimal else float(row[1]),
            )
            for row in reader
            if row[1] != "."
        ]
    return data


dt_format = "%Y-%m-%d"

data_float = load_data(dexuseu, dt_format)
data_dec = load_data(dexuseu, dt_format, use_decimal=True)

print(data_float[0])
print(format(data_float[0][1], "0.28f"))
print(data_dec[0])

from time import perf_counter

start = perf_counter()
for _ in range(10_000):
    result = sum(row[1] for row in data_float)
end = perf_counter()
print(f"elapsed = {end - start}, result = {result}")

start = perf_counter()
for _ in range(10_000):
    result = sum(row[1] for row in data_dec)
end = perf_counter()
print(f"elapsed = {end - start}, result = {result}")
