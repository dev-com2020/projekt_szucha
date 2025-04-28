from math_tools import add,divide
import pytest

def test_addition():
    assert add(2,3) == 5

def test_add(sample_numbers):
    a,b = sample_numbers
    assert add(a,b) == 9

def test_division():
    assert divide(10,2) == 5

def test_division_by_zero():
    try:
        divide(10,0)
        assert False, "Powinien być wyjątek"
    except ValueError as e:
        assert str(e) == "Nie dzielimy przez 0"

def test_division_by_zero_2():
    with pytest.raises(ValueError, match="Nie dzielimy przez 0"):
        divide(10,0)