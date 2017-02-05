# -*- coding: utf-8 -*-
from random import randint
# создал класс который генерирует кубика
# библиотека https://pymotw.com/3/

class Die():
    def __init__(self, sides = 20):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

d = Die()
d.roll_die()
