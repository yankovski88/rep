# -*- coding: utf-8 -*-
aliens = [] # создание списка
for alien_number in range(30): # создали 30 порядковых цифр (30 пришельцев)
    new_alien = {'color':'green', 'points':'7', 'speed':'slow'} # как создаются цифры, так и создается new_alien
    aliens.append(new_alien)

for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
# вывод первых 5 пришельцев
for alien in aliens[0:5]:
    print(alien)
print('.......')


alienb = [{'color':'yellow', 'points':'7', 'speed':'slow'}]
for alien1 in alienb:
    if alien1['color'] == 'green':
        alien1['color'] = 'yellow'
        alien1['points'] = '10'
        alien1['speed'] = 'medium'
#print(alien1) # работеат выводит yellow
    elif alien1['color'] == 'yellow':
        alien1['color'] = 'red'
        alien1['points'] = '15'
        alien1['speed'] = 'fast'
print(alien1)




