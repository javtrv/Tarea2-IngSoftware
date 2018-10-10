import unittest
from Pension import Pension

class PruebasEdadMayor(unittest.TestCase):
    def setUp(self):
        self.p = Pension()

    def tearDown(self):
    	self.p = None

##### PRUEBAS DE EDAD MAYOR QUE ANHO ACTUAL

    def test_Fecha_Ingresada_Mayor_Fecha_Actual1(self):
        self.assertFalse(self.p.anho_mayor_que_actual(0))

    def test_Fecha_Ingresada_Mayor_Fecha_Actual2(self):
        self.assertFalse(self.p.anho_mayor_que_actual(2018))

    def test_Fecha_Ingresada_Mayor_Fecha_Actual3(self):
        self.assertTrue(self.p.anho_mayor_que_actual(2020))


class PruebasDeRequisitos(unittest.TestCase):
    def setUp(self):
        self.p = Pension()

    def tearDown(self):
    	self.p = None

##### PRUEBAS DE REQUISITOS EN RecibePension

    def test_RecibePension1(self):
        self.assertTrue(self.p.RecibePension(2012, 'f', 750))
    def test_RecibePension2(self):
        self.assertTrue(self.p.RecibePension(2000, 'm', 2131))
    def test_RecibePension3(self):
        self.assertTrue(self.p.RecibePension(1950, 'm', 200))
        
    def test_RecibePension4(self):
        self.assertFalse(self.p.RecibePension(1945, 'f', 750))
    def test_RecibePension5(self):
        self.assertFalse(self.p.RecibePension(1950, 'm', 1000))

if __name__=="__main__":
    unittest.main()