import pytest
import requests
from unittest.mock import patch, Mock

def load_test_data_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    data = response.json()
    return [(item["userId"],item["title"]) for item in data]

@pytest.fixture
def mocked_api_data():
    mock_response = Mock()
    mock_response.json.return_value = [
        {
    "userId": 1,
    "title": "sunt aut facere repellat optio reprehenderit"},
    {
    "userId": 100,
    "title": "excepturi optio reprehenderit"},
    ]
    mock_response.raise_for_status = Mock()
    with patch('requests.get', return_value=mock_response):
        yield
    
@pytest.mark.usefixtures('mocked_api_data')
@pytest.mark.parametrize("userId,title",load_test_data_from_api())
def test_api_mocked(userId,title):
    assert isinstance(userId,int)
    assert isinstance(title, str)