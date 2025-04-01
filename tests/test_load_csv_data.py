import unittest
import csv
from ddt import ddt,data,unpack

def load_csv_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(int(row['a']), int(row['b']),int(row['expected'])) for row in reader]

csv_data = load_csv_data("tests/dane.csv")

@ddt
class TestMultiFromCsv(unittest.TestCase):

    @data(*csv_data)
    @unpack
    def test_multi_csv(self, a, b, expected):
        self.assertEqual(a * b, expected)