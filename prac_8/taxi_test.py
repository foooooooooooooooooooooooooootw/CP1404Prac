from prac_8.taxi import Taxi


def main():

    Prius1 = Taxi()
    Prius1.name = "Prius 1"
    Prius1.fuel = 100
    Prius1.price_per_km = 1.23
    Prius1.drive(40)
    print(Prius1)
    Prius1.start_fare()
    Prius1.drive(100)
    print(Prius1)


main()

