from app.controllers.math import inc, minus, power  

def test_inc():
    assert inc(3) == 4
    assert inc(0) == 1
    assert inc(-1) == 0
    assert inc(100) == 101

def test_minus():
    assert minus(3) == 2
    assert minus(0) == -1
    assert minus(-1) == -2
    assert minus(100) == 99

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(7, 1) == 7
    assert power(10, 2) == 100

