# -*- coding: utf-8 -*-
# Если класс который вы пишите представляет специализированую версию ранее написаного класаа, вы можете воспользоваться НАСЛЕДОВАНИЕМ
# Один класс, наследующий от другого, автоматически получает все атрибуты и методы первого класса
# Исходный класс называется РОДИТЕЛЕМ, а новый ПОТОМКОМ.
# ПОТОМОК наследует все атрибуты и методы родителя, а также может определять собственные атрибуты и методы.
class Car(): # строиться экземпляр Car
    '''Простая модель автомобиля'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.adometer_reading = 0

    def get_descriptive_name(self):
        '''возвращает аккуратно оформатированое описание'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''ввод пробега машины в милях'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

        # def update_odometr(self, mileage):
        #  '''Устанавливает заданое значение на адометре'''
        #   self.odometer_reading = mileage

    def update_odometer(self, mileage):
        '''Устанавливает заданое значение на адометре. При попытке обратной подкрутки изменение отклоняется'''
        if mileage >= self.odometer_reading:  # проверяет новое значение перед изменением атрибута
            # если показания нового значения больше или рабно текущему одометру, значению тогда можно изменить
            self.odometer_reading = mileage
        else:  # иначе если значение меньше получается сообщение о недоступности
            print('You can"t roll back an adometr')

    def increment_odometer(self, miles):
        '''увеличивает показания адаометра с заданым приращением'''
        self.odometer_reading += miles




class ElectricCar(Car): # определяется класс потомок ElectricCar
    '''Предстовляет аспекты машины, специфические для электромобилей'''
    def __init__(self, make, model, year): # получает необходимую информацию для создания экземпляра Car
        '''Инициализирует атрибуты класса родителя'''
        super().__init__(make, model, year)
        self.battery_size = 70 # добавили новый атрибут
# super() функция которая позволяет связать потомка с родителем. Приказывает Python вызвать метод __init__() класса, родителя ElectricCar

    def describe_battery(self): # выводит информацию о батареи
        #выводит информацию о мощности аккомулятора
        print('This car has a ' + str(self.battery_size) + 'Kwh battery')

    def fill_gas_tank(self): # при  одинковых именнах методов родителя и потомка, будет вывполнятся только потомок
        #У электоромобилей нет бензобака
        print('This car does not need a gas tank')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()





