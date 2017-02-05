# -*- coding: utf-8 -*-
filename = '193_programming.txt'
with open (filename, 'a') as file_object: # w означает что файл должен быть открыт в режиме записи
    file_object.write('I live programming.\n')
    file_object.write('I live programming and ruby\n')
    file_object.write('I live \n')
#r для чтения,(по умолчанию)
#a присоединения
#r+ допускающим как чтение так и запись в файл
