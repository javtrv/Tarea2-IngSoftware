import time

class Pension:
    anhoActual = int(time.strftime("%Y"))

    def RecibePension(self, anhoUsuario, sexo, horasCotizadas, anhosInsalubres):
        if self.anho_mayor_que_actual(anhoUsuario):
            return False
        if sexo not in ['m', 'M', 'f', 'F']:
            return False

        if anhosInsalubres < 4:
            if sexo in ['m', 'M']:
                if self.calcular_edad(anhoUsuario) >= 60:
                    return horasCotizadas >= 750
            elif sexo in ['f', 'F']:
                if self.calcular_edad(anhoUsuario) >= 55:
                    return horasCotizadas >= 750
        else:
            anhosRebajados = anhosInsalubres / 4
            if anhosRebajados > 5:
                anhosRebajados = 5
            if sexo in ['m', 'M']:
                if self.calcular_edad(anhoUsuario) >= (60 - anhosRebajados):
                    return horasCotizadas >= 750
            elif sexo in ['f', 'F']:
                if self.calcular_edad(anhoUsuario) >= (55 - anhosRebajados):
                    return horasCotizadas >= 750

        return False

    def anho_mayor_que_actual(self, anho):
        return self.anhoActual < anho

    def calcular_edad(self, anho_nacimiento):
        if anho_nacimiento > self.anhoActual:
            return 0

        return self.anhoActual - anho_nacimiento

def main():
    p = Pension()

    fechaUsuario = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
    sexo = input("Ingrese su sexo (m para masculino, f para femenino): ")
    horasCotizadas = int(input("Ingrese la cantidad de horas cotizadas: "))
    anhosInsalubres = int(input("Ingrese la cantidad de anhos insalubres: "))
    
    fechaUsuario = time.strptime(fechaUsuario, '%d/%m/%Y')
    anhoUsuario = int(fechaUsuario.tm_year)

    recibePension = p.RecibePension(
        anhoUsuario, 
        sexo, 
        horasCotizadas, 
        anhosInsalubres
        )

    if recibePension:
        print("Usted debe recibir la pension del IVSS.")
    else:
        print("Usted NO recibe pension del IVSS.")

if __name__ == '__main__':
    main()