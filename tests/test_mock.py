from unittest.mock import Mock, patch
import unittest

mock = Mock()
mock.say_hello.return_value = "Hej!"

print(mock.say_hello())

mock.say_hello.assert_called_once()


mock.method.side_effect = [1,2,3]
print(mock.method())
print(mock.method())
print(mock.method())

mock.obiekt(42)
# mock.obiekt(62)

mock.obiekt.assert_called()
mock.obiekt.assert_called_once()
mock.obiekt.assert_called_with(42)
mock.obiekt.assert_called_once_with(42)

def fetch_data():
    import requests
    response = requests.get("https://swapi.dev/api/people/1")
    return response.json()

# dane = fetch_data()
# print(dane)


class TestFetchData(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_data(self,mock_get):
        mock_get.return_value.json.return_value = {"name":"Shrek"}
        result = fetch_data()
        self.assertEqual(result, {"name":"Shrek"})