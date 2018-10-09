import unittest
from Pension import * 
class testPension(unittest.TestCase):
    
    def test_RecibePension(self):
        p = Pension()
        self.assertEqual(0, p.RecibePension())


if __name__=="__main__":
    unittest.main()