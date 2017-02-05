# -*- coding: utf-8 -*-
alien_0 = {'color':'green', 'points':'5'}
print(alien_0['color'])
print(alien_0['points'])

alien_1 = {'color':'red', 'points':'4'}
new_points = alien_1['points']
print('winner ' + str(new_points) + ' points')

alien = {'color':'red', 'points':'5'}
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
alien['color'] = 'yellow'
print('добовление в словарь', alien)

al = {'x_position':0, 'y_position':25, 'speed':'medium'}
al['speed'] = 'fast'
print ('Original x-position: ' + str(al['x_position'])) # вывели позицию x
# пришелец перемещается в право
# вычисляем величину смещения на основании текущей скорости
if al['speed'] == 'slow':
    x_increment = 1
elif al['speed'] == 'medium':
    x_increment = 2
else:
    # пришелец двигается бысто
    x_increment = 3
# Новая позиция равна сумме старой позиции и прирощения
# al['speed'] = fast вот эту строчку нужно куда=то (вверх) добавить и появится скорость 3
al['x_position'] = al['x_position'] + x_increment
print('New x-position: ' + str(al['x_position']))