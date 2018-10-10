import unittest # Modulo para realizar pruebas unitarias
from Pension import Pension # Modulo al cual se le haran las pruebas

class PruebasAnhoMayorQueActual(unittest.TestCase):
    '''
    Conjunto de pruebas de la funcion anho_mayor_que_actual,
    de no frontera, frontera frontera y de esquina
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

    def test_AnhoMayorQueAnho2030(self):
        '''
        Prueba: Ejecutar la funcion con 2030 como argumento
        Resultado esperado: True
        '''
        self.assertTrue(self.p.anho_mayor_que_actual(2030))

class PruebasAnhoMayorQueActualMalicia(unittest.TestCase):
    '''
    Conjunto de pruebas de malicia y casos invalidos de 
    la funcion anho_mayor_que_actual
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

    def test_AnhoMayorQueAnho100000(self):
        '''
        Prueba: Ejecutar la funcion con 100000 como argumento
        Resultado esperado: True
        '''
        self.assertTrue(self.p.anho_mayor_que_actual(100000))

    def test_AnhoMayorQueAnhoNegativo1(self):
        '''
        Prueba: Ejecutar la funcion con un numero negativo bajo como argumento
        Resultado esperado: False
        '''
        self.assertFalse(self.p.anho_mayor_que_actual(-5))

    def test_AnhoMayorQueAnhoNegativo2(self):
        '''
        Prueba: Ejecutar la funcion con un numero negativo alto como argumento
        Resultado esperado: False
        '''
        self.assertFalse(self.p.anho_mayor_que_actual(-100000))

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
    '''
    Conjunto de pruebas de la funcion calcular_edad,
    de no frontera, frontera frontera y de esquina
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

    def test_CalculaEdadCero(self):
        '''
        Prueba: Ejecuta la funcion con 2018 como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(2018))

    def test_CalculaEdad1(self):
        '''
        Prueba: Ejecuta la funcion con 2017 como parametro
        Resultado esperado: 1
        '''
        self.assertEqual(1, self.p.calcular_edad(2017))

    def test_CalculaEdad10(self):
        '''
        Prueba: Ejecuta la funcion con 2008 como parametro
        Resultado esperado: 10
        '''
        self.assertEqual(10, self.p.calcular_edad(2008))

    def test_CalculaEdad21(self):
        '''
        Prueba: Ejecuta la funcion con 1997 como parametro
        Resultado esperado: 21
        '''
        self.assertEqual(21, self.p.calcular_edad(1997))

    def test_CalculaEdadNoNacido(self):
        '''
        Prueba: Ejecuta la funcion con 2027 como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(2027))

    def test_CalculaEdadNoNacido2(self):
        '''
        Prueba: Ejecuta la funcion con 5027 como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(5027))

    def test_CalculaEdadNoNacido3(self):
        '''
        Prueba: Ejecuta la funcion con 2019 como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(2019))

class PruebasCalcularEdadMalicia(unittest.TestCase):
    '''
    Conjunto de pruebas de malicia y casos invalidos 
    de la funcion calcular_edad
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

    def test_CalculaEdadAnho0(self):
        '''
        Prueba: Ejecuta la funcion con 0 como parametro
        Resultado esperado: 2018
        '''
        self.assertEqual(2018, self.p.calcular_edad(0))

    def test_CalculaEdadAnhoNegativo1(self):
        '''
        Prueba: Ejecuta la funcion con numero negativo bajo como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(-5))

    def test_CalculaEdadAnhoNegativo2(self):
        '''
        Prueba: Ejecuta la funcion con numero negativo alto como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(-1000000))

    def test_EdadSinParametros(self):
        '''
        Prueba: Ejecutar la funcion sin argumentos
        Resultado esperado: Excepcion TypeError
        '''
        self.assertRaises(TypeError, self.p.calcular_edad)

    def test_EdadConParametroString(self):
        '''
        Prueba: Ejecutar la funcion con un argumento string
        Resultado esperado: Excepcion TypeError
        '''
        self.assertRaises(TypeError, self.p.calcular_edad, '10')


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
        self.assertFalse(self.p.recibe_pension(0, 'f', 0, 0))

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
    '''
    Conjunto de pruebas de malicia y casos invalidos 
    del argumento sexo para la funcion recibe_pension
    '''

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

    def test_IntroduceLetraIncorrecta1(self):
    	'''
        Prueba: Ejecuta la funcion con letra desconocida 'h' como parametro sexo
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'h', 1500, 0)

    def test_IntroduceLetraIncorrecta2(self):
    	'''
        Prueba: Ejecuta la funcion con letra desconocida 'k' como parametro sexo
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'k', 1500, 10)

    def test_IntroduceLetraIncorrecta3(self):
    	'''
        Prueba: Ejecuta la funcion con letra desconocida 'x' como parametro sexo
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'x', 1500, 5)

    def test_NoIntroduceLetra(self):
    	'''
        Prueba: Ejecuta la funcion con una letra vacia como parametro
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, '', 1500, 7)

class PruebasMaliciaInsalubridad(unittest.TestCase):
    '''
    Conjunto de pruebas de malicia y casos invalidos 
    del argumento anhos de insalubridad para la funcion recibe_pension
    '''

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

    def test_IntroduceInsalubridadNegativa(self):
        '''
        Prueba: Ejecuta la funcion con numero negativo bajo como parametro
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1940, 'f', 1500, -1)

    def test_IntroduceInsalubridadNegativa2(self):
        '''
        Prueba: Ejecuta la funcion con numero negativo medio como parametro
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1940, 'f', 1500, -100)

    def test_IntroduceInsalubridadNegativa3(self):
        '''
        Prueba: Ejecuta la funcion con numero negativo alto como parametro
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1940, 'f', 1500, -10000000)

if __name__=="__main__":
    unittest.main()