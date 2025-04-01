import unittest

class MySetupAndDownTest(unittest.TestCase):

    def setUp(self):
        self.data = [1,2,3]
        print("setup!")

    def test_sum(self):
        self.assertEqual(sum(self.data),6)
    
    def test_max(self):
        self.assertEqual(max(self.data),3)
    
    def tearDown(self):
        self.data.clear()
        print("Teardown!")

@classmethod
def setUpClass(cls):
    pass

@classmethod
def tearDownClass(cls):
    pass