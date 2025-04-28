import pytest
import sys

@pytest.mark.database
def test_connect_to_db():
    assert True

@pytest.mark.skip(reason="Nie gotowy!")
def test_future():
    assert False

@pytest.mark.xfail(reason="Brak implementacji")
def test_old_case():
    assert False

@pytest.mark.skipif(sys.platform == 'linux', reason="Test nie działa na linux")
def test_only_win():
    assert True