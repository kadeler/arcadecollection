from Components.Collider import *
#
from pygame import *


class ObjectTypeB:
    #Тэг объекта
    tag = 'Object'

    #Поле для работы с геометрией объекта
    geom = Axes()

    #Коллайдер объекта
    coll = Collider(geom)

