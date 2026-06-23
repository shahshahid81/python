import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "DEXUSEU.csv")

file = open(file_path, "r")
print(file.name)
print(file.readable())
print(file.writable())
print(file.closed)
file.close()
print(file.closed)


f = open(file_path)
data = f.readlines()
f.close()
print(data)

f = open(file_path)
print("Reading started...")
for line in f:
    print(line, end="")
print("Reading completed.")

print("Reading started...")
# f is iterator so this won't print anything
for line in f:
    print(line, end="")
print("Reading completed.")
f.close()

f = open(file_path)
print(next(f))
print(next(f))
print(next(f))
f.close()

# f = open(file_path)
# try:
#     for row in f:
#         print(row)
#         raise ValueError("forcing an exception...")
# finally:
#     print("closing the file...")
#     f.close()
# print(f.closed)

with open(file_path) as f:
    print(f.closed)
print(f.closed)

with open(file_path) as f:
    headers = next(f)

    for row in f:
        row = row.strip()
        data, value_str = row.split(",")
        print(data, value_str)

data = []
with open(file_path) as f:
    headers = next(f)

    for row in f:
        row = row.strip()
        date, value_str = row.split(",")
        try:
            value = float(value_str)
            data.append((date, value))
        except ValueError:
            pass

print(data)
