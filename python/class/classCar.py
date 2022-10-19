class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas = 32

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self) -> None:
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print(f"The Car need min : {self.gas} L")

class ElectricCar(Car):
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year) # To call superClass method and gives all attributes that defined for super class
        self.battery = Battery()


    def fill_gas_tank(self): # we can overwrite a method that exist in parent class , we use it instead of upper class
        print("This car has not gas")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.") 

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # Access to another class 

