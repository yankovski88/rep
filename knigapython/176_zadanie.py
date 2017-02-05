# -*- coding: utf-8 -*-
class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type, ):
        self.restaurant_name = restaurant_name
        self.cuisne_type = cuisine_type
        self.number_server = 4


    def describe_restaurant(self):
        print('Ресторан называется - ', self.restaurant_name)
        print('кухня ресторана - ', self.cuisne_type)
        print('обслужено человек - ', self.number_server)

    def set_number_served(self,person):
        '''изменяем колличество обслуженых'''
        self.number_server = person

    def increment_number_served(self, uvel_obsluj):
        '''доприбовляем колличество обслуженых людей к сущецствующим'''
        if uvel_obsluj >= self.number_server:
            self.number_server += uvel_obsluj

    def open_restaurant(self):
        print('Restaurant opened')

class IceCreamStand(Restaurant): # создаем потомка
    def __init__(self, restaurant_name, cuisine_type,): # выводим что наследовать
        super().__init__(restaurant_name, cuisine_type,) # прописываем функцию наследования
        self.flavors = ['rosin', 'tulpanin']

    def flav(self):
        print('сорта - ', self.flavors)

icecream = IceCreamStand('Ресторан мороженого', 'сладкая кухня') #данные о специализированом ресторане
icecream.describe_restaurant() # функция вывода данных
icecream.flav() # выввели наш дополнительный отрибут

















