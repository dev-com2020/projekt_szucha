import sys
import unittest

class SkipTestExample(unittest.TestCase):

    @unittest.skip("a bo tak!")
    def test_notImportant(self):
        self.fail("Wybucha cały system!!!")

    @unittest.skipIf(sys.version_info < (3,13), "Wymagamy python >= 3.12")
    def test_using_calendar(self):
        import calendar
        self.assertEqual(calendar.Month(4), calendar.APRIL)
    
    @unittest.skipUnless(sys.platform.startswith("win"), "Wymagamy MACOS!")
    def test_macos_support(self):
        from ctypes import WinDLL
        self.assertIsInstance(WinDLL)
    