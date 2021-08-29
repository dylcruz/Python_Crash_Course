#from car import Car, ElectricCar
import car
import electric_car

my_tesla = electric_car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = car.Car('Volkswagen', 'beetle', 2016)
print("\n" + my_beetle.get_descriptive_name())