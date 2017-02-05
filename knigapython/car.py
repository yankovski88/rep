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




class Battery(): # определили новый класс который не наследует другие классы
    '''Простая модель аккумулятора автомобиля'''
    def __init__(self, battery_size=70): # получает один параметр
        '''Инициализирует атрибуты аккумулятора'''
        self.battery_size = battery_size

    def describe_battery(self):  # выводит информацию о батареи (добавили еще метод)
        '''выводит информацию о мощности аккомулятора'''
        print('This car has a ' + str(self.battery_size) + 'Kwh battery')

    def get_range(self):
        '''выводит приблизительный запас хода для аккумулятора'''
        if self.battery_size == 70: # если мощность равна 70 то: растояние 240
            range = 240
        message = 'This car can go approximately ' + str(range)  + ' and ' + str(self.battery_size)
        print(message)


    def upgrade_battery(self):
        if self.battery_size <= 85:
            battery_size = 85 # ст 176 Задание 9-9 СДЕЛАТЬ!!!!!!!!!!!!!
            print('зарядка на : 85% ')





class ElectricCar(Car): # определяется класс потомок ElectricCar
    '''Предстовляет аспекты машины, специфические для электромобилей'''
    def __init__(self, make, model, year): # получает необходимую информацию для создания экземпляра Car
        '''Инициализирует атрибуты класса родителя'''
        super().__init__(make, model, year)
        self.battery = Battery() # добавили новый атрибут, строка приказывает Pythony создать новый экземпляр Battery(со значение,battery_size)

# super() функция которая позволяет связать потомка с родителем. Приказывает Python вызвать метод __init__() класса, родителя ElectricCar