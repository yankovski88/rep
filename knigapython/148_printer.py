# -*- coding: utf-8 -*-
#список который нужно напечатать
unp = ['spisok1', 'spisok2', 'spisok3']
finunp = []

# цикл который последовательно печатает каждую модель до конца списка
# после печати каждая модель перемещается в список finunp
def pechat (unp, finunp):
    while unp: # пока
        cur = unp.pop()
        # печать модели на 3d принтере
        print('pechat', cur)
        finunp.append(cur)

def vivgot(finunp):
# вывод всех готовых моделей
    print('готовые печати')
    for i in finunp:
        print(i)

pechat(unp[:], finunp) # нужно вставлять список для печати
# после доболвения [:] среза создавалась копия
vivgot(finunp) # нужно вставлять список который нужно вывести
print(unp, 'список который мы обробатывали был пуст, пока не прописали в функцию [:]')


