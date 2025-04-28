import pytest

@pytest.fixture(params=[1,2,3])
def number(request):
    return request.param

@pytest.fixture(params=["+","-"])
def operator(request):
    return request.param

def test_pos(number):
    assert number > 0

def test_calculation(number,operator):
    if operator == "+":
        result = number + number
    else:
        result = number - number
    assert isinstance(result,int)