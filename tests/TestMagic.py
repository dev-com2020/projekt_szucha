from unittest.mock import MagicMock

mock_list = MagicMock()
mock_list.__len__.return_value = 3

print(len(mock_list))

mock_dict = MagicMock()

mock_dict.__getitem__.side_effect = lambda key: f"Value for {key}"

print(mock_dict['user'])

mock_iter = MagicMock()
mock_iter.__iter__.return_value = iter([1,2,3])

for x in mock_iter:
    print(x)

mock_func = MagicMock()
mock_func.return_value = 345
print(mock_func())


from unittest.mock import mock_open, patch

mock_file = mock_open(read_data="Czy to juz koniec?")

with patch("builtins.open", mock_file):
    with open("pliczke.txt") as f:
        content = f.read()
        print(content)