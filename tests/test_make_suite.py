import unittest
from test_mock import TestFetchData
from test_zadanie import TestUserContoller
import sys


def make_suite():
        dwa_testy = unittest.TestSuite()
        dwa_testy.addTest(TestUserContoller)
        dwa_testy.addTest(TestFetchData)
        return dwa_testy

if __name__ == "__main__":
    sys.path.append('/Users/tomaszkaniecki/Desktop/projekt_szucha/tests')
    suite = make_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)