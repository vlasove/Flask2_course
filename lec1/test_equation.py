import equation 

def test_linear():
    assert equation.linear(1,2) == 1
    assert equation.linear(0, 1) == 0
    assert equation.linear(5, 0) == 1

def test_quadratic():
    assert equation.quadratic(2,1,2) == 0
    assert equation.quadratic(2, 10, 1) == 2 
    assert equation.quadratic(1, 0 ,0) == 1 

def test_solve():
    assert equation.solve(2,1,2) == 0
    assert equation.solve(0 ,1, 2) == 1

