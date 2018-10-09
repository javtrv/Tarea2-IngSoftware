import unittest
from Pension import * 
class testPension(unittest.TestCase):
    
    def test_RecibePension(self):
        p = Pension()
        self.assertEqual(0, p.RecibePension())

    def test_Fecha_Ingresada_Mayor_Fecha_Actual1(self):
        p = Pension()
        self.assertEqual(0,p.CompararFecha(1995))

    def test_Fecha_Ingresada_Mayor_Fecha_Actual2(self):
        p = Pension()
        self.assertEqual(0,p.CompararFecha(2007))

    def test_Fecha_Ingresada_Mayor_Fecha_Actual3(self):
        p = Pension()
        self.assertEqual(0,p.CompararFecha(2020))


if __name__=="__main__":
    unittest.main()