# def test_monkey(monkeypatch):
#     monkeypatch.setattr(module_or_object,"attr_name",new_value)
#     monkeypatch.setenv("ENV_VAR",new_value)

class App:
    def get_user_name():
        return "Real User"


def test_get_user_name_monk(monkeypatch):
    monkeypatch.setattr(App,"get_user_name",lambda: "Test User")
    assert App.get_user_name() == "Test User"

