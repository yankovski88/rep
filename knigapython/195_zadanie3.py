# -*- coding: utf-8 -*-

while True:
    print( 'For exit enter "q": ')
    a = input('why do do you like make program?  ',)
    if a == 'q':
        break
    z = a
b = '195_zadani3.txt'
with open(b, 'a') as file_object3:
    file_object3.write( str(z))# СДЕЛАТЬ ТАК ЧТОБЫ ЗАПИСЬ БЫЛА С НОВОЙ СТРОКИ