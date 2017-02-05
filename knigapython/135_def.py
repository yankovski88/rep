# -*- coding: utf-8 -*-
# def определили функцию
def priv(username):
    '''выводит приветствие'''
    print('привет', username.title())

priv('yura') # функция выводит сообщение привет


# ЗАДАНИЕ МОЖНОЛИ ИЗИ СПИСКА СОЗДАТЬ СЛОВАРЬ?????
'''
a = ['sdf', 'qwe']
print(dict(a))
'''
def kot (name, namekot):
    print(name, 'его кот', namekot)

kot('yura', 'margo'.title())

#имменнованые аргументы точно присвоили имя
def k (n, ani):
    print(n, ani)
k (n ='yur', ani= 'mar')

# при большом вводе одного и того параметра(значение по умолчанию)
def h (ne, hh= 'kot'):
    print(ne, 'его', hh)
h(ne='yurasuper')
h('yurasuper') # тоже самое выводит, что и в первом
