import simple_math

def test_simple_add():
    assert simple_math.simple_add(1,3)==4

def test_simple_sub():
    assert simple_math.simple_sub(5,4)==1

def test_simple_mult():
    assert simple_math.simple_mult(3,5)==15

def test_simple_div():
    assert simple_math.simple_div(8,4)==2

def test_poly_first():
    assert simple_math.poly_first(2,4,-1)==2

def test_poly_second():
    assert simple_math.poly_second(2,5,1,2)==15

