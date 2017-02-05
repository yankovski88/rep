# -*- coding: utf-8 -*-
a = {'andrey': 'c',
     'yura':'python',
     'sacha':'ruby'}
b = ['sacha', 'yura']
for h in b:
    for n in a:
        if h in n:
            print(h)

# 2 вариант
x = {'kolia':'c',
     'vasia':'ruby'}
z = ['kolia', 'vasia', 'dima']
for name in x.keys():
    print(name.title())

    if name in x:
        print('Я, ', name.title(), 'нравится язык', x[name].title() + '!')

if 'dis' not in x.keys(): # если нет dis в списке словарей, тогда вывести
    print('dis', 'введи свой язык' )

# 3 вариант сортируем поалфовитному порядку
x = {'kolia':'c',
     'vasia':'ruby',
     'dima':'python',}

for name in sorted(x.keys()):
    print (name)