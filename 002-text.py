text1 = 'spam eggs'  # single quotes
text2 = "Paris rabbit got your back :)! Yay!"  # double quotes
text3 = '1975'  # digits and numerals enclosed in quotes are also strings

print('doesn\'t')  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), special characters are interpreted, so \n produces new line

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote, raw strings, don't escape anything,  a raw string may not end in an odd number of \ characters, else it will escape the last string quote

# Can use 3 single quotes as well for multiline
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3 * 'un' + 'ium')

# String literal with space in between are concatenated, notice that there is no space after concatenation. Only works with string literals.
print('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')

print(text)

prefix = 'Py'
# print(prefix 'thon')  # can't concatenate a variable and a string literal
print(prefix + 'thon')

word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5

print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])
# print(word[-7]) # index out of range error
print(word[0:2])  # Py, position 2 excluded
print(word[2:5])  # tho, position 5 excluded
# character from the beginning (0th index) to position 2 (excluded)
print(word[:2])
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end (-1)

print(word[:2] + word[2:])
print(word[:4] + word[4:])

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   
-6  -5  -4  -3  -2  -1
"""

# out of range slice indexes are handled gracefully when used for slicing
print(word[4:42])
print(word[42:])

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error
# word[0] = 'J'
# word[2:] = 'py'
# There is also no mutable string type, but str.join() or io.StringIO can be used to efficiently construct strings from multiple fragments.

print('J' + word[1:])
print(word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print(len(s))
