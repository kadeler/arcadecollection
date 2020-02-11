#
#Геометрия осей объекта
class Geometry:
    #
    position = 0 #Позиция
    vector = 0 #Направление
    size = 0 #Размер

#
#Классы осей
class xAxis(Geometry):
    pass

class yAxis(Geometry):
    pass

#
#Выбранная нами ось
class SelectedAxis(Geometry):
    pass
####
#
#
#Действия с осями координат
class Axes:
    #Оси координат
    x_axis = xAxis()
    y_axis = yAxis()

    #Выбранная ось
    sel_ax = SelectedAxis()

    #Выбор оси
    def SelectAxis(self, ax):
        if ax == 'x': #Выбираем ось X
            self.sel_ax = self.x_axis
            return self.sel_ax
        #
        #
        if ax == 'y': #Выбираем ось Y
            self.sel_ax = self.y_axis
            return self.sel_ax
