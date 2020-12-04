numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

'---------------------------------'

numbers[0] = "ten"
numbers[6] = 1
numbers2 = numbers[2:7]

if 9 in numbers:
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")

print(numbers)
print(numbers2)
