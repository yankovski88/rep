# -*- coding: utf-8 -*-
san = ['san1', 'san2', 'san3', 'san1' , 'san1']
finsan = []
#a = True
while san:
    v = san.pop() # для каждого элимента вывели получилось
    print('получилось', v)

    finsan.append(v) # добавили один список во второй
print(finsan)


# удалил все повторяющиеся элименты
while 'san1' in finsan:
    finsan.remove('san1')
print(finsan)

h = {}
tt = True
while tt == True:

    name = input('как зовут: ')
    gorod = input('введите город, где хотели провести отпуск: ')
    h[name] = gorod
    dd = input('для вывода данных и выхода, введите quit')
    if dd == 'quit':
        tt = False
print(h)