import pytest

def get_user_class():
    return "admin"

def test_default_user():
    x = get_user_class()
    assert x == "admin"

def get_admin_priv():
    return {"write","read","delete"}

def test_admin_priv():
    expected = {"write","delete"}
    actual = get_admin_priv()
    assert expected.issubset(actual)

def test_floats():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def get_user():
    return "guest"

def test_get_user():
    role = get_user()
    if role != "admin":
        pytest.fail(f"niepoprawna nazwa w bazie: {role}")

def test_skip():
    pytest.skip("Nie gotowe!")