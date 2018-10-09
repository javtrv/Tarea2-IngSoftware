import unittest
from Pension import * 
class testPension(unittest.TestCase):
    
    def test_RecibePension(self):
        p = Pension()
        self.assertEqual(0, p.RecibePension())

    def test_Fecha_Ingresada_Mayor_Fecha_Actual(self):
        p = Pension()
        self.assertEqual(1,ObtenerFecha())


if __name__=="__main__":
    unittest.main()