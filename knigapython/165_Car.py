# -*- coding: utf-8 -*-
class Car():
    '''простая модель автомобиля'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #подключили атрибут с исходным значением 0

    def get_descriptive_name(self):
        '''возвращает аккуратно оформатированое описание'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer (self):
        '''ввод пробега машины в милях'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    #def update_odometr(self, mileage):
      #  '''Устанавливает заданое значение на адометре'''
     #   self.odometer_reading = mileage

    def update_odometer(self, mileage):
        '''Устанавливает заданое значение на адометре. При попытке обратной подкрутки изменение отклоняется'''
        if mileage >= self.odometer_reading: # проверяет новое значение перед изменением атрибута
            # если показания нового значения больше или рабно текущему одометру, значению тогда можно изменить
            self.odometer_reading = mileage
        else: # иначе если значение меньше получается сообщение о недоступности
            print('You can"t roll back an adometr')

    def  increment_odometer(self, miles):
        '''увеличивает показания адаометра с заданым приращением'''
        self.odometer_reading += miles

my_used_car = Car('subaru', 'autback', 2014)
print(my_used_car.get_descriptive_name())

my_used_car.read_odometer() # изначально было столько миль
my_used_car.update_odometer(200) # обновли одометр с функцией скрцчивания
my_used_car.read_odometer() # вывели наш адометер
my_used_car.increment_odometer(500) # прибовляет к существующему адометру еще мили
my_used_car.read_odometer()  # обратно вывели одометер
my_used_car.increment_odometer(1000) # прибовляет к существующему адометру еще мили
my_used_car.read_odometer() # обратно вывели одометер

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer() # вывели что автомобил с 0 пробегом

my_new_car.odometer_reading = 23 # изменили атрибута одометр напрямую
my_new_car.read_odometer()

my_new_car.update_odometer(123) # создали метод который добовляет значение одометра
my_new_car.read_odometer()

