import pytest
import sys
import os
from conftest import only_linux,only_python_11

@pytest.mark.skipif(only_linux,reason="Test na linux")
def test_only_linux():
    assert True

@pytest.mark.skipif(only_python_11,reason="Test na 3.11")
def test_only_11():
    assert True
