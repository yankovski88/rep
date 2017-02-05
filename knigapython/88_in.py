# -*- coding: utf-8 -*-
a = [1, 2, 3, 4] # проверка или есть такое значение в списке
b = 1
if b in a:
    print(True)
else:
    print(False)

# проверка или пользователь есть вчерном писке
q = ['andrey', 'korolina']
user = 'kolia'
if user not in q:
    print(user.title(), 'you can to write')
