from pygame import *


class Object:
    #Оси
    x = 0
    y = 0

    #Кортеж осей
    ax = None

    #Основная ось
    main = None

    def axes(self):
        self.ax = (self.x, self.y)