# def test_monkey(monkeypatch):
#     monkeypatch.setattr(module_or_object,"attr_name",new_value)
#     monkeypatch.setenv("ENV_VAR",new_value)
import os

class App:
    def get_user_name():
        return "Real User"
    def get_api_key():
        return os.getenv("JHD87347FHUE")


def test_get_user_name_monk(monkeypatch):
    monkeypatch.setattr(App,"get_user_name",lambda: "Test User")
    assert App.get_user_name() == "Test User"

def test_get_api_key(monkeypatch):
    monkeypatch.setenv("JHD87347FHUE", "fake-key-123")
    assert App.get_api_key() == "fake-key-123"

def test_env_missing(monkeypatch):
    monkeypatch.delenv("JHD87347FHUE", raising=False)
    assert App.get_api_key() is None

