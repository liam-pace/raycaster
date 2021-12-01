import math

number_types = (float, int, complex)

class Vector2D:
    __slots__ = ["__x", "__y"]

    """
    Constructs A Vector Object
    """
    def __init__(self, x, y) -> None:
        if isinstance(x, number_types) and isinstance(y, number_types):self.__x = x;self.__y = y
        else:raise TypeError


    """
    Operator:  Equals
    Symbol:    ==
    Purpose:
        Determines If Two Vectors Are Equal
    """
    def __eq__(self, o):
        if isinstance(o, Vector2D):return self.__x==o.__x and self.__y==o.__y
        else:return False

    """
    Operator:  Uniary Subtraction
    Symbol:    -
    Purpose:
        Reflects The Vector Over The X and Y Axis
    """
    def __neg__(self):
        return Vector2D(-self.__x, -self.__y) 

    """
    Operator:  Addition
    Symbol:    +
    Purpose:
        Positivly Translates A Vector
    """
    def __add__(self, o):
        if isinstance(o, Vector2D):return Vector2D(self.__x+o.__x, self.__y+o.__y)
        elif isinstance(o, number_types):return Vector2D(self.__x+o, self.__y+o)
        else:raise TypeError

    """
    Operator:  Subtraction
    Symbol:    -
    Purpose:
        Negativly Translates A Vector
    """
    def __sub__(self, o):
        if isinstance(o, Vector2D):return Vector2D(self.__x-o.__x, self.__y-o.__y)
        elif isinstance(o, number_types):return Vector2D(self.__x-o, self.__y-o)
        else:raise TypeError

    """
    Operator:  Multiplication
    Symbol:    *
    Purpose:
        Scales A Vector Increasingly
    """
    def __mul__(self, o):
        if isinstance(o, Vector2D):return Vector2D(self.__x*o.__x, self.__y*o.__y)
        elif isinstance(o, number_types):return Vector2D(self.__x*o, self.__y*o)
        else:raise TypeError
    
    """
    Operator:  Division
    Symbol:    /
    Purpose:
        Scales A Vector Decreasingly
    """
    def __truediv__(self, o):
        if isinstance(o, Vector2D):return Vector2D(self.__x/o.__x, self.__y/o.__y)
        elif isinstance(o, number_types):return Vector2D(self.__x/o, self.__y/o)
        else:raise TypeError

    """
    Operator:  Exponentiation
    Symbol:    **
    Purpose:
        Scales A Vector Exponentially 
    """
    def __pow__(self, o):
        if isinstance(o, Vector2D):return Vector2D(self.__x**o.__x, self.__y**o.__y)
        elif isinstance(o, number_types):return Vector2D(self.__x**o, self.__y**o)
        else:raise TypeError

    """
    Operator:  Bitwise XOR
    Symbol:    ^
    Purpose:
        Provides The Dot Product Of Two Vectors
    """
    def __xor__(self, o):
        if isinstance(o, Vector2D):dot = self*o;return dot.__x+dot.__y
        else:raise TypeError
    
    """
    Operator:  Bitwise NOT
    Symbol:    ~
    Purpose:
        Normalizes The Current Vector Into A Unit Vector
    """
    def __invert__(self):
        return self/self.Mag()

    """
    Operator:  Bitwise OR
    Symbol:    |
    Purpose:
        Provides The Normals Between The Line Formed By Two Vectors
    """
    def __or__(self, o):
        if isinstance(o, Vector2D):diff = o-self;return (~Vector2D(-diff.__y, diff.__x), ~Vector2D(diff.__y, -diff.__x))
        else:raise TypeError

    """
    Sets or Returns The X Value Of This Vector
    """
    def X(self, x=None):
        if x==None:return self.__x
        elif isinstance(x, number_types):self.__x = x
        else:raise TypeError

    """
    Sets or Returns The Y Value Of This Vector
    """
    def Y(self, y=None):
        if y==None:return self.__y
        elif isinstance(y, number_types):self.__y = y
        else:raise TypeError

    """
    Returns The Length Of This Vector
    """
    def Mag(self):
        return math.sqrt(self^self)

    @staticmethod
    def Angle(degs):
        rads = math.radians(degs)
        return Vector2D(math.cos(rads), math.sin(degs))


class Transform:
    __slots__ = ["__position", "__rotation", "__scale"]
    
    def __init__(self, position, rotation, scale) -> None:
        if isinstance(position, Vector2D) and isinstance(rotation, number_types) and isinstance(scale, Vector2D):self.Position(position);self.Rotation(rotation);self.Scale(scale)
        else:raise TypeError

    def __mul__(self,o):
        if isinstance(o, Transform): return Transform(self.__position + o.__position, self.__rotation + o.__rotation, self.__scale * o.__scale)
        elif isinstance(o, Vector2D): scaled = o * self.__scale; trigg = Vector2D.Angle(self.__rotation); triggedA = scaled * trigg; triggedB = scaled * Vector2D(trigg.__y, trigg.__x); rotated = Vector2D(triggedA.__x - triggedA.__y, triggedB.__x + triggedB.__y); return rotated + self.__position
        else: raise TypeError

    def Position(self, position=None):
        if position==None:return self.__position
        elif isinstance(position, Vector2D):self.__position = position
        else:raise TypeError

    def Rotation(self, rotation=None):
        if rotation==None:return self.__rotation
        elif isinstance(rotation, number_types):self.__rotation = rotation
        else:raise TypeError

    def Scale(self, scale=None):
        if scale==None:return self.__scale
        elif isinstance(scale, Vector2D):self.__scale = scale
        else:raise TypeError