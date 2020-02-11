from Components.Collider import *
#
from pygame import *
<<<<<<< HEAD
<<<<<<< 11b232e7c46796872791cd658b43b9c46252a091:SourceCode/ObjectsMng/Object.py
from copy import *

=======

#
##
>>>>>>> Snage N2:SourceCode/ObjectsMng/ObjectTypeA.py
=======

#
##
>>>>>>> Рефакторинг
class Axes:
    x = 0
    y = 0

#
#Поля геометрии
    #Позиция
class Position(Axes):
    pass
<<<<<<< HEAD
<<<<<<< 11b232e7c46796872791cd658b43b9c46252a091:SourceCode/ObjectsMng/Object.py

class Size(Axes):
    radius = 0
=======
=======
>>>>>>> Рефакторинг
    #Вектор
class Vector(Axes):
    pass
    #Размер
class Size(Axes):
    radius = 0


class Geometry:
    #
    position = Position() #Позиция
    vector = Vector() #Направление
    size = Size() #Размер
<<<<<<< HEAD
>>>>>>> Snage N2:SourceCode/ObjectsMng/ObjectTypeA.py

class Vector(Axes):
    pass


<<<<<<< 11b232e7c46796872791cd658b43b9c46252a091:SourceCode/ObjectsMng/Object.py
class Object:
    Tag = 'Object' #Тег объекта
    
    position = Position() #Позиция
    size = Size() #Размер 
    vector = Vector() #Направление
=======
=======



>>>>>>> Рефакторинг
class ObjectTypeA:
    #Поле для работы с геометрией объекта
    geom = Geometry()

    #Тэг объекта
    tag = 'Object'

<<<<<<< HEAD
    coll = Collider()
>>>>>>> Snage N2:SourceCode/ObjectsMng/ObjectTypeA.py
=======
    coll = Collider()
>>>>>>> Рефакторинг
