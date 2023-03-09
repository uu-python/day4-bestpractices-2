# test_fib_params.py
import fib
import pytest

# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 
@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 2),
    (3, 5)
])
def test_fib_parametrized(n, expected):
    assert fib.fib(n) == expected
