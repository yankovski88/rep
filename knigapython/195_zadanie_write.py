# -*- coding: utf-8 -*-
'''
file = '195_guest.txt'
a = input('введите свое имя: ')

with open(file, 'a') as file_object:
    file_object.write(a)
'''

file2 = 'guest_book195.txt'

a = ''
while a != 'quit':
    print('введите quit для выхода')
    a = input('введите имя: \n')
    if a == 'quit':
        break
    g = 'hello! ', a
   # print(g)
with open(file2, 'a') as file_object2:
    file_object2.write(str(g))