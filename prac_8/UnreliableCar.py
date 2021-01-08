from prac_8.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=50):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}".format(super().__str__())

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        if random.uniform(0.0, 100.0) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0

        return distance_driven
