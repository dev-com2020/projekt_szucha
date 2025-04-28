import pytest
import requests

def load_test_data_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    data = response.json()
    return [(item["userId"],item["title"]) for item in data]

@pytest.mark.parametrize("userId,title",load_test_data_from_api())
def test_api(userId,title):
    pass