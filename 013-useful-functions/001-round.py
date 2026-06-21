print(round(0.325))
print(round(0.875))

# this will round to 14 because in case of tie, we round to the closest even digit, which is 14
print(round(13.5))

# this will round to 12 because in case of tie, we round to the closest even digit, which is 12
print(round(12.5))

print(round(0.125, 1))
print(round(0.125, 2))

# closest between 123450 and 123460 for 123456 is 123460, hence rounded there
print(round(123456, -1))

# closest between 123000 and 124000 for 123456 is 123000, hence rounded there
print(round(123456, -3))

# 1235 is between 1230 and 1240, both are same distance but 1240 is even hence rounded to 1240
print(round(1235, -1))

# 1245 is between 1240 and 1250, both are same distance but 1240 is even hence rounded to 1240
print(round(1245, -1))

print(round(0.125, 2))

# 0.325 is 0.32500000000000001110 and is slightly greater hence rounded to 0.33
print(round(0.325, 2))
print(format(0.325, "0.20f"))
