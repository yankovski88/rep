# -*- coding: utf-8 -*-
file = '192_zadanie_10-1.txt'
a = '' # если '' то выводит как в файле в разные строчки
with open(file) as file_object:
    lin = file_object.readlines()
    for line in lin:

        a += line#.strip() # c strip() лепит все в одну строчку
        #a.append(line) # .strip без отступа все в одну строчку []
    a = a.replace ('Python', 'c') # ЗАМЕНЬ СЛОВА!!!!!!(решено)
    a = a * 3 # сделал 3 одинаковые строки
    print(a)

print(a) #вывел вне блока with
