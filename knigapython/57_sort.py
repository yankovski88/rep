# -*- coding: utf-8 -*-

a = [ 'd', 'f', 'j',]
a.sort() # отсортирвоали по алфовитному порядку порядку
print(a)

a.sort(reverse=True) # сортировка в обратном порядке
print(a)


#функция сортирует, но не сохраняет порядок
n = ['gricha', 'vasia', 'koli', 'petia' ]
print(sorted(n)) #['gricha', 'koli', 'petia', 'vasia']
print(n) #['gricha', 'vasia', 'koli', 'petia']

b = ['asdf', 'sdgf', 'lkjnl', 'bsdfddd',]
b.reverse() # отсортировала в обратном порядке не зависимо от алфовита
print(b)

v = len(b) # сколько элиментов в списке
print(v)