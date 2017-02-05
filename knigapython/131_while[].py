# -*- coding: utf-8 -*-
# проверка полььзователй
a = []
b = ['abra', 'kira', 'kolia']
while b:
    v = b.pop()
    print('проверены', v.title())
    a.append(v)
# вывод всех провереныых пользоватейл
a = sorted(a)
print(a)
for a in a:
   # a = sorted(a)
    print(a.title())