from Components.Color import *
#
from pygame import *

class Paintbrush:

    #Цвет "кисти"
    color = Red
    

    def __init__(self, geom):
        self.Geom_ = geom

    
    #Создаем круг
    def circle(self, surface, radius):
        draw.circle(surface, self.color, (self.Geom_.position.x, self.Geom_.position.y), radius)

    #Создаем квадрат
    def square(self, surface):
        draw.rect(surface, self.color,
                  (self.Geom_.position.x, self.Geom_.position.y,
                   self.Geom_.size.x, self.Geom_.size.y))


