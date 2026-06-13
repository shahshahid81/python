print(ord("A"))
print(ord("α"))
print(ord("🐍"))

print(hex(ord("A")))
print(hex(ord("α")))
print(hex(ord("🐍")))

print(int("3B1", 16))  # base 16

α = "alpha"
print(α)

# characters similar to letter or numbers work for variable name, not others
# SyntaxError: invalid character '🐍' (U+1F40D)
# 🐍 = "snake"


# \N is named escape for a character
var = "\N{LATIN CAPITAL LETTER A}lways look on the bright side"
print(var)

# unicode character, lower case "u" using 4 digits only so that python know to read exactly 4 digits for a unicode character
var = "\u0041lways look on the bright side"
print(var)

# unicode character, upper case "U" using 8 digits only so that python know to read exactly 8 digits for a unicode character
var = "\U00000041lways look on the bright side"
print(var)

# lower u, so 4 characters
print("\u03b1")
# upper U so 8 digits
print("\U0001f40d")
print("\N{Grinning Face}")
print("\U0001f600")