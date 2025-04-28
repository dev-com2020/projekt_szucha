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