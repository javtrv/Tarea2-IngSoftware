import unittest

class testPension(unittest.TestCase):
    
    def test_RecibePension(self):
        p = Pension()
        self.assertEqual(self,0, p.RecibePension)


if __name__=="__main__":
    unittest.main()