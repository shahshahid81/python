a = 10
b = 3
print(a / b)
print(a // b)

print(-12 / 5)
# integer division takes floor of value instead of truncating the fraction, hence output is -3 instead of -2
print(-12 // 5)

print(10 % 3)
print(4 % 2)
print(5 % 2)
print(13567 % 2)

elapsed_minutes = 165
hours = elapsed_minutes // 60
# Below is same as mod, we remove the above division value from remainder to get remainder
# remaining_minutes = elapsed_minutes - (elapsed_minutes // 60 * 60)
remaining_minutes = elapsed_minutes % 60
print(hours, remaining_minutes)

total = 0
for i in range(1, 1_001):
    total += i
    if i % 100 == 0:
        print(f"total = {total}...")
print(f"Final total = {total}")

# Python's modulo (%) behaves differently from languages like C, C++, Java, and JavaScript
# when negative numbers are involved.
#
# Let:
#   a = dividend
#   b = divisor
#
# Python guarantees:
#     a == (a // b) * b + (a % b)
#
# Integer division (//) takes the floor of the result instead of truncating
# the fractional part.
#
# Example:
#   -7 / 3 = -2.333...
#   Python:             -7 // 3 = -3  (floor)
#   C/C++/Java/JS:      -7 / 3  = -2  (truncate)
#
# Since Python uses floor division, the remainder (%) always has the same
# sign as the divisor (b).
#
# In contrast, C/C++/Java/JavaScript use truncating division, so the
# remainder has the same sign as the dividend (a).

print(7 % 3)     # 1

print(-7 % 3)    # 2
# Python:  -7 // 3 = -3
#           -7 = (-3 * 3) + 2
# C/C++/Java/JavaScript: -1

print(7 % -3)    # -2
# Python:  7 // -3 = -3
#           7 = (-3 * -3) + (-2)
# C/C++/Java/JavaScript: 1

print(-7 % -3)   # -1
# Same result in Python and C/C++/Java/JavaScript