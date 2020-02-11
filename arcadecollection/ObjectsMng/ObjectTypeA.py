from Components.Collider import *
#
from pygame import *
 

class ObjectTypeA:
    #Поле для работы с геометрией объекта
    geom = Geometry()

    #Тэг объекта
    tag = 'Object'

    #Коллайдер объекта
    coll = Collider()
