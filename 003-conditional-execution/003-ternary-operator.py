ask_price = 100
if ask_price > 50:
    volume = 50
else:
    volume = 80
print(volume)

ask_price = 100
volume = 50 if ask_price > 50 else 80
print(volume)

a = 20
b = 10
distance = a - b if a > b else b - a
print(distance)

MISSING_VALUE = -999
current_value = 100
running_total = 15000
running_count = 125

if current_value == MISSING_VALUE:
    clean_value = 0
else:
    clean_value = current_value
running_total = running_total + clean_value

MISSING_VALUE = -999
current_value = 100
running_total = 15000
running_count = 125

clean_value = 0 if current_value == MISSING_VALUE else current_value
running_total = running_total + clean_value
