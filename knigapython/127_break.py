# -*- coding: utf-8 -*-
#break прерывает цикл while без продолжения цикла
prompt = '\nPlease enter the name of a city you have visid'
while True: # цикл while True выполняется бесконецно пока не будт выполнена команда break
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print('i love to go', city.title())