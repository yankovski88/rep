# -*- coding: utf-8 -*-
# ЗАДАНИЕ ВЫЙТИ ПО QUIT ПО BREAK КОМАНДЕ(сделано)
t = '1'
active = True
while t != '0':
    print('для выхода введите 0 или quit')
    t = input('введите ваша возраст: ')
    if t == '0':
        print('Выход')
        active == False # выход через active True
    elif t == 'quit':
        print('Exit')
        break # конец цикла
    elif t <= '2':
        print('цена билета 0 руб')
    elif t <='12':
        print('билет стоит 10 рублей')
    else:
        print('цена билета 15 рублей')