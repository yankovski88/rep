# -*- coding: utf-8 -*-
def make_pizza(size, *toppings):
    '''выводит описание пиццы'''
    print('\nMaking a ' + str(size) + 'cm' + ' pizza with toppings: ')
    for i in toppings:
        print('- ' + i)
