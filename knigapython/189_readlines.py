# -*- coding: utf-8 -*-
# строки файла pi186 сохроняются в списке блоке with, после чего выводятся за пределами этого блока.
filename = 'pi186' # переменная с файлом
with open(filename) as file_object:
    lines = file_object.readlines() # читает каждую строку из файла и сохраняет еев списке, список сохраняется в переменной lines
    for line in lines:              #с которой можно продолжить работу после завершения блока with
        print(line.rstrip()) # вывели все элименты всписка lines

# вывели по одной точно соответсвующей строчке файла
