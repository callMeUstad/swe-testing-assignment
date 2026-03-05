import pytest
from calculator import Calculator

calc = Calculator()

# --- Basic operations ---
def test_add():
    assert calc.add(5, 3) == 8

def test_subtract():
    assert calc.subtract(10, 4) == 6

def test_multiply():
    assert calc.multiply(6, 7) == 42

def test_divide():
    assert calc.divide(20, 4) == 5

# --- Edge cases ---
def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_negative_numbers():
    assert calc.add(-2, -3) == -5
    assert calc.subtract(-5, -2) == -3

def test_decimal_numbers():
    assert calc.multiply(2.5, 4) == 10.0
    assert calc.divide(5.0, 2) == 2.5

def test_large_numbers():
    assert calc.add(1_000_000_000, 2_000_000_000) == 3_000_000_000