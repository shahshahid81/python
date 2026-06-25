import csv
import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


with open(get_file_path("actors.csv")) as f:
    for row in f:
        print(row)


with open(get_file_path("actors.csv")) as f:
    for row in f:
        row = row.strip()
        fields = row.split(",")
        print(fields)

with open(get_file_path("actors.csv")) as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for row in reader:
        print(row)
