# -*- coding: utf-8 -*-
a = '1'
file = 'pi192.txt'
#birthday = input('введите день рождения: ') # запросили день рождения
with open(file) as file_object: # отыр файл
    for line in file_object:

        '''
        if birthday in line: # ввел поиск или есть такое савподение
            print('да есть такое савпадение')
    else:
        print('в 4 миллионах нет такого числа')
'''
        line = line.replace('1', '0')
        #if a in line: # ЗАМЕНИ ЦИФРУ 1 НА 0 В ЭТОМ ФАЙЛЕ!!!!!!!!!!!!!!!
         #   '1' == '0'
            #a == '0'

        print(line)

