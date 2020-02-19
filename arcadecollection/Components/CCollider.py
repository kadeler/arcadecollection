from ObjectsMng.OInformation import *
#


class CCollider:

    def __init__(self, obj):
        #Состояния:
        self.collision = False
        self.trigger = False

        #Объект внутри данного объекта
        self.insider = None

        #Текущий объект
        self.object = obj


    #Проверка на вхождение в объект
    def Inside(self):
        for obj in OArray:
            if not(obj is self.object):
                if self.object.point.intersection(obj.point) != set():
                    return obj
            #
            #
        return None


    #Проверка на столкновение
    def Collision(self):
        self.coll_obj = self.Inside()

        if self.coll_obj != None:
            if self.collision and self.coll_obj.coll.collision:
                if self.object.coll.collision and self.insider.coll.collision:
                    return True
                #
                #
        return False 


    #Проверка на триггер
    def Trigger(self):
        self.trig_obj = self.Inside()

        if self.trig_obj != None:
            if self.trigger and self.trig_obj.coll.trigger:
                if self.object.coll.trigger and self.insider.coll.trigger:
                    return True
                #
                #
        return False