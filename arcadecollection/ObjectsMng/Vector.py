class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    #Возможность сравнения векторов
    def __eq__(self, vec):
        return (self.x == vec.x and self.y == vec.y)


    #Возможность сложения векторов
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)


