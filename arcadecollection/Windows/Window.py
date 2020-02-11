from ObjectsMng.Object import *

from pygame import *

class Window(Object):
    stop = False #Переменная для остановки ОСНОВНОГО цикла

    #
    #Конструктор
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    

    #Проверка на событие QUIT
    def loopWin(self):
        for i in event.get():
            if i.type == QUIT:
                self.stop = True


    #Метод открытия окна
    def openWin(self):
        init()

        self.size = (self.width, self.height)
        self.surface = display.set_mode(self.size)

        self.loopWin()


    #Метод, закрывающий окно
    def Exit(self):
        quit()