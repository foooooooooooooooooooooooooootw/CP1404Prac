from prac_8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name = "", fuel = 0, fanciness = 2):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        self.current_fare_distance = 0


    def __str__(self):
        return "{}, plus flagfall of ${:.2f}, total ${}".format(super().__str__(), self.flagfall, self.get_fare())

    def get_fare(self):
        return (super().get_fare()) + self.flagfall

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        return distance_driven