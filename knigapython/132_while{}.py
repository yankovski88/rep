# -*- coding: utf-8 -*-
a = {}
b = True
while b == True:
    v = input('введите имя: ')
    n = input('введите сколько лет: ')
    a[v] = n
    repeat = input('желаете продолжить: yes/no')
    if repeat == 'no':
        #print('Exit')
        b = False
#print(a)
for name, age in a.items():
    print('меня зовут', name.title(), 'мне', age, 'лет')

