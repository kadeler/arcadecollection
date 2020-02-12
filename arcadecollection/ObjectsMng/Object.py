#from Components.Collider import *
from Components.Paintbrush import *
#
from pygame import *
 
class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    #Возможность сложения векторов
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

#Поля для работы с геометрией:
class Geometry:
    position = Vector() #Позиция
    direction = Vector() #Направление
    size = Vector() #Размер



class Object:
    #Поле для работы с геометрией объекта
    geom = Geometry()


    def set_paintbrush(self):
        #"Кисть" для изменения формы объекта
        self.paint = Paintbrush(self.geom)
    
    def __init__(self):
        self.set_paintbrush()

    #Тэг объекта
    tag = 'Object'

    
    #Двигаем объект в направлении:
    def move_object(self):
        self.geom.position += self.geom.direction

    #Коллайдер объекта
    #coll = Collider()
