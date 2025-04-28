import pytest
import requests

@pytest.fixture(scope="session")
def test_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    data = response.json()
    return [(item["userId"],item["title"]) for item in data]

def pytest_generate_tests(metafunc):
    if "userId" in metafunc.fixturenames and "title" in metafunc.fixturenames:
        data = requests.get("https://jsonplaceholder.typicode.com/posts").json()
        params = [(item["userId"],item["title"]) for item in data]
        metafunc.parametrize("userId,title",params)

def test_api_better(userId,title):
    assert isinstance(userId,int)
    assert isinstance(title,str)