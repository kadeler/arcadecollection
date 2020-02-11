from Games.GSnake.Snake import *
from Windows.Window import *


xSizeWin = 1270
ySizeWin = 720

SnakeWin = Window(xSizeWin, ySizeWin)
Snk = Snake(SnakeWin)


def SnakeInf():
    Snk.startRespawn(xSizeWin // 2, ySizeWin // 2)
    Snk.move()


#Основной цикл сессии Snake
def snakeLoop():
    while not(SnakeWin.stop) and not(Snk.dead):
        time.delay(200)

        SnakeWin.openWin()
        SnakeInf()

        #Обновляем экран
        display.update()

snakeLoop()