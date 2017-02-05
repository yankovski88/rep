# -*- coding: utf-8 -*-
a = ['vasia', 'kolia']
b = 'Hello, ' + a[0].title() # вывели из списка и увеличили первую букву
print (b)

gg = ['wer', 'dSf']
print (gg[-1].lower()) # ката

a = ['honda', 'suzuki', 'yamaha']
del a[2] # удаляет выбранные элимент
print(a)

print(a[-1])
a.append('ducati')
print(a)

a.insert(0, 'bmw')
print(a)


a.insert(2, 'mers')
print(a)

a[0] = 'volvo'
print(a)

b = a.pop(0) # исключили из списка по номеру
print('sorry', b)

с = a.pop()
print('sorry', с, 'последний')

a.remove('mers') # удалили mers по слову
print(a)


pp = ['qwe', 'ook']
del pp[-1]
print(pp[-1].upper())
nn = pp.pop(-1)
print(nn.title(), 'нужно удалить')


#print ('первый' pop(pp.[-1].title()))