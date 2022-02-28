import simple_math

def test_simple_math():
    assert simple_math.simple_add(1,1) == 2

def test_simple_sub():
    assert simple_math.simple_sub(1,1) == 0

def test_simple_mult():
    assert simple_math.simple_mult(1,1) == 1

def test_simple_div():
    assert simple_math.simple_div(1,1) == 1

def test_poly_first():
    assert simple_math.poly_first(1,1,1) == 2

def test_poly_second():
    assert simple_math.poly_second(1,1,1,1) == 3
