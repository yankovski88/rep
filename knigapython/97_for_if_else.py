# -*- coding: utf-8 -*-
pizza = ['peppers', 'cheez', 'mushrooms']
for pizza in pizza:
    if 'peppers' in pizza:
        print ('Sori, it is not')
    else:
        print ('This is pizza', pizza)
print('\nFinished making your pizza')

a = ['']
for a in a:
    print ('Add', a)
else:
    print('base pizza?' )


topings = [] # начинаем с пустого списка
if topings: # программа выполняет проверку, а потом переходит к циклу for
    for topings in topings:
        print('Add', topings)
        print('Finichid', topings)
else:
    print('Are you sure you want a plain pizza?')


aa = ['as', 'ad', 'ae']
klient = ['as', 'perec', 'cheez']
for klient in klient:
    if klient in aa:
        print('Adding', klient)
    else:
        print('Not', klient)