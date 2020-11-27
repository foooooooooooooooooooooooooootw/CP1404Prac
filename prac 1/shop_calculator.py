total_price = 0.00

items = int(input("Number of items: "))

while items <= 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))

for i in range(items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print("Total price for {} items is ${:.2f}".format(items, total_price))
