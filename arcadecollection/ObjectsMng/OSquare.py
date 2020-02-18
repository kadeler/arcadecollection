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

        #
        self.point = set()
        #self.PointFind()

        #Коллайдер объекта
        self.coll = CCollider(self)
        self.tag = 'square'
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


    #Создаем квадрат
    def Create(self, surface):
        draw.rect(surface, self.color,
                  (self.geom.position.x, self.geom.position.y,
                   self.geom.size.x, self.geom.size.y))