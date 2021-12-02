from math import radians, sqrt
from geometry import *

TYPE_VALUES = [list(), set(), dict(), "Hello World!", False]




# VECTOR2D CLASS

def test_vector_invalid_constructor():
    try:
        for value in TYPE_VALUES:
            _ = Vector2D(value, value)
            print("CONSTRUCTOR Failed To Enforce With Type: ", type(value))
            assert False
    except TypeError:
        assert True

def test_vector_equality():
    v = Vector2D(1,2)
    v2 = Vector2D(1,2)
    v3 = Vector2D(30, 2)
    assert (v == v2) == True
    assert (v == v3) == False
    assert (v2 == v3) == False

def test_vector_getters():
    v = Vector2D(1,2)
    assert v.X() == 1
    assert v.Y() == 2

def test_vector_setters():
    v = Vector2D(1,2); v.X(10); v.Y(20)
    assert v.X() == 10
    assert v.Y() == 20

def test_vector_invalid_setters():
    v = Vector2D(0,0)
    try:
        for value in TYPE_VALUES:
            v.X(value)
            print("X POSITION Failed To Enforce With Type: ", type(value))
            v.Y(value)
            print("Y POSITION Failed To Enforce With Type: ", type(value))
            assert False
    except TypeError:
        assert True

def test_vector_operators():
    v = Vector2D(1,1)
    v2 = Vector2D(2,2)
    norms = v | v2
    assert (v + v2) == Vector2D(3,3)
    assert (v - v2) == Vector2D(-1,-1)
    assert (v * v2) == Vector2D(2,2)
    assert (v / v2) == Vector2D(0.5,0.5)
    assert (v ** v2) == Vector2D(1,1)
    assert (v ^ v2) == 4
    assert norms[0] == Vector2D(-1/sqrt(2), 1/sqrt(2))
    assert norms[1] == Vector2D(1/sqrt(2), -1/sqrt(2))




# TRANSFORM CLASS

def test_transform_invalid():
    try:
        for value in TYPE_VALUES:
            _ = Transform(value, value, value)
            print("CONSTRUCTOR Failed To Enforce With Type: ", type(value))
            assert False
    except TypeError:
        assert True

def test_transform_equality():
    t1 = Transform(Vector2D(10,10), 0, Vector2D(10,10))
    t2 = Transform(Vector2D(20,20), 0, Vector2D(10,10))
    t3 = Transform(Vector2D(10,10), 0, Vector2D(20,20))
    t4 = Transform(Vector2D(20,20), 0, Vector2D(20,20))
    t5 = Transform(Vector2D(10,10), 0, Vector2D(10,10))

    assert (t1 == t2) == False
    assert (t1 == t3) == False
    assert (t1 == t4) == False
    assert (t1 == t5) == True

def test_transform_getters():
    t = Transform(Vector2D(0,0), 0, Vector2D(1,1))
    assert t.Position() == Vector2D(0,0)
    assert t.Rotation() == 0
    assert t.Scale() == Vector2D(1,1)

def test_transform_setters():
    t = Transform(Vector2D(0,0), 0, Vector2D(1,1))
    t.Position(Vector2D(1,1))
    t.Rotation(5)
    t.Scale(Vector2D(10,10))
    assert t.Position() == Vector2D(1,1)
    assert t.Rotation() == 5
    assert t.Scale() == Vector2D(10,10)

def test_transform_invalid_setters():
    t = Transform(Vector2D(0,0), 0, Vector2D(0,0))
    try:
        for value in TYPE_VALUES:
            t.Rotation(value)
            print("ROTATION Failed To Enforce With Type: ", type(value))
            t.Position(value)
            print("POSITION Failed To Enforce With Type: ", type(value))
            t.Scale(value)
            print("SCALE Failed To Enforce With Type: ", type(value))
            assert False
    except TypeError:
        assert True

def test_transform_operators():
    t1 = Transform(Vector2D(0,0), 0, Vector2D(1,1))
    t2 = Transform(Vector2D(10,10), 90, Vector2D(5,5))
    t3 = Transform(Vector2D(-5, 40), -45, Vector2D(0.5,0.5))
    assert (t1 * t2) == t2
    assert (t2 * t1) == t2
    assert (t2 * t3) == Transform(Vector2D(5, 50), 45, Vector2D(2.5,2.5))
    assert (t3 * t2) == Transform(Vector2D(5, 50), 45, Vector2D(2.5,2.5))

def test_transform_vector():
    v = Vector2D(2,2)
    t = Transform(Vector2D(10,10), 45, Vector2D(5,5))
    c = math.cos(radians(45))
    s = math.sin(radians(45))
    result = v * t
    expected = Vector2D((2*5)*c-(2*5)*s + 10,(2*5)*s+(2*5)*c + 10)
    assert result == expected 