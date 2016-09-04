from point import Point


class OutOfFuel(Exception):
    pass


class ToMuchFuel(Exception):
    pass


class Car:
    def __init__(self, model="Mercedes", capacity=60, consumption=0.6,
                 location=Point(0, 0)):
        self.model = model
        self.fuel_amount = 0
        self.fuel_capacity = capacity
        self.fuel_consumption = consumption
        self.location = location

    def drive(self, destination):
        length = self.location.distance(destination)
        fuel_needed = length * self.fuel_consumption
        if fuel_needed > self.fuel_amount:
            raise OutOfFuel()
        self.fuel_amount -= fuel_needed
        self.location = destination

    def drive_to_point(self, x, y):
        destination = Point(x, y)
        self.drive(destination)

    def refill(self, fuel):
        self.fuel_amount += fuel
        if self.fuel_amount > self.fuel_capacity:
            self.fuel_amount = self.fuel_capacity
            raise ToMuchFuel()

    def __str__(self):
        return 'Model: {0}\nfuel capacity: {1}\nfuel amount: {2}\n' \
               'fuel consumption: {3}\ncar location: {4}\n'\
               .format(self.model, self.fuel_capacity, self.fuel_amount,
                       self.fuel_consumption, self.location)


volvo = Car('Volvo', 50, 0.5, Point(2, 3))

print volvo
volvo.refill(35)
volvo.drive(Point(15, 14))
print volvo



