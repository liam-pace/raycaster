import math

class Vector2D:
    __slots__ = ["__x", "__y"]

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def __eq__(self, o):
        if isinstance(o, Vector2D): return self.__x == o.__x and self.__y == o.__y
        else: return False
    def __neg__(self):
        return Vector2D(-self.__x, -self.__y) 

    def __add__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x + o.__x, self.__y + o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x + o, self.__y + o)
        else: raise TypeError
    def __sub__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x - o.__x, self.__y - o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x - o, self.__y - o)
        else: raise TypeError
    def __mul__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x * o.__x, self.__y * o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x * o, self.__y * o)
        else: raise TypeError
    def __truediv__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x / o.__x, self.__y / o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x / o, self.__y / o)
        else: raise TypeError
    def __pow__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x ** o.__x, self.__y ** o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x ** o, self.__y ** o)
        else: raise TypeError

    def __or__(self, o):
        if isinstance(o, Vector2D): diff = o - self; return (Vector2D(-diff.__y, diff.__x), Vector2D(diff.__y, -diff.__x))
        else: raise TypeError
    def __xor__(self, o):
        if isinstance(o, Vector2D): dot = self * o; return dot.__x + dot.__y
        else: raise TypeError 
    def __inverse__(self):
        return math.sqrt(self | self)
