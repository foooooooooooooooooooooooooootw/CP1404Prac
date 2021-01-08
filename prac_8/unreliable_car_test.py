from prac_8.UnreliableCar import UnreliableCar


def main():
    proton_saga = UnreliableCar()
    proton_saga.name = "proton_saga"
    proton_saga.fuel = 100
    proton_saga.drive(40)
    print(proton_saga)


main()
