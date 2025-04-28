from math_tools import add,divide

def test_addition():
    assert add(2,3) == 5

def test_division():
    assert divide(10,2) == 5

def test_division_by_zero():
    try:
        divide(10,0)
        assert False, "Powinien być wyjątek"
    except ValueError as e:
        assert str(e) == "Nie dzielimy przez 0"