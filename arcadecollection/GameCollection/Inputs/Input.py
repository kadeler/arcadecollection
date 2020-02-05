from pygame import *

class Input:

#Методы для определения настроек управления
    #Массив нажатий на клавиатуру
    def keys(self, i):
        return key.get_pressed()[i]

    #Возвращает TRUE, если кнопка в аргументе была нажата
    def definit(self, key1, key2 = False):
        if key1:
            return key1

        if key2:
            return key2

#Управление:
    #Вправо
    def right(self):
        return self.definit(self.keys(K_d), self.keys(K_RIGHT))

    #Влево
    def left(self):
        return self.definit(self.keys(K_a), self.keys(K_LEFT))

    #Вниз
    def down(self):
        return self.definit(self.keys(K_s), self.keys(K_DOWN))

    #Вверх
    def up(self):
        return self.definit(self.keys(K_w), self.keys(K_UP))

#Оси координат:
    #Проверка для управляемых объектов, которые всегда находятся в движении
    #Проверяет в какую сторону двигается объект и инвертирует направление, если оно не соответстует необходимому
    #По горизонтали:
    def check_hor(self, dir):
        if self.right() and dir < 0: #Проверка на движение вправо
            return dir * -1
        
        elif self.left() and dir > 0: #Проверка на движение влево
            return dir * -1

        else:
            return dir

    #По вертикали:
    def check_vert(self, dir):
        if self.up() and dir > 0: #Проверка на движение вверх
            return dir * -1
        
        elif self.down() and dir < 0: #Проверка на движение вниз
            return dir * -1

        else:
            return dir


    #Движение по оси X
    def horizontal(self):
        return self.right() or self.left()

    #Движение по оси Y
    def vertical(self):
        return self.up() or self.down()