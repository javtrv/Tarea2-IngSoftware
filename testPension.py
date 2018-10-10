import unittest # Modulo para realizar pruebas unitarias
from Pension import Pension # Modulo al cual se le haran las pruebas

class PruebasAnhoMayor(unittest.TestCase):
    '''
    Conjunto de pruebas de la funcion anho mayor,
    de frontera y de esquina
    '''

    # Configuracion

    def setUp(self):
        '''
        Instancia el modulo Pension y configura el anho actual
        de manera directa para poder controlar las pruebas
        '''
        self.p = Pension()
        self.p.anho_actual = 2018

    def tearDown(self):
        '''
        Elimina la instancia del modulo Pension
        asociada a la prueba
        '''
        self.p = None

    # Pruebas

    def test_AnhoMayorQueAnho0(self):
        '''
        Prueba: Ejecutar la funcion con 0 como argumento
        Resultado esperado: False
        '''
        self.assertFalse(self.p.anho_mayor_que_actual(0))

    def test_AnhoMayorQueAnho2017(self):
        '''
        Prueba: Ejecutar la funcion con 2017 como argumento
        Resultado esperado: False
        '''
        self.assertFalse(self.p.anho_mayor_que_actual(2017))

    def test_AnhoMayorQueAnho2018(self):
        '''
        Prueba: Ejecutar la funcion con 2018 como argumento
        Resultado esperado: False
        '''
        self.assertFalse(self.p.anho_mayor_que_actual(2018))

    def test_AnhoMayorQueAnho2019(self):
        '''
        Prueba: Ejecutar la funcion con 2019 como argumento
        Resultado esperado: True
        '''
        self.assertTrue(self.p.anho_mayor_que_actual(2019))

    def test_AnhoMayorQueAnho2020(self):
        '''
        Prueba: Ejecutar la funcion con 2020 como argumento
        Resultado esperado: True
        '''
        self.assertTrue(self.p.anho_mayor_que_actual(2020))

    def test_AnhoMayorQueAnho100000(self):
        '''
        Prueba: Ejecutar la funcion con 100000 como argumento
        Resultado esperado: True
        '''
        self.assertTrue(self.p.anho_mayor_que_actual(100000))

class PruebasAnhoMayorMalicia(unittest.TestCase):
    '''
    Conjunto de pruebas de malicia de la funcion anho mayor
    '''

    # Configuracion

    def setUp(self):
        '''
        Instancia el modulo Pension
        '''
        self.p = Pension()

    def tearDown(self):
        '''
        Elimina la instancia del modulo Pension
        asociada a la prueba
        '''
        self.p = None

    # Pruebas

    def test_AnhoSinParametros(self):
        '''
        Prueba: Ejecutar la funcion sin argumentos
        Resultado esperado: Excepcion TypeError
        '''
        self.assertRaises(TypeError, self.p.anho_mayor_que_actual)

    def test_AnhoConParametroString(self):
        '''
        Prueba: Ejecutar la funcion con un argumento string
        Resultado esperado: Excepcion TypeError
        '''
        self.assertRaises(TypeError, self.p.anho_mayor_que_actual, '2010')

class PruebasCalcularEdad(unittest.TestCase):
    def setUp(self):
        '''
        Instancia el modulo Pension y configura el anho actual
        de manera directa para poder controlar las pruebas
        '''
        self.p = Pension()
        self.p.anho_actual = 2018

    def tearDown(self):
        '''
        Elimina la instancia del modulo Pension
        asociada a la prueba
        '''
        self.p = None

    def test_Calcula_Edad_Cero(self):
        self.assertEqual(0, self.p.calcular_edad(2018))

    def test_Calcula_Edad_10(self):
        self.assertEqual(10, self.p.calcular_edad(2008))

    def test_Calcula_Edad_21(self):
        self.assertEqual(21, self.p.calcular_edad(1997))

    def test_Calcula_Edad_No_Nacido(self):
        self.assertEqual(0, self.p.calcular_edad(2027))

    def test_Calcula_Edad_Anho_0(self):
        self.assertEqual(2018, self.p.calcular_edad(0))

class PruebasDeRequisitos(unittest.TestCase):
    def setUp(self):
        '''
        Instancia el modulo Pension
        '''
        self.p = Pension()

    def tearDown(self):
        '''
        Elimina la instancia del modulo Pension
        asociada a la prueba
        '''
        self.p = None

    def test_RecibePension1(self):
        self.assertFalse(self.p.recibe_pension(2012, 'f', 750, 0))
    def test_RecibePension2(self):
        self.assertFalse(self.p.recibe_pension(2000, 'm', 2131, 0))
    def test_RecibePension3(self):
        self.assertFalse(self.p.recibe_pension(1950, 'm', 200, 0))

    def test_RecibePension4(self):
        self.assertTrue(self.p.recibe_pension(1945, 'f', 750, 0))
    def test_RecibePension5(self):
        self.assertTrue(self.p.recibe_pension(1950, 'm', 1000, 0))

    def test_RecibePension6(self):
        self.assertTrue(self.p.recibe_pension(1958, 'm', 750, 0))
    def test_RecibePension7(self):
        self.assertTrue(self.p.recibe_pension(1963, 'f', 750, 0))

    def test_RecibePension8(self):
        self.assertFalse(self.p.recibe_pension(1959, 'm', 750, 0))
    def test_RecibePension9(self):
        self.assertFalse(self.p.recibe_pension(1964, 'f', 750, 0))

    def test_RecibePension10(self):
        self.assertFalse(self.p.recibe_pension(0, '', 0, 0))

class PruebasInsalubridad(unittest.TestCase):
    def setUp(self):
        '''
        Instancia el modulo Pension
        '''
        self.p = Pension()

    def tearDown(self):
        '''
        Elimina la instancia del modulo Pension
        asociada a la prueba
        '''
        self.p = None

    def test_Recibe_Pension_Sin_Insalubridad(self):
        self.assertTrue(self.p.recibe_pension(1960, 'f', 1500, 0))

    def test_Recibe_Pension_Con_Insalubridad(self):
        self.assertTrue(self.p.recibe_pension(1960, 'm', 1500, 10))

    def test_No_Recibe_Pension_Con_Insalubridad(self):
        self.assertFalse(self.p.recibe_pension(2010, 'f', 500, 15))

class PruebasMaliciaSexo(unittest.TestCase):
    def setUp(self):
        '''
        Instancia el modulo Pension
        '''
        self.p = Pension()

    def tearDown(self):
        '''
        Elimina la instancia del modulo Pension
        asociada a la prueba
        '''
        self.p = None

    def test_Introduce_Letra_Incorrecta1(self):
        self.assertFalse(self.p.recibe_pension(1950, 'h', 1500, 0))

    def test_Introduce_Letra_Incorrecta2(self):
        self.assertFalse(self.p.recibe_pension(1950, 'k', 1500, 10))

    def test_Introduce_Letra_Incorrecta3(self):
        self.assertFalse(self.p.recibe_pension(2050, 'q', 1500, 0))

    def test_No_Introduce_Letra(self):
        self.assertFalse(self.p.recibe_pension(2050, '', 1500, 0))

if __name__=="__main__":
    unittest.main()