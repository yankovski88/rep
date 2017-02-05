# -*- coding: utf-8 -*-
#создали словарь который не меняется местами
from collections import OrderedDict
b = OrderedDict()
b ['kolia']= 'c',
b ['vasia'] = 'ruby',
b ['dima']= 'python',

for key, values in b.items():
    print(key, 'любит',  values)
#print(b)

