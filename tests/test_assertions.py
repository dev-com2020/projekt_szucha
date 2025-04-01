import unittest

class TestAsercjiUnitTest(unittest.TestCase):

    def test_assertNotEqual(self):
        # sprawdza nierówność
        self.assertNotEqual(2 + 2, 5)
    
    def test_assertTrue(self):
        self.assertTrue(3 < 5)

    def test_assertFalse(self):
        self.assertFalse(3 > 5)
    
    def test_assertIsNot(self):
        a = object()
        b = object()
        self.assertIsNot(a,b)

    def test_assertIsNone(self):
        self.assertIsNone(None)

    def test_assertIsNotNone(self):
        self.assertIsNotNone(123)
    
    def test_assertIn(self):
        self.assertIn(3,[1,2,3])
    
    def test_assertNotIn(self):
        self.assertNotIn(4,[1,2,3])

    def test_assertIsIstance(self):
        self.assertIsInstance("hej",str)
    
    def test_assertNotIsIstance(self):
        self.assertNotIsInstance("hi",int)

    def test_assertGreater(self):
        self.assertGreater(5,3)
    
    def test_assertGreaterEqual(self):
        self.assertGreaterEqual(5,5)

    def test_assertLess(self):
        self.assertLess(3,5)
    
    def test_assertLessEqual(self):
        self.assertLessEqual(5,5)  
    
    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=1)
    
    def test_assertNotAlmostEqual(self):
        self.assertNotAlmostEqual(0.1 + 0.2, 0.4, places=1)
    
    def test_assertRaises(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1/0
    
    def test_assertLogs(self):
        """Test logowania"""
        import logging
        logger = logging.getLogger('test_loggera')
        with self.assertLogs(logger, level="INFO") as cm:
            logger.info("test message")
        self.assertIn("test message", cm.output[0])
    


if __name__ == '__main__':
    unittest.main(verbosity=2)