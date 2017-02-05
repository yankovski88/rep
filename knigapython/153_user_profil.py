# -*- coding: utf-8 -*-
def profile (first, last, **user_info):
    # ** добавляет пустой словарь
    '''строит словарь с информацией о пользователе'''
    vprof = {}
    vprof['first_name'] = first
    vprof['last_name'] = last
    for key, value in user_info.items():
        vprof[key] = value
    return vprof

b = profile('yura', 'yankovski',
            name2='abra',
            erunda = 'kadabra',)
print(b)