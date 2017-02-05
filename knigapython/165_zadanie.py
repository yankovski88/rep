# -*- coding: utf-8 -*-
class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
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




restaurant = Restaurant('Cenno', 'russkaya')
restaurant.number_server = 5 # изменили колличество обслуженых на прямую
restaurant.open_restaurant()
restaurant.set_number_served(100) # изменили кол. обслуженых через метод
restaurant.describe_restaurant()
restaurant.increment_number_served(1000) # брибавли к существующ 100 еще 1000 обслуженых
restaurant.describe_restaurant()

restaurant2 =Restaurant('Словянка', 'belaruskaya')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Minsk', 'ispanskaia')
restaurant3.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, age, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.login_attempts = 3
    def describe_user(self):
        print(self.first_name.title(),)
        print(self.last_name, )
        print(self.age)
        print(self.status)
        print(self.login_attempts)

    def increment_login_attempts(self, i):
        '''уыеличивает login_attempts на 1'''
        self.login_attempts += i

    def reset_login_attempts(self):
        '''обнуляте login_attempts'''
        self.login_attempts = 0
        print('должно обнулить')

    def greet_user(self):
        print('Hello', self.first_name.title())

user = User('yura', 'yankovski', '25', 'сложно')
#user.describe_user()
#user.greet_user()

user.reset_login_attempts() # все работает обнуляет
user.describe_user()
user.increment_login_attempts(1122) # добавили добовляет 1(1122)
user.describe_user()

#user2 = User('kolia', 'yankovski', '22', 'добре')
#user2.describe_user()
#user2.greet_user()








