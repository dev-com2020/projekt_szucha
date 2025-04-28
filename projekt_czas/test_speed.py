import pytest
import time

def test_fast_1():
    time.sleep(0.1)
    assert True

def test_fast_2():
    time.sleep(0.3)
    assert True

@pytest.mark.slow
def test_slow_1():
    time.sleep(1.1)
    assert True

def test_slow_2():
    time.sleep(1.5)
    assert True