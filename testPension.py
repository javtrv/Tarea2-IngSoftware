import unittest
from Pension import * 
class testPension(unittest.TestCase):
    def setUp(self):
        self.p = Pension()

    def test_RecibePension(self):
        self.assertEqual(0, self.p.RecibePension())

##### PRUEBAS DE EDAD MAYOR QUE ANHO ACTUAL

    def test_Fecha_Ingresada_Mayor_Fecha_Actual1(self):
        self.assertEqual(0,self.p.CompararFecha(1995))

    def test_Fecha_Ingresada_Mayor_Fecha_Actual2(self):
        self.assertEqual(0,self.p.CompararFecha(2007))

    def test_Fecha_Ingresada_Mayor_Fecha_Actual3(self):
        self.assertEqual(0,self.p.CompararFecha(2020))


if __name__=="__main__":
    unittest.main()