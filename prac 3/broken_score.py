"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))


def grade_bracket():
    if score >= 90:
        return ("Excellent")
    elif score >= 50:
        return ("Passable")
    else:
        return ("Bad")


if score < 0 or score > 100:
    print("Invalid score")

else:
    print(grade_bracket())
