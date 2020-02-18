#from Games.GSnake.SnakeManager import *
from ObjectsMng.OCircle import *


class Test:
    def __init__(self):

        self.a = OCircle()

        self.a.geom.position = Vector(100, 100)
        self.a.geom.radius = 1

        self.a.PointFind()


        self.b = OCircle()

        self.b.geom.position = Vector(100, 104)
        self.b.geom.radius = 4
        
        self.b.PointFind()
    

obj = Test()

obj.a.coll.collision = True
obj.b.coll.collision = True
obj.b.tag = 'pisya'

print(obj.a.coll.coll_obj.tag if obj.a.coll.Collision() else '')