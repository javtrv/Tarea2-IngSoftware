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

    def test_AnhoMayorQueAnhoNegativo(self):
        '''
        Prueba: Ejecutar la funcion con un numero negativo como argumento
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.anho_mayor_que_actual, -5)
        self.assertRaises(ValueError, self.p.anho_mayor_que_actual, -100000)

    def test_AnhoSinParametros(self):
        '''
        Prueba: Ejecutar la funcion sin argumentos
        Resultado esperado: Excepcion TypeError
        '''
        self.assertRaises(TypeError, self.p.anho_mayor_que_actual)

    def test_AnhoConParametroString(self):
        '''
        Prueba: Ejecutar la funcion con un argumento string
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.anho_mayor_que_actual, '2010')

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
        Prueba: Ejecuta la funcion con anhos en el futuro como parametro
        Resultado esperado: 0
        '''
        self.assertEqual(0, self.p.calcular_edad(2027))
        self.assertEqual(0, self.p.calcular_edad(5027))
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

    def test_CalculaEdadAnhoNegativo(self):
        '''
        Prueba: Ejecuta la funcion con numero negativo como parametro
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.calcular_edad, -5)
        self.assertRaises(ValueError, self.p.calcular_edad, -1000000)

    def test_EdadSinParametros(self):
        '''
        Prueba: Ejecutar la funcion sin argumentos
        Resultado esperado: Excepcion TypeError
        '''
        self.assertRaises(TypeError, self.p.calcular_edad)

    def test_EdadConParametroString(self):
        '''
        Prueba: Ejecutar la funcion con un argumento string
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.calcular_edad, '10')


class PruebasRecibePension(unittest.TestCase):
    '''
    Conjunto de pruebas de la funcion recibe_pension,
    de no frontera, frontera frontera y de esquina para
    sus argumentos en general
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

    def test_RecibePensionMuyJoven(self):
        '''
        Prueba: Ejecutar la funcion con una edad muy joven
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(2012, 'f', 750, 0))
        self.assertFalse(self.p.recibe_pension(2000, 'm', 2131, 0))

    def test_RecibePensionSinHoras(self):
        '''
        Prueba: Ejecutar la funcion sin las horas cotizadas correctas
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(1950, 'm', 200, 0))

    def test_RecibePensionJusto(self):
        '''
        Prueba: Ejecutar la funcion con los datos justos
        Resultado esperado: True
        '''

        self.assertTrue(self.p.recibe_pension(1963, 'f', 750, 0))
        self.assertTrue(self.p.recibe_pension(1958, 'm', 750, 0))

    def test_RecibePensionPorDebajoMujer(self):
        '''
        Prueba: Ejecutar la funcion con datos por debajo para hombre
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(1963, 'f', 749, 0))
        self.assertFalse(self.p.recibe_pension(1964, 'f', 750, 0))


    def test_RecibePensionPorDebajoHombre(self):
        '''
        Prueba: Ejecutar la funcion con datos por debajo para hombre
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(1958, 'm', 749, 0))
        self.assertFalse(self.p.recibe_pension(1959, 'm', 750, 0))

    def test_RecibePensionPorEncimaMujer(self):
        '''
        Prueba: Ejecutar la funcion con datos por encima para mujer
        Resultado esperado: True
        '''
        self.assertTrue(self.p.recibe_pension(1962, 'f', 750, 0))
        self.assertTrue(self.p.recibe_pension(1963, 'f', 751, 0))

    def test_RecibePensionPorEncimaHombre(self):
        '''
        Prueba: Ejecutar la funcion con datos por encima para hombre
        Resultado esperado: True
        '''

        self.assertTrue(self.p.recibe_pension(1957, 'm', 750, 0))
        self.assertTrue(self.p.recibe_pension(1958, 'm', 751, 0))

    def test_RecibePensionSinDatos(self):
        '''
        Prueba: Ejecutar la funcion sin datos reales
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(0, 'f', 0, 0))
        self.assertFalse(self.p.recibe_pension(0, 'm', 0, 0))

class PruebasInsalubridad(unittest.TestCase):
    '''
    Conjunto de pruebas de la funcion recibe_pension,
    de no frontera, frontera frontera y de esquina para
    su argumento de anhosInsalubridad en particular
    '''

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

    def test_RecibePensionSinInsalubridad(self):
        '''
        Prueba: Ejecutar la funcion con 0 como parametro de insalubridad
        pero con otros datos correctos
        Resultado esperado: True
        '''

        self.assertTrue(self.p.recibe_pension(1960, 'f', 1500, 0))

    def test_RecibePensionConInsalubridad(self):
        '''
        Prueba: Ejecutar la funcion con 10 como parametro de insalubridad
        y otros datos correctos
        Resultado esperado: True
        '''

        self.assertTrue(self.p.recibe_pension(1960, 'm', 1500, 10))

    def test_NoRecibePensionConInsalubridad(self):
        '''
        Prueba: Ejecutar la funcion con 15 como parametro de insalubridad
        pero con otros datos insuficientes
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(2010, 'f', 500, 15))
        self.assertFalse(self.p.recibe_pension(1980, 'm', 1000, 15))

    def test_RecibePensionPorDebajoConInsalubridad(self):
        '''
        Prueba: Ejecutar la funcion con datos por debajo
        pero con el bono de insalubridad
        Resultado esperado: True
        '''

        self.assertTrue(self.p.recibe_pension(1964, 'f', 750, 4))
        self.assertTrue(self.p.recibe_pension(1959, 'm', 750, 4))
        self.assertTrue(self.p.recibe_pension(1965, 'f', 750, 8))
        self.assertTrue(self.p.recibe_pension(1960, 'm', 750, 8))
        self.assertTrue(self.p.recibe_pension(1966, 'f', 750, 12))
        self.assertTrue(self.p.recibe_pension(1961, 'm', 750, 12))
        self.assertTrue(self.p.recibe_pension(1967, 'f', 750, 16))
        self.assertTrue(self.p.recibe_pension(1962, 'm', 750, 16))
        self.assertTrue(self.p.recibe_pension(1968, 'f', 750, 20))
        self.assertTrue(self.p.recibe_pension(1963, 'm', 750, 20))

    def test_RecibePensionPorDebajoConInsalubridadExtra(self):
        '''
        Prueba: Ejecutar la funcion con datos por debajo y con un bono
        que se excede y no genera mas de 5 anos descontados
        Resultado esperado: False
        '''

        self.assertFalse(self.p.recibe_pension(1969, 'f', 750, 30))
        self.assertFalse(self.p.recibe_pension(1964, 'm', 750, 30))

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

    def test_IntroduceLetraIncorrecta(self):
        '''
        Prueba: Ejecuta la funcion con letra desconocida como parametro sexo
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'h', 1500, 0)
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'k', 1500, 10)
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
        Prueba: Ejecuta la funcion con numero negativo como parametro
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1940, 'f', 1500, -1)
        self.assertRaises(ValueError, self.p.recibe_pension, 1940, 'f', 1500, -100)
        self.assertRaises(ValueError, self.p.recibe_pension, 1940, 'f', 1500, -10000000)

class PruebasMaliciaAnhoNacimiento(unittest.TestCase):
    '''
    Conjunto de pruebas de malicia y casos invalidos 
    del argumento anhoNacimiento para la funcion recibe_pension
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

    def test_AnhoNegativo(self):
        '''
        Prueba: Ejecutar la funcion con un numero negativo como argumento de
        anho de nacimiento
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, -1950, 'f', 1500, 10)
        self.assertRaises(ValueError, self.p.recibe_pension, -10000000, 'f', 1500, 10)

class PruebasMaliciaHorasCotizadas(unittest.TestCase):
    '''
    Conjunto de pruebas de malicia y casos invalidos 
    del argumento horasCotizadas para la funcion recibe_pension
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

    def test_HorasNegativas(self):
        '''
        Prueba: Ejecutar la funcion con un numero negativo como argumento de
        horas cotizadas
        Resultado esperado: Excepcion ValueError
        '''
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'f', -780, 10)
        self.assertRaises(ValueError, self.p.recibe_pension, 1950, 'f', -10000000, 10)

if __name__=="__main__":
    unittest.main()