def main():

    minimum_length = 8
    password = get_password(minimum_length)

    for i in range(len(password)):
        print("*", end='')


def get_password(minimum_length):
    password = input("Enter your password: ")
    while len(password) < minimum_length:
        print("Your password is too short.")
        print("Minimum length is {} characters".format(minimum_length))
        password = input("Enter your password: ")
    return password


main()

