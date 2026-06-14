price = 100

while price > 90:
    print(f"price = {price} - waiting for the price to come down....")
    price -= 1
print(f"buying at {price}")

price = 100
while price < 50:
    print(f"price = {price}")
print("Done")

# infinite loop
# price = 100
# while price > 90:
#     print(price)
#     price += 10

data = [100, 200, 300, 400, 500]
print(data.pop())
print(data)

data = [100, 200, 300, 400, 500]

while len(data) > 0:
    last_element = data.pop()
    print(f"processing element: {last_element}")

print("=" * 50)
data = [100, 200, 300, 400, 500]
# note that range is set to length of data, not checked everytime, just computed once and we are changing length in loop body
for i in range(len(data)):
    print(f"\ni={i}")
    print(f"before removing element: {data}")
    last_element = data.pop(i)
    print(f"processing element: {last_element}")
    print(f"after removing element: {data}")
