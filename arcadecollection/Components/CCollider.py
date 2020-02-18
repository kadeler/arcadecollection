from ObjectsMng.OInformation import *
#


class CCollider:

    def __init__(self, obj):
        #Состояния:
        self.collision = False
        self.trigger = False

        self.object = obj


    #Проверка на вхождение в объект
    def Inside(self):
        for obj in OArray:
            if not(obj is self.object):
                if self.object.point.intersection(obj.point) != set():
        #
                    self.insider = obj
                    return True
        #
        return False
    #
    #


    #Проверка на столкновение
    def Collision(self):
        if self.object.coll.collision and obj.coll.collision:
            self.coll_obj = self.insider
            return True

        else:
            return False

    #Проверка на триггер
    def Trigger(self):
        if self.object.coll.trigger and obj.coll.trigger:
            self.trig_obj = self.insider
            return True

        else:
            return False