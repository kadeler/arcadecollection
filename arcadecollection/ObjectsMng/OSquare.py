from ObjectsMng.Object import *


class Geometry(GeneralGeometry):
    size = Vector() #Размер

class OSquare(Object):
    
    #Конструктор!
    def __init__(self):
        #Поле для работы с геометрией объекта
        self.geom = Geometry() 

        #Цвет объекта
        self.color = Red

        #Множества точек внутри объекта
        self.point = set()

        #Коллайдер объекта
        self.coll = CCollider(self)

        #
        #
        #
        self.toArray()
        #

    #Ищем все точки данного объекта в World
    def PointFind(self):
        for x in range(self.geom.position.x, self.geom.position.x + self.geom.size.x):
            for y in range(self.geom.position.y, self.geom.position.y + self.geom.size.y):
                self.point.add((x, y))
         
                
    #Двигаем объект в направлении:
    def move_object(self):

        #
        self.PointFind()

        #
        if not self.coll.Collision():
            self.geom.position += self.geom.direction


    #
    #Создаем квадрат
    def Create(self, surface):
        draw.rect(surface, self.color,
                  (self.geom.position.x, self.geom.position.y,
                   self.geom.size.x, self.geom.size.y))