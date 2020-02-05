from Games.GSnake.Snake import *
from Windows.Window import *


xSizeWin = 1000
ySizeWin = 1000

SnakeWin = Window(xSizeWin, ySizeWin)
Snk = Snake(SnakeWin)


def SnakeInf():
    Snk.startRespawn(xSizeWin // 2, ySizeWin // 2)
    Snk.move()


while not(SnakeWin.stop) and not(Snk.dead):
    time.delay(200)

    SnakeWin.openWin()
    SnakeInf()

    display.update()