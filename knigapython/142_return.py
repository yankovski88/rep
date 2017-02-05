# -*- coding: utf-8 -*-
# return передает занчение из функции в строку в которой эта функция была вызвана
def get (first_name, last_name, middle_name=''):
    '''возвращает аккуратно отформотированое полное имя'''
    if middle_name: # если есть имя которое не всегда прописывается то:
        full_name = first_name + ' ' + last_name + ' ' + middle_name # выводитсчя этот выриант
    else: # иначе если нет 3 имени, то:
        full_name = first_name + ' ' + last_name # вывести этот выриант
    return full_name.title() # вернуло уже отформатированное значение в точку возврата
musician = get('jimi', 'hendrix')
print(musician)
musician = get('jimi', 'hendrix', 'boets')
print(musician)
