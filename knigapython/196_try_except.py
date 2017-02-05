# -*- coding: utf-8 -*-
try: # если есть пользователь все ошибки нужно прописывать
    a = int(input('введите число: '))
    print(5/a)
except ZeroDivisionError:
    print('на ноль делить нельзя')