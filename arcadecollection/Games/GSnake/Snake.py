from ObjectsMng.OCircle import *
from Inputs.SnakeCntrl import *
from Windows.Window import *
#
from copy import *


class Tail(OCircle): 

    #
    def set_geom(self, geom):
        self.geom = geom
        
    #
    def set_tail(self, surface, radius):
        self.Create(surface, radius)
        


class Snake(OCircle):
    #Массив частей хвоста
    arr_tail = []

    #Состояния змеи
    start = False #Старт игры
    dead = False #Переменная смерти
    spawn = False #Появление змеи на карте
    defualt_Tquantity = 4

    #Количество очков
    score = 3


    #Диспетчер змеи
    def set_snake(self, surface, position):
        #Определяем экран
        self.surface = surface        

        #Стартуем в позиции:
        self.start_atPoint(position)
        self.Create(surface, self.radius)

        #Запускаем движение
        self.move()

    #Цикл, ведущий хвост за головой змеи
    def tail(self):
        if self.start: #Начинаем создавать хвост при условном "старте" игры
            #Двигаем хвост, если длина его массива соответствует необходимой длине хвоста
            if len(self.arr_tail) == self.length_snake:

                #
                for i in range(self.length_snake):
                    #Передвигаем все части хвоста, кроме той, 
                    #что ближе всего к голове 
                    if i != self.length_snake - 1:
                        self.arr_tail[i].collision = True
                        self.arr_tail[i].geom = deepcopy(self.arr_tail[i + 1].geom)
                        self.arr_tail[i].set_tail(self.surface, self.radiusTail)

                    else: #Присваиваем последней части хвоста координаты головы
                        self.arr_tail[len(self.arr_tail) - 1].collision = False
                        self.arr_tail[len(self.arr_tail) - 1].geom = deepcopy(self.geom)
                        
                        
            else: #Иначе заполняем массив до необходимой длины

                #Двигаем части хвоста, которые уже есть в масссиве
                for i in range(len(self.arr_tail)):
                    if i != len(self.arr_tail):
                        self.arr_tail[i].collision = True

                    self.arr_tail[i].set_tail(self.surface, self.radiusTail)

                #
                #Каждый display.update добавляем еще одну часть массива
                #Пока его велечина не станет соответствовать длине хвоста
                self.arr_tail.append(Tail())
                self.arr_tail[len(self.arr_tail) - 1].set_geom(deepcopy(self.geom))


    #Координаты спавна змеи на старте игры
    def start_atPoint(self, position, step = Vector(40, 40)):

        if not self.spawn:
            #Устанавливаем радиус головы и хвоста змеи
            self.radius = (position.x + position.y) // 36
            self.radiusTail = int(self.radius / 1.5)

            #Устанавливаем шаг змеи
            self.step = Vector(self.radius, self.radius)

            #Устанавливаем координаты змеи
            self.geom.position = position
            
            
            #Сообщаем о появлении змеи на карте
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
            #
            #
            #Ось Y
            if Input().vertical():
                self.geom.direction = Vector(0, Input().check_vert(self.step.y))

            
            #Начинаем массив хвоста с головы
            if len(self.arr_tail) == 0:
                self.arr_tail.append(Tail())
                #
                self.arr_tail[0].set_geom(deepcopy(self.geom))
                self.arr_tail[0].collision = False
            #
            #Сообщаем о старте игры
            if self.geom.direction.x != 0 or self.geom.direction.y != 0:
                self.start = True
            #
            #Обозначаем стартовоую длину змеи
            if self.start:
                self.length_snake = self.score + self.defualt_Tquantity + 1


            self.move_object()
            self.tail()