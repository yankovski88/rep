# -*- coding: utf-8 -*-
# строим строку со всеми цифрами из файла без промежуточных отпусков.
filename = 'pi186' # переменная с файлом
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' # создается переменная для числа pi(наших строк)
for line in lines: # цикл который добвляет каждый раз новую строку
    pi_string += line.strip()
# strip() удаляет растояние в строке
print(pi_string[:15]) # выводим строку и длину
print(len(pi_string))

# int() преобразует как целое число
# float() преобразует как вещественное