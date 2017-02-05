# -*- coding: utf-8 -*-
# проверка возраста и цена билета
# нужно для проверки одного условия когда оно появляется программа прекращает работу
age = 18
age2 = 4
age0 = 20
if age0 <= age2:
    print ('Go to home')
elif age0 <= age: # приментя если нужно бльше чем одно if
    print('cena 2 dollara')
else:
    print ('cena 5 dollarow')

# if нужно для проверки каждый раз нового условия
pizza = ['kolbasa', 'cheez']
if 'kolbasa' in pizza:
    print('Adding kolbasa')
if 'vetchina' in pizza:
    print('Adding vetchina') # не добавилось т.к. нет в списке
if 'cheez' in pizza:
    print ('Adding chezz')
print('Finishing making your pozza')

alien_color = 'green'
if 'green' in alien_color: # если не green то ничего не выводится
    print('plaer got five point')
else:
    print()
