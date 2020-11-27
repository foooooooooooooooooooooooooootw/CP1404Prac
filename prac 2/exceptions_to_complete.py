finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number! "))  # TODO: this line
        finished = True  # TODO: this line
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
