import pytest
import sys
import os

# Definicja warunków skip
only_linux = sys.platform != "linux"
is_windows = sys.platform == 'win32'
only_python_11 = sys.version_info[:2] != (3,11)
ci_env = os.getenv("CI") == 'true'

# globalne fixtury
@pytest.fixture
def sample_numbers():
    return 6,3

# skipowanie globalne

def pytest_collection_modifyitems(config,items):
    skip_windows = pytest.mark.skip(reason="pomijam testy na win")
    if is_windows:
        for item in items:
            item.add_marker(skip_windows)


