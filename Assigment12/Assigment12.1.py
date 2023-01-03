class Vehicle:
    def __init__(self):
        self.speed = ...
        self.color = 'white'
        self.model = ...

    def turn_on(self):
        ...

    def turn_off(self):
        ...

    def gear_change(self):
        ...


class Airplane(Vehicle):
    def __init__(self):
        super().__init__()##********
        self.capacity = ...
        self.country = ...

    def fly():
        ...

class Car(Vehicle):
    def __init__(sel):
        super().__init__()##********
        self.number_of_wheels = ...
        self.license_plate = ...


jimbo = Airplane()
pride = Car()
bmw = Car()
benz = Car()
my_cars = [pride, bmw, benz, jimbo]

pride.license_plate = "sfsdfsd_sdf456"
pride.color = 'green'
