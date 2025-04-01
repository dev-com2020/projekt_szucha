import sys
import unittest


sys.path.append('/Users/tomaszkaniecki/Desktop/projekt_szucha')
from serwisy.Calculator import Calculator


class TestCalculations(unittest.TestCase):

    def test_Given_DodajeDwieLiczby(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_sum(), 10, "The sum is wrong")
    
    def test_diff(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_differnces(), 6, "The diff is wrong")

    def test_product(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_product(), 16, "The product is wrong")

    def test_quote(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_quotient(), 4, "The quote is wrong")

if __name__ == '__main__':
    unittest.main()
