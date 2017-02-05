# -*- coding: utf-8 -*-
filename = 'pi186' # путем файла
with open(filename) as file_object: #содержимое переменной сохроняется в файле
    for line in file_object: # для просмотра содрежимого все строки перебираются
        print( line.rstrip()) # удаляем лишние отступы


