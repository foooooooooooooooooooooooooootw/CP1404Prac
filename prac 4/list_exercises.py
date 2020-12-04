NUMBER_OF_NUMBERS = 5
Number_list = []

for i in range(NUMBER_OF_NUMBERS):
    current_number = float(input("Number: "))
    Number_list.append(current_number)

print("The first number is {}".format(int(Number_list[0])))
print("The last number is {}".format(int(Number_list[4])))
print("The smallest number is {}".format(int(min(Number_list))))
print("The largest number is {}".format(int(max(Number_list))))
print("The average of the numbers is {}".format(sum(Number_list) / len(Number_list)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
login = input("What's your username? ")
if login in usernames:
    print("Access Granted")
else:
    print("Access Denied")
