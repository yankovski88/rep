# -*- coding: utf-8 -*-
def greet (names):
    '''приветствие для каждого пользователя'''
    for name in names:
        a = 'Hello' + ' ' + name.title()
        print(a)

usernames = ['yura', 'kolia', 'aliona']
greet (usernames)

# к каждому имени присвоили значение
def re (nam):
    for re in nam:
        print ('hi', re)

g = ['mashina', 'kater', 'sdfasdf']

re(g)
