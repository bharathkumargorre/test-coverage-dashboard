import sys
import os

# Add src folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import utils


def test_add():
    assert utils.add(2, 3) == 5


def test_subtract():
    assert utils.subtract(10, 5) == 5


def test_multiply():
    assert utils.multiply(3, 4) == 12


def test_divide():
    assert utils.divide(10, 2) == 5


def test_divide_by_zero():
    assert utils.divide(10, 0) == "Cannot divide by zero"


def test_is_even():
    assert utils.is_even(4) is True
    assert utils.is_even(5) is False


def test_factorial():
    assert utils.factorial(5) == 120
    assert utils.factorial(0) == 1