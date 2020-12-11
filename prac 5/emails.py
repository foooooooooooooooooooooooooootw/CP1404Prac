emails = ["lindsay.ward@jcu.edu.au", "abe@gmail.com"]
names = ["Lindsay Ward", "Abe"]
database = {"lindsay.ward@jcu.edu.au": "Lindsay Ward", "abe@gmail.com": "Abe"}
email = input("Email: ")

program_started = 1

while program_started == 1:

    if email == "":
        program_started = 0


    elif database.get(email) is not None:
        check = input("is your name {}? (Y/n) ".format(database.get(email)))

        if check.upper() not in ("", "Y", "N", "YES", "NO"):
            print("Invalid input.")
            check = input("is your name {}? (Y/n) ".format(database.get(email)))

        elif check.upper() == "Y" or check == "" or check.upper() == "YES":
            email = input("Email: ")

        elif check.upper() == "N" or check.upper() == "NO":
            name = input("Name: ")

    elif database.get(email) == None:
        split_email = email.split("@")
        possible_name = split_email[0].title()
        guess = input("Is your name {}? (Y/n) ".format(possible_name))

        if guess.upper() not in ("", "Y", "N", "YES", "NO"):
            print("Invalid input.")
            guess = input("Is your name {}? (Y/n) ".format(possible_name))

        elif guess.upper() == "Y" or guess == "" or guess.upper() == "YES":
            database[email] = possible_name
            email = input("Email: ")

        elif guess.upper() == "N" or guess.upper() == "NO":
            real_name = input("Name: ")
            database[email] = real_name
            email = input("Email: ")

print(" ")
for i in database:
    print("{} ({})".format(database[i], i))
