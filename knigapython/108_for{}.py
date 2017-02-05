# -*- coding: utf-8 -*-
user_0 = {'name':'Kolia',
          'nik':'krut',
          'age':'18',}
print(user_0) #{'nik': 'krut', 'age': '18', 'name': 'Kolia'}
print(user_0.items()) # dict_items([('nik', 'krut'), ('age', '18'), ('name', 'Kolia')])
for key in user_0.items():
    print(key)
    '''
('nik', 'krut')
('age', '18')
('name', 'Kolia')
    '''
# user_0.items() выводит ключ и значение
for key, value in user_0.items(): # нужно 2 именя для ключа и значения
    print('\nKey: ', key)
    print('value: ' + value)
    '''
Key:  age
value: 18

Key:  name
value: Kolia

Key:  nik
value: krut
    '''
