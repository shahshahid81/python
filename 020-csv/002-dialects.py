import csv
import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


print(csv.list_dialects())

with open(get_file_path("actors.pdv")) as f:
    for row in f:
        print(row.strip())

with open(get_file_path("actors.pdv")) as f:
    reader = csv.reader(
        f, delimiter="|", quotechar="'", escapechar="\\", skipinitialspace=True
    )
    for row in reader:
        print(row)

csv.register_dialect(
    "pdv", delimiter="|", quotechar="'", escapechar="\\", skipinitialspace=True
)


print(csv.list_dialects())


with open(get_file_path("actors.pdv")) as f:
    reader = csv.reader(f, dialect="pdv")
    for row in reader:
        print(row)
