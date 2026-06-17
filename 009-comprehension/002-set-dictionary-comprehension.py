widget_sales = [
    {"name": "widget 1", "sales": 10},
    {"name": "widget 2", "sales": 5},
    {"name": "widget 3", "sales": 0},
]

sales_by_widget = {}
for d in widget_sales:
    widget_name = d["name"]
    sales = d["sales"]
    sales_by_widget[widget_name] = sales
print(sales_by_widget)

sales_by_widget = {}
for d in widget_sales:
    sales_by_widget[d["name"]] = d["sales"]
print(sales_by_widget)

sales_by_widget = {}
for d in widget_sales:
    if d["sales"] > 0:
        sales_by_widget[d["name"]] = d["sales"]
print(sales_by_widget)

sales_by_widget = {d["name"]: d["sales"] for d in widget_sales if d["sales"] > 0}
print(sales_by_widget)

paragraph = """
To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to.
"""

punctuation = ",.!:-\n"
for char in punctuation:
    paragraph = paragraph.replace(char, " ")
print(paragraph)

# default split by space
all_words = paragraph.split()

words = {word.lower() for word in all_words if len(word) > 4}

print(words)

data = ["a", "a", "a", "b", "b", "c", "c", "c", "d"]

freq = {"a": 3, "b": 2, "c": 3, "d": 1}

freq = {}
for element in set(data):
    count = len([char for char in data if char == element])
    freq[element] = count
print(freq)

freq = {
    element: len([char for char in data if char == element]) for element in set(data)
}
print(freq)


from collections import Counter

data = ["a", "a", "a", "b", "b", "c", "c", "c", "d"]

freq = Counter(data)
print(freq)
print(dict(freq))

paragraph = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum."""
freq = Counter(paragraph)
print(dict(freq))

ignored = " ,.\n"
freq = Counter(paragraph.casefold())
print(dict(freq))

freq = {
    key: value
    for key, value in freq.items()
    if key not in ignored
}
print(freq)

freq = {
    key: value
    for key, value in dict(Counter(paragraph.casefold())).items()
    if key not in ignored
}
print(freq)

freq = {
    key: value
    for key, value in Counter(paragraph.casefold()).items()
    if key not in ignored
}
print(freq)