import pytest
from calculator import Calculator

calc = Calculator()

# --- Integration test 1: simulate addition flow ---
def test_addition_flow():
    a, b = 5, 3
    op = "+"
    
    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.subtract(a, b)
    elif op == "*":
        result = calc.multiply(a, b)
    elif op == "/":
        result = calc.divide(a, b)
    
    assert result == 8

# --- Integration test 2: clear after calculation ---
def test_clear_function():
    calc_result = calc.add(10, 5)
    cleared = calc.clear()
    
    assert cleared == 0
    assert calc_result == 15  # original calculation still correct

# --- Integration test 3: simulate subtraction flow ---
def test_subtraction_flow():
    a, b = 10, 4
    op = "-"
    
    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.subtract(a, b)
    elif op == "*":
        result = calc.multiply(a, b)
    elif op == "/":
        result = calc.divide(a, b)
    
    assert result == 6