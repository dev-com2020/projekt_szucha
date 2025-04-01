import unittest

def multiply(a,b):
    return a * b

class TestMuliply(unittest.TestCase):
    def helper(self, a, b, expected):
        result = multiply(a,b)
        self.assertEqual(result, expected)
    
    def test_multiply_cases(self):
        cases = [
            (2,3,6),
            (0,5,0),
            (-1,10,-10)
        ]
        for a,b,expected in cases:
            with self.subTest(a=a,b=b,expected=expected):
                self.helper(a,b,expected)