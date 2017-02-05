# -*- coding: utf-8 -*-

a = [1, 2, 3, 4, 5,345, 3, 34, 346,]
b = max(a) # максимальное значение списка
c = min(a)
n = sum(a) # сумма всех чисел
print(b)
print(c)
print(n)

j = [spisok**2 for spisok in range(1, 10)] # возведение в степень в списке
print(j)

k1 = []
kk = list(range(1, 1000000))
k1.append(sum(kk))
print('k1',k1) # сумма 1000000

n3 = [] # вывод только четных
n1 = list(range(1, 20, ))
for n2 in n1:
    if n2 % 2 == 0:
        n3.append(n2)
print(n3)

m1 = []
m2 = list(range(1, 20))
for m3 in m2:
    if m3 % 2 != 0:
        m1.append(m3)
print(m1)


b1 = [] # нашли все числа кратные 3
b2 = list(range(1, 30))
for b4 in b2:
    if b4 % 3 == 0:
        b1.append(b4)
print(b1)

v3 = [] #создал список числе в кубе, и вывел только те, что меньше 10
v1 = list (v2**3 for v2 in range(1, 10))
for vv in v1:
    if vv < 10:
        v3.append(vv)
        print(v3)
