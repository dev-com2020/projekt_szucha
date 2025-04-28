import pytest
import sys
import os

# Definicja warunków skip
only_linux = sys.platform != "linux"
is_windows = sys.platform == 'win32'
is_linux = sys.platform == 'linux'
only_python_11 = sys.version_info[:2] != (3,11)
ci_env = os.getenv("CI") == 'true'

# globalne fixtury
@pytest.fixture
def sample_numbers():
    return 6,3

# skipowanie globalne

def pytest_collection_modifyitems(config,items):
    skip_linux = pytest.mark.skip(reason="pomijam testy na linuxa")
    if is_linux:
        for item in items:
            item.add_marker(skip_linux)


