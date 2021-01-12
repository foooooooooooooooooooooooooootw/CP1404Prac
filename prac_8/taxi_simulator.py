from prac_8.taxi import Taxi
from prac_8.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():

    program_started = 1
    choice = input("q)uit, c)hoose taxi, d)rive" + "\n" + ">>> ")
    current_taxi = None
    total_bill = 0.0

    while program_started == 1:

        if choice.lower() not in ["q", "c", "d"]:
            print("invalid input")
            choice = input("q)uit, c)hoose taxi, d)rive" + "\n" + ">>> ")

        elif choice.lower() == "q":
            print("Total trip cost: ${:.2f}".format(total_bill))
            print("Taxis are now:")
            print("0 - {}".format(taxis[0]))
            print("1 - {}".format(taxis[1]))
            print("2 - {}".format(taxis[2]))
            break

        elif choice.lower() == "c":
            print("Taxis available:")
            print("0 - {}".format(taxis[0]))
            print("1 - {}".format(taxis[1]))
            print("2 - {}".format(taxis[2]))
            current_taxi = int(input("Choose taxi: "))
            print("Bill to date: ${:.2f}".format(total_bill))
            choice = input("q)uit, c)hoose taxi, d)rive" + "\n" + ">>> ")

        elif choice.lower() == "d":
            taxis[current_taxi].start_fare()
            distance = int(input("Drive how far? "))
            taxis[current_taxi].drive(distance)
            print(taxis[current_taxi])
            total_bill += float(taxis[current_taxi].get_fare())
            print("Your {} trip cost you ${}".format(taxis[current_taxi].name, taxis[current_taxi].get_fare()))
            print("Bill to date: ${:.2f}".format(total_bill))
            choice = input("q)uit, c)hoose taxi, d)rive" + "\n" + ">>> ")



main()