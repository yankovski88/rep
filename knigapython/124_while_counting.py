# -*- coding: utf-8 -*-
number = 1
while number <= 5:
    print (number)
    number += 1

activ = True # True цикл выполняется
prom = '\nfirst stroka'
prom += '\nenter quit'
message = ''
while message != 'quit': # цикл продолжается пока message не будет равно quit
    message = input(prom)
    if message != 'quit':
        activ = False # не знаю что эта строчка дает, все работает и без нее
        '''
    elif message != 'q':  # чет не заканьчивается цикл на q
        activ = False
        '''
        print(message)


a = 7

