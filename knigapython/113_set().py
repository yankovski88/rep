# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
a = {'kolia': 'c',
     'vasia': 'c',
     'dima': 'python',}
# set() это множество в котором в котороом все значения уникальны
for n in set(sorted(a.values())): # вывести только уникальные значения и попорядку
    print(n.title()) # вывод с большой буквы

b = {'nile':'egipet',
     'gorin':'stolin',
     'kopanec':'mankovichi',}
for key, values in b.items():
    print(key, ' протекает в ', values)
    print(key)


