from ObjectsMng.Field import *
#Этот файл создан для дополнительной обработки значений x и y!
#Вот так вот!
#

#Параметры объекта
class GeneralField(Field):

    main_axis = False

    size = 0 #Размер
    position = 0 #Позиция
    vector = 0 #Вектор



#По x:
class _X(GeneralField):

    def begin(self, obj):
        if obj != None:
            self.size = obj.size.x
            self.position = obj.position.x
            self.vector = obj.vector.x

        return (self.position, self.vector, self.main_axis)

    def end(self, obj):
        if obj != None:
            obj.size.x = self.size
            obj.position.x = self.position
            obj.vector.x = self.vector
        

    def __init__(self, obj):
        self.begin(obj)

#По y:
class _Y(GeneralField):    

    def begin(self, obj):
        if obj != None:
            self.size = obj.size.y
            self.position = obj.position.y
            self.vector = obj.vector.y
        
        return (self.position, self.vector, self.main_axis)

    def end(self, obj):
        if obj != None:
            obj.size.y = self.size
            obj.position.y = self.position
            obj.vector.y = self.vector

    def __init__(self, obj):
        self.begin(obj)


class Axes:
    x = None
    y = None

    def inside(self, obj):
        return (self.x.begin(obj),
                self.y.begin(obj))

    def outside(self, obj):
        return (self.x.end(obj),
                self.y.end(obj))

    def __init__(self, obj = Field()):

        #Оси:
        self.x = _X(obj)
        self.y = _Y(obj)

