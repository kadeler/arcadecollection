from Components.Component import *


class Collider(Component):
    def __init__(self, GeomOrPos, size = None):
        self.GeomOrPos = deepcopy(GeomOrPos)
        self.size = deepcopy(size) if size != None else None
        