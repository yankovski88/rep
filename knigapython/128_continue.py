# -*- coding: utf-8 -*-
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue #если остаток делится на 2, то continue приказывает проигнарировать оставшийся цикл код и вернуться к началу
        # если не делится на 2, то оставшаяся часть года выполняется
    print(number)

# если i = 0, то пропусти и продолжи)
'''
    >> > for i in 'hello world':
        ...
        if i == 'o':
            ...
        continue
    ...
    print(i * 2, end='')
    ...
    hheellll
    wwrrlldd
    '''