import math

class Vector2D:
    __slots__ = ["__x", "__y"]

    """
    Constructs A Vector Object
    """
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    """
        Returns the length of the vector
    """
    def mag(self):
        return math.sqrt(self^self)

    """
    Operator:   Equals
    Symbol:     ==
    Purpose:
        Determines If Two Vectors Are Equal
    """
    def __eq__(self, o):
        if isinstance(o, Vector2D): return self.__x == o.__x and self.__y == o.__y
        else: return False

    """
    Operator:   Uniary Subtraction
    Symbol:     -
    Purpose:
        Reflects The Vector Over The X and Y Axis
    """
    def __neg__(self):
        return Vector2D(-self.__x, -self.__y) 

    """
    Operator:   Addition
    Symbol:     +
    Purpose:
        Positivly Translates A Vector
    """
    def __add__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x + o.__x, self.__y + o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x + o, self.__y + o)
        else: raise TypeError

    """
    Operator:   Subtraction
    Symbol:     -
    Purpose:
        Negativly Translates A Vector
    """
    def __sub__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x - o.__x, self.__y - o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x - o, self.__y - o)
        else: raise TypeError

    """
    Operator:   Multiplication
    Symbol:     *
    Purpose:
        Scales A Vector Increasingly
    """
    def __mul__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x * o.__x, self.__y * o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x * o, self.__y * o)
        else: raise TypeError
    
    """
    Operator:   Division
    Symbol:     /
    Purpose:
        Scales A Vector Decreasingly
    """
    def __truediv__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x / o.__x, self.__y / o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x / o, self.__y / o)
        else: raise TypeError

    """
    Operator:   Exponentiation
    Symbol:     **
    Purpose:
        Scales A Vector Exponentially 
    """
    def __pow__(self, o):
        if isinstance(o, Vector2D): return Vector2D(self.__x ** o.__x, self.__y ** o.__y)
        elif isinstance(o, (float, int, complex)): return Vector2D(self.__x ** o, self.__y ** o)
        else: raise TypeError

    """
    Operator:   Bitwise OR
    Symbol:     |
    Purpose:
        Provides The Normals Between The Line Formed By Two Vectors
    """
    def __or__(self, o):
        if isinstance(o, Vector2D): diff = o - self; return (Vector2D(-diff.__y, diff.__x), Vector2D(diff.__y, -diff.__x))
        else: raise TypeError

    """
    Operator:   Bitwise XOR
    Symbol:     ^
    Purpose:
        Provides The Dot Product Of Two Vectors
    """
    def __xor__(self, o):
        if isinstance(o, Vector2D): dot = self * o; return dot.__x + dot.__y
        else: raise TypeError
    
    """
    Operator:   Bitwise NOT
    Symbol:     ~
    Purpose:
        Normalizes The Current Vector Into A Unit Vector
    """
    def __inverse__(self):
        return self / self.mag()
