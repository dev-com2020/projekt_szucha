import pytest
import sys
import os

only_linux = sys.platform != "linux"
only_python_11 = sys.version_info[:2] != (3,11)
ci_env = os.getenv("CI") == 'true'

@pytest.mark.skipif(only_linux,reason="Test na linux")
def test_only_linux():
    assert True

@pytest.mark.skipif(only_python_11,reason="Test na 3.11")
def test_only_11():
    assert True
