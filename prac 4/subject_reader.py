"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_details()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_lists = []
    for line in input_file:
        repr(line)  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list_of_lists.append(parts)
    print(list_of_lists)

    input_file.close()


def subject_details():
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.split(',')
        parts[2] = int(parts[2])
        print("{} is taught by {:12} and has {:>3} students".format(parts[0], parts[1], parts[2]))


main()
