import sys
import unittest

from serwisy.categorize import categorize_by_age


sys.path.append('/Users/tomaszkaniecki/Desktop/projekt_szucha')



class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):
        self.assertEqual(categorize_by_age(5),"Child...","błąd!")
    
    def test_adolescent(self):
        self.assertEqual(categorize_by_age(9),"Child","pokazuje inny komunikat!")

if __name__ == '__main__':
    unittest.main()
