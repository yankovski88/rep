# -*- coding: utf-8 -*-
# сделалть бмв большими,а остальные с заглавной
a = ['bmw', 'mers', 'audi']
for car in a:
    if car == 'bmw':
            print(car.upper())
    else:
        print(car.title())
