# -*- coding: utf-8 -*-
from car import Car, ElectricCar# из файла импортировали наш класс
# все работает хоть и красным светиться

my_new_car = Car('audi', 'a5', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'roadster', 2016) # создали по классу автомобиль электро
print(my_tesla.get_descriptive_name())