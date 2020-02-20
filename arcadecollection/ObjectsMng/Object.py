from ObjectsMng.Vector import *
from Components.Color import *
from Components.Component import *
#
from pygame import *

#Поля для работы с геометрией:
class GeneralGeometry:
    position = Vector() #Позиция
    direction = Vector() #Направление


class Object(OInformation):

    #Добавление объекта в "массив объектов"
    def toArray(self):
        OArray.append(self)

    def move_object(self, Invert = False):
        if not Invert:
            self.geom.position += self.geom.direction
            
        else:
            self.geom.position += Vector(-self.geom.direction.x, -self.geom.direction.y)