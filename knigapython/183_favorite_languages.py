# -*- coding: utf-8 -*-
from collections import OrderedDict # импортировали класс из модуля
# программа отслеживает порядок как отвечают участники на опрос
fav = OrderedDict() # создается экземпляр класса OrderedDict() который сохроняется в fav
# создается пустой упорядоченный словарь и сохраняет кго в fav
fav ['jen'] = 'python' # пары из имени и языка постепенно добовляются в словарь
fav ['sarah'] = 'c'
fav ['edvard'] = 'ruby'
fav ['phil'] = 'python'
for name, language in fav.items(): # теперь данные будут выводится как и отвечали по порядку
    print(name.title() + ' favorite language is ' + language.title())