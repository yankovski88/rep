# -*- coding: utf-8 -*-
# remove() удаляет значение из списка
pets = ['cat', 'dog', 'cat', 'animal']
while 'cat' in  pets: # продлять цикл пока есть cat
    #if pets == 'cat':
    pets.remove('cat')
print(pets)

a = ['b', 'b', 'h', 'g', 't']
print(a)

while 'b' in a: # если b в a то удалить b
    a.remove('b')
print(a)