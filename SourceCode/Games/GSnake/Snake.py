from ObjectsMng.Axes import *
from Component.Collider import *
from Inputs.SnakeCntrl import *
from Windows.Window import *

from copy import *

prev = None
axis = Ax()

class Snake(Object):

    snakeWin = Window() #Окно, с которым будет взаимодействовать змея
    cntrl = SnakeCntrl() #Input сессии со змейкой
    coll = Collider()

    #Массив частей хвоста
    arr_tail = []

    radius = 0
    radiusTail = 0
    
    #Состояния змеи
    start = False #Старт игры
    dead = False #Переменная смерти
    spawn = False #Появление змеи на карте
    defualt_Tquantity = 3

    #Количество очков
    score = 0


    #
    #Коструктор:
    def __init__(self, SnakeWin = snakeWin):
        self.snakeWin = SnakeWin

        #Определяем радиус головы змеи по формуле:
        self.radius = (SnakeWin.width + SnakeWin.height) // 100
        self.radiusTail = self.radius * 2 // 3



    #Просто рисуем хвостик :D
    def draw_tail(self, ax):
        draw.circle(self.snakeWin.surface, (25, 175, 55), (ax.x.position, ax.y.position), self.radiusTail)


    #ДВИЖЕНИЕ хвоста
    def move_tail(self):
        for i in range(len(self.arr_tail)):

            if i != len(self.arr_tail) - 1:
                self.arr_tail[i] = self.arr_tail[i + 1]
            else:
                self.arr_tail[i] = deepcopy(axis)

            self.draw_tail(self.arr_tail[i])

            
    #СОЗДАНИЕ хвоста
    def create_tail(self):
        global prev

        for i in self.arr_tail:
            self.draw_tail(i)

        prev = deepcopy(axis)
        self.arr_tail.append(prev)



    #Рисуем ГОЛОВУ змеи в позиции (x, y)
    def draw_head(self, axis):
        draw.circle(self.snakeWin.surface, (25, 175, 55), (axis.x.position, axis.y.position), self.radius)


    #Рисуем ХВОСТ змеи в позиции (x, y)
    def putTail(self):
        if self.start: #Игровые очки + стандартное кол-во частей хвоста + голова змеи
            if len(self.arr_tail) < self.score + self.defualt_Tquantity + 1:
                self.create_tail()
            else:
                self.move_tail()


    #Координаты спавна змеи на старте игры
    def startRespawn(self, x, y, xV = 50, yV = 50):

        if not self.spawn:
            #Устанавливаем шаг змеи
            xV = self.radius
            yV = self.radius

            #Устанавливаем координаты змеи
            self.position.x = x
            self.position.y = y

            #Устанавливаем скорость змеи
            self.vector.x = xV
            self.vector.y = yV

            #Сообщаем о том что старт произошел
            self.spawn = True

            #self.put


    def change_coord(self, ax):
        if ax.main_axis:
            ax.begin(self)
            
            ax.position += ax.vector

            ax.end(self)

    #Движение змеи
    def move(self):

        #Проверяем возможность передвижения
        if not self.dead:

        #Проверяем ось, по которой движется змея
        #И изменяем направления в зависимости от выбранной стороны: 

            #Ось X
            if self.cntrl.horizontal():
                self.vector.x = self.cntrl.check_hor(self.vector.x)
                axis.x.main_axis, axis.y.main_axis = True, False

                self.start = True
            
            #Ось Y
            if self.cntrl.vertical():
                self.vector.y = self.cntrl.check_vert(self.vector.y)
                axis.x.main_axis, axis.y.main_axis = False, True

                self.start = True

            if len(self.arr_tail) == 0:
                axis.inside(self)
                prev = deepcopy(axis)
                self.arr_tail.append(prev)

            #Изменяем координаты
            self.change_coord(axis.x)
            self.change_coord(axis.y)
            axis.inside(self)

            #Присваиваем измененные координаты змее
            self.putTail()
            self.draw_head(axis)

            #Фиксируем положение коллайдера головы змеи за самой головой
            self.coll.fix_field()