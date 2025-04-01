import sys
import unittest


sys.path.append('/Users/tomaszkaniecki/Desktop/projekt_szucha')
from serwisy.Calculator import Calculator


class TestCalculationsWithSetup(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(8, 2)

    def test_Given_DodajeDwieLiczby(self):
        self.assertEqual(self.calc.get_sum(), 10, "The sum is wrong")
    
    def test_diff(self):
        self.assertEqual(self.calc.get_differnces(), 6, "The diff is wrong")

    def test_product(self):
        self.assertEqual(self.calc.get_product(), 16, "The product is wrong")

    def test_quote(self):
        self.assertEqual(self.calc.get_quotient(), 4, "The quote is wrong")

if __name__ == '__main__':
    unittest.main()
