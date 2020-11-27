"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? If either user input is not a number.
2. When will a ZeroDivisionError occur? When either user input is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? yes, see below.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if numerator == 0 or denominator == 0:
        print("Please enter a number that is not 0.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
