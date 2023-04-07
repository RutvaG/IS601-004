#ucid:RG695 date:02/27/2023
from MyCalc import MyCalc

def test_add():
    r = MyCalc()
    s = r.add(6, 2)
    assert s == 8

#ucid:RG695 date:02/27/2023
def test_sub():
    r = MyCalc()
    s = r.sub(8, 2)
    assert s == 6

#ucid:RG695 date:02/27/2023
def test_mult():
    r = MyCalc()
    s = r.mult(5, 4)
    assert s == 20

#ucid:RG695 date:02/27/2023
def test_div():
    r = MyCalc()
    s = r.div(20, 4)
    assert s == 5

#ucid:RG695 date:02/27/2023
def test_add():
    x = MyCalc()
    ans = x.add(6,6)
    result = x.add(ans, 4)
    assert result == 16

#ucid:RG695 date:02/27/2023
def test_sub():
    r = MyCalc()
    ans = r.sub(8,4)
    result = r.sub(ans, 2)
    assert result == 2

#ucid:RG695 date:02/27/2023
def test_mult():
    r = MyCalc()
    sol = r.mult(5, 4)
    result = r.mult(sol, 2)
    assert result == 40

#ucid:RG695 date:02/27/2023
def test_div():
    r = MyCalc()
    sol = r.div(16, 4)
    result = r.div(sol, 4)
    assert result == 1
