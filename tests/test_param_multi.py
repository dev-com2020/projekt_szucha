from parameterized import parameterized
import unittest

class TestMultiParam(unittest.TestCase):

    @parameterized.expand([
        ("positive", 2,3,6),
        ("zero", 0,5,0),
        ("negative", -1,10,-10)
    ])
    def test_multi_param(self,name,a,b,expected):
        self.assertEqual(a * b, expected)
