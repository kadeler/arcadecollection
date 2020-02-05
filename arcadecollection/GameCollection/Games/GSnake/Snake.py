from ObjectsMng.Axes import *
from Inputs.SnakeCntrl import *
from Windows.Window import *

from copy import *

prev = None
axis = Axes()

class Snake(Field):

    snakeWin = Window() #Окно, с которым будет взаимодействовать змея
    cntrl = SnakeCntrl()

    arr_tail = []

    radius = 0
    radiusTail = 0
    
    #Состояния змеи
    start = False #Старт игры
    dead = False #Переменная смерти
    spawn = False
    score = 10


    #
    #Коструктор:
    def __init__(self, SnakeWin = snakeWin):
        self.snakeWin = SnakeWin

        #Определяем радиус головы змеи по формуле:
        self.radius = (SnakeWin.width + SnakeWin.height) // 100
        self.radiusTail = self.radius * 2 // 3



    def draw_tail(self, ax):
        #draw.rect(self.snakeWin.screen, (25, 175, 55), (ax.x.position, ax.y.position), 20)
        draw.circle(self.snakeWin.screen, (25, 175, 55), (ax.x.position, ax.y.position), self.radiusTail)

    def move_tail(self):
        for i in range(len(self.arr_tail)):

            if i != len(self.arr_tail) - 1:
                self.arr_tail[i] = self.arr_tail[i + 1]
            else:
                self.arr_tail[i] = deepcopy(axis)

            self.draw_tail(self.arr_tail[i])

            

    def create_tail(self):
        global prev

        for i in self.arr_tail:
            self.draw_tail(i)

        prev = deepcopy(axis)
        self.arr_tail.append(prev)



    #Создание змеи в позиции (x, y)
    def put(self, axis):
        global prev

        
        draw.circle(self.snakeWin.screen, (25, 175, 55), (axis.x.position, axis.y.position), self.radius)



    def putTail(self):
        if self.start:
            if len(self.arr_tail) < self.score + 1:
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
            self.put(axis)
            self.putTail()