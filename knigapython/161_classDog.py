# -*- coding: utf-8 -*-
class Dog(): # скобки пусты т.к. класс создается с нуля
    # Dog это экземпляр класса
    '''Простая модель собаки'''
# метод __init__  автоматически выполняется при создании каждого нового экземпляра на базе класса Dog
# метод __init__ с тремя параметрами self, name, age
# self ссылка на экземпляр,она предостовляет конкретному экземпляру доступ к атрибутам и методам класса
    def __init__(self, name, age):# приведена строка документации с кратким описанием класса
        '''инициализирует атрибуты name и age'''
        self.name = name # переменные к которы обращаются через класс называются атрибутами
        self.age = age

    def sit(self): # функция являющая частью класса называется методом
        '''собака садиться по команде'''
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        '''собака перекатываетсяч по команде'''
        print(self.name.title() + ' rolled over!')


#создадим класс представлящим канкретную собаку
# my_dog это отдельный экземпляр класса, созданный на базе класса Dog
my_dog = Dog('willie', 6)
print('My dogs name is ' + my_dog.name.title()) # обращение к атрибутам my_dog.name
print('My dog is ' + str(my_dog.age) + ' years old')

#вызов методов определенных в классе Dog
my_dog.sit()
my_dog.roll_over()


# создадим еще один экземпляр класса
your_dog = Dog('Richerd', 23)
print('My name is dog: ', your_dog.name)
print('My dog is ' + str(your_dog.age), 'years old')
your_dog.sit()
your_dog.roll_over()

