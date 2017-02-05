# -*- coding: utf-8 -*-
def a (*znachenie): # функция выводит любое значение
    print(znachenie)

a('asdf', 'sdfasdf')

def b (first, last, **inoe):
    totle = {}
    totle['first'] = first
    totle['last'] = last
    for key, value in inoe.items():
        totle[key] = value
    return totle

v = b ('yura', 'yankovski',
       er='vasia' )
print (v)


def t (model, contre, **echcte):
    sl = {}
    sl['model_avto'] = model
    sl['contre_proizvod'] = contre
    for key, value in echcte.items():
        sl[key] = value
    return sl
fr = t('жигули', 'ссср', состояние = 'хорошое')
print(fr)


