from prac_8.silver_service_taxi import SilverServiceTaxi


def main():
    half_hummer = SilverServiceTaxi()
    half_hummer.name = "Hummer"
    half_hummer.fuel = 100
    half_hummer.drive(18)
    print(half_hummer)


main()
