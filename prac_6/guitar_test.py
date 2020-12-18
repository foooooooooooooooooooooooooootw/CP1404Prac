from prac_6.guitar import Guitar


Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

print("Get age: expected 98, got " + str(Gibson.get_age()))
print("Is vintage: expected True, got " + str(Gibson.is_vintage()))
