class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Car:", self.make, self.model, self.year)

    def start_engine(self):
        print("Engine started!")

my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info()
my_car.start_engine()
