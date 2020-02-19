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