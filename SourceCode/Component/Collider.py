from ObjectsMng.Object import *


class Collider(Object):

    def __init__(self, object = Object()):
        self.object = object


    def fix_field(self):
        self.position = self.object.position
        self.size = self.object.size

    def circleT(self):
        pass

    def rectT(self):
        pass

    def polygonT(self):
        pass