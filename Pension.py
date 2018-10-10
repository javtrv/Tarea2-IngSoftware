import time # Importamos este modulo para el manejo del tiempo

class Pension:
    '''
    Modulo de Python 3 que contiene funciones para determinar si un
    venezolano, dado su anho de nacimiento, sexo, horas cotizadas en el IVSS
    y anhos insalubres, debe recibir o no la pension de este organismo.
    '''

    # Al instanciar el modulo, obtenemos el anho actual
    anhoActual = int(time.strftime("%Y"))

    def recibe_pension(self, anhoUsuario, sexo, horasCotizadas, anhosInsalubres):
        '''
        Utilizando el resto de funciones de este modulo, determina
        si un venezolano deber percibir ingresos por parte de la pension
        del IVSS o no en el anho en curso.
        '''

        # Devolvemos False si se introduce un anho incorrecto
        if self.anho_mayor_que_actual(anhoUsuario):
            return False

        # Devolvemos False si se introduce un sexo desconocidou
        if sexo not in ['m', 'M', 'f', 'F']:
            return False

        # Si tiene menos de 4 anhos insalubres, lo ignoramos
        if anhosInsalubres < 4:

            # Caso para los hombres
            if sexo in ['m', 'M']:
                if self.calcular_edad(anhoUsuario) >= 60:
                    return horasCotizadas >= 750

            # Caso para las mujeres
            elif sexo in ['f', 'F']:
                if self.calcular_edad(anhoUsuario) >= 55:
                    return horasCotizadas >= 750

        # Si tiene mas de 4 anhos insalubres, los contamos en grupos de 4
        else:
            anhosRebajados = anhosInsalubres / 4

            # Solo vamos a rebajar hasta 5 anhos
            if anhosRebajados > 5:
                anhosRebajados = 5

            # Caso para los hombres
            if sexo in ['m', 'M']:
                if self.calcular_edad(anhoUsuario) >= (60 - anhosRebajados):
                    return horasCotizadas >= 750

            # Caso para las mujeres
            elif sexo in ['f', 'F']:
                if self.calcular_edad(anhoUsuario) >= (55 - anhosRebajados):
                    return horasCotizadas >= 750

        # En cualquier otro caso, retornamos False
        return False

    def anho_mayor_que_actual(self, anho):
        '''
        Determina si un anho introducido es mayor
        al anho actual
        '''

        return self.anhoActual < anho

    def calcular_edad(self, anho_nacimiento):
        '''
        Determina la edad de una persona a partir de su anho
        de nacimiento con respecto al anho actual.
        '''

        if anho_nacimiento > self.anhoActual or anho_nacimiento < 0:
            return 0

        return self.anhoActual - anho_nacimiento

def main():
    '''
    Procedimiento principal que solicita al usuario por medio
    de la consola sus datos y le manifiesta si este anho percibe
    o no percibe ingresos por la pension del IVSS
    '''

    # Instanciamos el modulo de Pension
    p = Pension()

    # Solicitamos por la entrada interactiva sus datos
    fechaUsuario = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
    sexo = input("Ingrese su sexo (m para masculino, f para femenino): ")
    horasCotizadas = int(input("Ingrese la cantidad de horas cotizadas: "))
    anhosInsalubres = int(input("Ingrese la cantidad de anhos insalubres: "))
    
    # Tomamos el anho de la fecha de nacimiento del usuario
    fechaUsuario = time.strptime(fechaUsuario, '%d/%m/%Y')
    anhoUsuario = int(fechaUsuario.tm_year)

    # Determinamos si el usuario recibe pension
    recibePension = p.recibe_pension(
        anhoUsuario, 
        sexo, 
        horasCotizadas, 
        anhosInsalubres
        )

    # Imprimimos un mensaje acorde a lo que se determino y retornamos
    if recibePension:
        print("Usted debe recibir la pension del IVSS este anho.")
    else:
        print("Usted NO recibe pension del IVSS este anho.")

    return

if __name__ == '__main__':
    main()