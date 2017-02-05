# -*- coding: utf-8 -*-
a = ['asdf', 'df', 'we']
print(a[0:2]) # срез от 0 до 2
print(a[-2:]) # -2 и до конца


b = ['asdf', 'df', 'we', 'ert', 'sdfgre']
for n in b[0:3]:
    print(n.title(), 'зачислен')


my_bludo = ['bulba', 'saslat', 'borchct']
a = my_bludo[:]
print(my_bludo)
print('my_friend bludo', a[-2:]) # блидо которые нарвятся другу

my_bludo.append('cannoly')
a.append('pizza')

print(my_bludo)
print('my_friend bludo', a[:]) # блидо которые нарвятся другу

