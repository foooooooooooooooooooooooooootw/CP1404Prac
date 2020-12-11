"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    state_code = state_code.upper()
    if state_code in CODE_TO_NAME:
        print("{:3} is {}".format(state_code, CODE_TO_NAME[state_code]))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
    
code = []
state = []
state_no = 0
for i in CODE_TO_NAME:
    code.append(i)
    state.append(CODE_TO_NAME[i])
    print("{:3} is {}".format(code[state_no],state[state_no]))
    state_no += 1