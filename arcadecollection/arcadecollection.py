#from Games.GSnake.SnakeManager import *
from ObjectsMng.ObjectTypeB import *

a = ObjectTypeB()


a.geom.y_axis.position = 100
a.geom.SelectAxis('y')

a.coll.geom.sel_ax.position = 200

print(a.geom.sel_ax.position)