name = input("Enter your name: ").strip()
if name == "":
    print("Please enter text.")
else:
    file = open("name.txt", "w")
    file.write(name)
    file.close()

file = open("name.txt", "r")
name = file.readline()
if name == "":
    print("The text file is empty.")
else:
    print("Your name is {}".format(name))
file.close()

file2 = open("numbers.txt", "r")
number1 = file2.readline()
number2 = file2.readline()
number3 = int(number1) + int(number2)
print(number3)
file.close()

file2 = open("numbers.txt", "r")
total = 0
numbers = file2.readlines()
for number in numbers:
    number = float(number)
    total += number
print(total)
file2.close()
