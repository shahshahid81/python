import csv
import os


def get_file_path(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    return file_path


data = [
    ["First Name", "Last Name", "DOB", "Sketches"],
    [
        "John",
        "Cleese",
        "10/27/39",
        "The Cheese Shop, Ministry of Silly Walks, It's the Arts",
    ],
    ["Eric", "Idle", "3/29/43", 'The Cheese Shop, Nudge Nudge, "Spam"'],
    ["Peter", "O'Toole", "8/2/32", "Lawrence of Arabia"],
]

test_csv = get_file_path("test.csv")

with open(test_csv, "w") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)


with open(test_csv) as f:
    for row in f:
        print(row, end="")

csv.register_dialect("pdv", delimiter="|", quotechar="'", escapechar="\\")


with open(test_csv, "w") as f:
    writer = csv.writer(f, dialect="pdv")
    for row in data:
        writer.writerow(row)

csv.register_dialect(
    "pdv", delimiter="|", quotechar="'", escapechar="\\", doublequote=False
)


with open(test_csv, "w") as f:
    writer = csv.writer(f, dialect="pdv")
    for row in data:
        writer.writerow(row)

with open(test_csv) as f:
    for row in f:
        print(row, end="")
