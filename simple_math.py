"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    The sum of two numbers
    """
    return a+b

def simple_sub(a,b):
    """
    The subtraction of two numbers
    """
    return a-b

def simple_mult(a,b):
    """
    The product of two numbers
    """
    return a*b

def simple_div(a,b):
    """
    The division of two numbers
    """
    return a/b

def poly_first(x, a0, a1):
    """
    The first-order polynomial of a1 for x with constant a0
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    The second-order polynomial of a2 for x - extended on the poly_first() function
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
