from Games.GSnake.Snake import *


xSizeWin = 1240
ySizeWin = 800

SnakeWin = Window(xSizeWin, ySizeWin)
Snk = Snake()




#Основной цикл сессии Snake
def snakeLoop():
    while not(SnakeWin.stop): #and not(Snk.dead):
        time.delay(100)

        SnakeWin.openWin()

        Snk.set_snake(SnakeWin.surface,
                      Vector(xSizeWin // 2, ySizeWin // 2))


        #Обновляем экран
        display.update()

snakeLoop()