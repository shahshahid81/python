import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


f = open(get_file_path("test.csv"), "w")
f.write("abc")
f.write("123456")
f.close()

with open(get_file_path("test.csv")) as f:
    print(f.readlines())

with open(get_file_path("test.csv"), "w") as f:
    f.write("abc\n")
    f.write("123456\n")

with open(get_file_path("test.csv")) as f:
    print(f.readlines())

data = [
    "line 1",
    "line 2",
    "line 3",
]

with open(get_file_path("test.csv"), "w") as f:
    f.writelines(data)

with open(get_file_path("test.csv")) as f:
    print(f.readlines())

data = [
    "line 1\n",
    "line 2\n",
    "line 3\n",
]

with open(get_file_path("test.csv"), "w") as f:
    f.writelines(data)

with open(get_file_path("test.csv")) as f:
    print(f.readlines())

data = [
    "line 1",
    "line 2",
    "line 3",
]

with open(get_file_path("test.csv"), "w") as f:
    f.writelines("\n".join(data))

with open(get_file_path("test.csv")) as f:
    print(f.readlines())

with open(get_file_path("test.csv")) as f:
    try:
        raise ValueError("Bogus")
    except:
        pass

print(f)
print(f.closed)

with open(get_file_path("test.csv")) as f:
    for line in f:
        print(line, end="")


with open(get_file_path("test.csv"), "a") as f:
    f.write("line4\n")
    f.write("line5\n")

with open(get_file_path("test.csv")) as f:
    for line in f:
        print(line.strip())

with open(get_file_path("does_not_exists.txt"), "a") as f:
    f.write("line 1")

with open(get_file_path("does_not_exists.txt")) as f:
    print(f.readlines())

with open(get_file_path("DEXUSEU.csv")) as f:
    for _ in range(5):
        print(next(f).strip())

with open(get_file_path("DEXUSEU.csv")) as f:
    data = f.readlines()

del data[0]
print(data[0:5])

data = [line.strip() for line in data]

print(data[0:5])

data = [line.split(",") for line in data]

print(data[0:5])


def split_date(date_str):
    return date_str[:4], date_str[5:7], date_str[8:]


print(split_date("2015-04-03"))


def transform_row_for_output(row):
    row = row.strip()
    dt_str, rate = row.split(",")
    year, month, date = split_date(dt_str)

    try:
        float(rate)
    except ValueError:
        return ""

    month = str(int(month))
    date = str(int(date))
    return ",".join([year, month, date, rate]) + "\n"


print(transform_row_for_output("2015-04-03,1.0990"))
print(transform_row_for_output("2015-07-03,."))


with open(get_file_path("DEXUSEU.csv")) as f:
    data = f.readlines()

del data[0]

target_file = get_file_path("output.csv")
with open(target_file, "w") as f:
    f.write("YEAR,MONTH,DAY,EXCH\n")
    for row in data:
        f.write(transform_row_for_output(row))

with open(target_file) as f:
    for row in f:
        print(row.strip())


def transform_file_batch(source_file, target_file):
    with open(get_file_path(source_file)) as f:
        data = f.readlines()

    del data[0]

    with open(get_file_path(target_file), "w") as f:
        f.write("YEAR,MONTH,DAY,EXCH\n")
        for row in data:
            f.write(transform_row_for_output(row))


transform_file_batch("DEXUSEU.csv", "output.csv")


def transform_file(source_file, target_file):
    with open(get_file_path(source_file)) as source:
        with open(get_file_path(target_file), "w") as target:
            next(source)
            f.write("YEAR,MONTH,DAY,EXCH\n")
            for row in source:
                target.write(transform_row_for_output(row))


with open(get_file_path("output.csv")) as f:
    data = f.readlines()
