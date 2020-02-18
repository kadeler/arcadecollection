from ObjectsMng.Object import *
#
from math import *


class Geometry(GeneralGeometry):
    radius = 0 #Радиус окружности

class OCircle(Object):

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
        self.tag = 'circle'
        #
        #
        #
        self.toArray()
        #



    #Ищем все точки данного объекта в World
    def PointFind(self):
        #Начинаем считать точки по тому же принцепу, что и в квадрате: с верхней левой точки
        begin_point = self.geom.position + Vector(-self.geom.radius, -self.geom.radius)
        centre = self.geom.position #Центр окружности

        #Проверяем, находится ли точка в окружности
        for point_x in range(begin_point.x, begin_point.x + self.geom.radius * 2):
            for point_y in range(begin_point.y, begin_point.y + self.geom.radius * 2):

                #Супер классная формула кто ее не знает тот канешь капец))0)
                if (centre.x - point_x) ** 2 + (centre.y - point_y) ** 2 <= self.geom.radius ** 2:
                    self.point.add((point_x, point_y))


    #Создаем круг
    def Create(self, surface, radius):
        draw.circle(surface, self.color, (self.geom.position.x, self.geom.position.y), radius)


