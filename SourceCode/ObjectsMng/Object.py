from pygame import *
from copy import *

class Axes:
    x = 0
    y = 0


class Position(Axes):
    pass

class Size(Axes):
    radius = 0

class Vector(Axes):
    pass


class Object:
    Tag = 'Object' #Тег объекта
    
    position = Position() #Позиция
    size = Size() #Размер 
    vector = Vector() #Направление