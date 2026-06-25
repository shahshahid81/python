import csv
import os
from pprint import pprint


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


nasdaq = get_file_path("nasdaq.csv")

with open(nasdaq) as f:
    for _ in range(5):
        row = next(f)
        print(row)

with open(nasdaq) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


def parse_nasdaq(f_name):
    result = []
    with open(get_file_path(f_name)) as f:
        reader = csv.reader(f)
        headers = next(reader)
        result.append(headers)

        for row in reader:
            row[-1] = float(row[-1])
            result.append(row)
    return result


pprint(parse_nasdaq("nasdaq.csv"))

census = get_file_path("st-2001est-01.csv")

with open(census) as f:
    for _ in range(10):
        print(next(f))

with open(census) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open(census) as f:
    reader = csv.reader(f)

    headers = next(f)
    print(headers)

    for row in reader:
        area = row[0]
        data = row[1:]

        data = [area] + [int(field.replace(",", "")) for field in data]
        print(data)


def parse_census_data(file_name):
    result = []

    with open(file_name) as f:
        reader = csv.reader(f)

        headers = next(f)
        result.append(headers)

        for row in reader:
            area = row[0]
            data = row[1:]

            data = [area] + [int(field.replace(",", "")) for field in data]
            result.append(data)
    return result


pprint(parse_census_data(census))
