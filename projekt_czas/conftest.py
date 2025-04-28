import pytest
import time

SLOW_TEST_THRESHOLD = 1.0

def pytest_addoption(parser):
    parser.addoption(
        "--run-slow", action="store_true",
        default=False, help="Uruchamia testy powolne"
    )


def pytest_collection_modifyitems(config,items):
    run_slow = config.getoption("--run-slow")
    if not run_slow:
        skip_slow = pytest.mark.skip(reason="Pomijam testy bez flagi")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)

