# -*- coding: utf-8 -*-
focus = ['yura', 'kolia', 'vasia']
r = []
def show_magicians(focus):
    for i in focus:
        print(i)

def make_great (focus, r):
    for n in focus:
        he = n + 'Great'
        r.append(he)
    print(r)


f2 = ['sdf', 'sdfsdsdf']
gg = []
make_great(f2, gg)

show_magicians(f2) # список не изменился
show_magicians(gg[:]) # к списку добавили дополнительную функцию

#функция добавь в список
ab = []
def kk (tt, ab):
    #ab.append(tt)
    for uu in tt:
        ab.append(uu)

ff = ['abra', 'sdf',]
kk(ff, ab) # cоздал функцию которая добовляет в список
print(ab)

ddd = {}
ddd['1'] = 'yura' # проверка над оболение словаря
print(ddd)





