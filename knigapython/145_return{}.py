# -*- coding: utf-8 -*-
def build_person (first_name, last_name, age=''):
    '''возвращение словаря с информацией о человеке'''
    person = {'first':first_name, 'last':last_name}
    #print(person) # print можно не ввовдить

    if age: # добавили под функцию еще возраст
        person[age] = age
        return person  # возвращает person, но под функцией нужно ввести print


musician = build_person('yura', 'yankovski')
print(musician)