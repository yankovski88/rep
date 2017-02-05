# -*- coding: utf-8 -*-
def get (a, b): # создали функцию по выводу имени и фамилии с увеличение заглаыной буквы
    fin = a + ' ' + b
    return fin.title()

while True:
    print('для выхода введите quit  в имя')

    na = input('введите имя: ')
    if na == 'quit':
        break
    nb = input('введите фамилю: ')

    g = get (na, nb)
    print(g)
    #break


