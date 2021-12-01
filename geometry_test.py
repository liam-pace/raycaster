from math import sqrt
from geometry import *

def test_vector_improper_constructor():
    try: v = Vector2D("False", "True"); assert False; v = Vector2D(False, True); assert False; v = Vector2D([], []); assert False; v = Vector2D({}, {}); assert False
    except TypeError: assert True

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

def test_vector_improper_setters():
    try: v = Vector2D(1,2); v.X("Hello World"); assert False; v = Vector2D(1,2); v.Y("Hello World"); assert False; v = Vector2D(1,2); v.X(False); assert False; v = Vector2D(1,2); v.Y(True); assert False; v = Vector2D(1,2); v.X([]); assert False; v = Vector2D(1,2); v.Y([]); assert False; v = Vector2D(1,2); v.X({}); assert False; v = Vector2D(1,2); v.Y({}); assert False
    except TypeError: assert True

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