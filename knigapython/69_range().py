# -*- coding: utf-8 -*-
a = ['vasia', 'kolia', 'vika']
for n in range(1, 5): # все числа от 1 до 5 вывело в столбик
    print(n)

b = [1, 5]
for n in b:
    print(b)


h = list(range(1, 5)) # создает список, из диапазона
print(h)

k = list(range(1, 10, 2)) # содали список с шагом 2
print(k)

#
u = list(range(1, 10, 2)) # содали список с шагом 2
x = []
for m in k:
    g = m ** 2
    x.append(g)
print(x)