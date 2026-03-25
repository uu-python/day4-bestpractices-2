"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Add two numbers.

    Parameters:
    a (float or int): First number
    b (float or int): Second number

    Returns:
    float or int: Sum of a and b
    """
    return a+b

def simple_sub(a,b):
    """
    Subtract two numbers.

    Parameters:
    a (float or int): Minuend
    b (float or int): Subtrahend

    Returns:
    float or int: Difference of a minus b
    """
    return a-b

def simple_mult(a,b):
    """
    Multiply two numbers.

    Parameters:
    a (float or int): First number
    b (float or int): Second number

    Returns:
    float or int: Product of a and b
    """
    return a*b

def simple_div(a,b):
    """
    Divide two numbers.

    Parameters:
    a (float or int): Dividend
    b (float or int): Divisor (must not be zero)

    Returns:
    float or int: Quotient of a divided by b

    Raises:
    ZeroDivisionError: If b is zero
    """
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
