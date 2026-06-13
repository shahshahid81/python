message = "Definitive guide to Python"
print(message.upper())
print(message.lower())
print(message.title())

print("abc" == "ABC")
print("aBc".lower() == "abC".lower())

lower_alpha = "\u03b1"
upper_alpha = "\u0391"
print(lower_alpha, upper_alpha)
print(lower_alpha == upper_alpha)
print(lower_alpha.lower() == upper_alpha.lower())

snake = "🐍"
# Below is True since there is no lower or upper for the character, so same character is used
print(snake.lower() == snake.upper())

print(lower_alpha.casefold())
print(upper_alpha.casefold())
# casefold returns a value that normalize the case sensitive characters so it can be compared case insensitively
# This happens because there are some characters which behaves differently, check below where length is changing
print(lower_alpha.casefold() == upper_alpha.casefold())

street = "stra\N{LATIN SMALL LETTER SHARP S}e"
print(street)
print(street.upper())
print(len(street), len(street.upper()))

data = "STRASSE"
print(data.lower())
print(data.lower() == street.lower())
print(data.casefold() == street.casefold())

# Latin small letter e with circumflex
s1 = "ê"
# Latin small letter e, combining circumflex accent
s2 = "ê"

print(s1 == s2)

s1 = "\N{LATIN SMALL LETTER E WITH CIRCUMFLEX}"
print(s1)
s2 = "\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}"
print(s2)

print(s1.upper() == s2.upper())
print(s1.casefold() == s2.casefold())


name = "Peter "
print(name)
print(name.rstrip())
name = "\t Peter\tJones\t"
print(name)
print(name.strip())

s = "ababpythonabab"
print(s)
print(s.strip("ab"))
s = "abcabpythonabab"
print(s)
print(s.strip("ab"))

print("Python" + " " + "rocks!")

data = "Jones,Peter"
split_data = data.split(",")
last_name, first_name = split_data
print(data)
print(split_data)
print(last_name)
print(first_name)

data = ["item 1", "item 2", "item 3"]
print(",".join("ABCD"))

print("rock" in "Python rocks!")
print("rock".casefold() in "Python rocks!".casefold())

print("Python rocks".startswith("Python"))
print("Python rocks".endswith("rocks"))
print("Python rocks".casefold().endswith("rocks".casefold()))

message = "To every action there is always an equal and opposite reaction"

# index works on all sequences and raises error if index not found, find works on strings only
# index return first one
print(message.index("action"))
print(message.find("Newton"))

print(message.index("action", 9 + len("action")))
