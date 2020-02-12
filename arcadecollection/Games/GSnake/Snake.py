from Components.Collider import *
from Inputs.SnakeCntrl import *
from Windows.Window import *

from copy import *


class Tail(Object):

    def __init__(self, position):
        self.position = position

    #
    def set_tail(self, surface, radius):
        self.set.circle(surface, radius)


class Snake(Object):
    #Массив частей хвоста
    arr_tail = []

    #Радиусы головы и хвоста
    radius = 0
    radiusTail = 0
    
    #Предыдущая позиция головы
    prev = None


    #Состояния змеи
    start = False #Старт игры
    dead = False #Переменная смерти
    spawn = False #Появление змеи на карте
    defualt_Tquantity = 3

    #Количество очков
    score = 0


    def set_snake(self, surface, position):
        #Определяем экран
        self.surface = surface

        #Стартуем в позиции:
        self.start_atPoint(position)
        self.set.circle(surface, self.radius)

        #Запускаем движение
        self.move()



    def tail(self):
        if self.start:
            for i in range(len(self.arr_tail)):
                if len(self.arr_tail) == self.length_snake:
                    self.arr_tail[i].set_tail(self.surface, self.radiusTail)



            if len(self.arr_tail) < self.length_snake:
                for i in range(len(self.arr_tail), self.length_snake + 1):
                    self.arr_tail.append(self.prev)


    #ДВИЖЕНИЕ хвоста
    def move_tail(self):
        for i in range(len(self.arr_tail)):

            if i != len(self.arr_tail) - 1:
                self.arr_tail[i] = self.arr_tail[i + 1]
            else:
                self.arr_tail[i].geom.position = deepcopy(self.geom.position)

            self.draw_tail(self.arr_tail[i])

            
    #СОЗДАНИЕ хвоста
    def create_tail(self):
        if self.start:
            #
            for i in range(self.length_snake):
                if i >= self.length_snake:
                    self.arr_tail[i].set_tail(self.surface, self.radiusTail)
                else:
                    self.arr_tail.append(Tail(self.prev))

            #
            self.prev = deepcopy(self.geom.position)
            self.arr_tail.append(Tail(self.prev))


    #Рисуем ХВОСТ змеи в позиции (x, y)
    def putTail(self):
        if self.start: #Игровые очки + стандартное кол-во частей хвоста + голова змеи
            if len(self.arr_tail) < self.score + self.defualt_Tquantity + 1:
                self.create_tail()
            #else:
            #    self.move_tail()


    #Координаты спавна змеи на старте игры
    def start_atPoint(self, position, step = Vector(40, 40)):

        if not self.spawn:
            #Устанавливаем шаг змеи
            self.radius = (position.x + position.y) // 36

            #Устанавливаем шаг змеи
            self.step = Vector(self.radius, self.radius)

            #Устанавливаем координаты змеи
            self.geom.position = position
            

            #Сообщаем о том что старт произошел
            self.spawn = True 


    #Движение змеи
    def move(self):

        #Проверяем возможность передвижения
        if not self.dead:

        #Проверяем ось, по которой движется змея
        #И изменяем направления в зависимости от выбранной стороны: 

            #Ось X
            if Input().horizontal():
                self.geom.direction = Vector(Input().check_hor(self.step.x), 0)
            

            #Ось Y
            if Input().vertical():
                self.geom.direction = Vector(0, Input().check_vert(self.step.y))

            
            #
            if len(self.arr_tail) == 0:
                self.arr_tail.append(Tail(self.geom.position))


            #
            if self.geom.direction.x != 0 or self.geom.direction.y != 0:
                self.start = True

            #
            if self.start:
                self.length_snake = self.score + self.defualt_Tquantity + 1

            #Присваиваем измененные координаты змее
            self.move_object()
            self.tail()
            #self.putTail()