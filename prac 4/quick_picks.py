import random

NUMBERS_PER_LINE = 6


def main():
    quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        generate_random()


def generate_random():
    number_list = []
    for i in range(NUMBERS_PER_LINE):
        random_number = random.randint(1, 45)
        while random_number in number_list:
            random_number = random.randint(1, 45)
        number_list.append(random_number)
        number_list = sorted(number_list)
    strip1 = str(number_list).strip("[]")
    strip2 = str(strip1).replace(",", "")
    print("{:>2}".format(strip2))


main()
