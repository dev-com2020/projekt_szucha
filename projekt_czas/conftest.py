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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item):
    start_time = time.time()
    outcome = yield
    duration = time.time() - start_time
    item.duration = duration

def pytest_runtest_makereport(item,call):
    if call.when == "call":
        if hasattr(item,'duration') and item.duration > SLOW_TEST_THRESHOLD:
            if "slow" not in item.keywords:
                print(f"Test {item.name} trwał {item.duration:.2f}s - warto go oznaczyć slow")