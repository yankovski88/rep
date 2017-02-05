# -*- coding: utf-8 -*-
alien_0 = {'color':'green', 'points':'5'}
alien_1 = {'color':'red', 'points':'3'}
alien_2 = {'color':'yellow', 'points':'1'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


al = [] # создание списка
for alien_number in range(30): # создали 30 порядковых цифр
    new_alien = {'color':'green', 'points':'7', 'speed':'slow'} # как создаются цифры, так и создается new_alien
    al.append(new_alien)
    #print(alien_number) вывел 30 цифр
print('выводит  30 иноплатинитят', al) # выводит 30 цифр
# вывод 5 первых пришельцев
for aq in al[:5]: # вывести только первые 5 пришельцев
    print(alien)
print('......')
# вывод созданных пришельцев
print('Total number of aliens: ', str(len(al))) # проверка или точно 30 пришельцев

