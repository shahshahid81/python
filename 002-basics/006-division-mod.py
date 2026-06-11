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
