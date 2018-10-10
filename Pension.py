import time

class Pension:
    anhoActual = int(time.strftime("%Y"))

    def RecibePension(self, anhoUsuario, sexo, horasCotizadas, anhosInsalubres):
        if self.anho_mayor_que_actual(anhoUsuario):
            return False

        if anhosInsalubres < 4:
            if sexo == 'm':
                if self.calcular_edad(anhoUsuario) >= 60:
                    if horasCotizadas >= 750:
                        return True
                    else:
                        return False
                else:
                    return False
            elif sexo == 'f':
                if self.calcular_edad(anhoUsuario) >= 55:
                    if horasCotizadas >= 750:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            anhosRebajados = anhosInsalubres / 4
            if anhosRebajados > 5:
                anhosRebajados = 5
            if sexo == 'm':
                if self.calcular_edad(anhoUsuario) >= (60 - anhosRebajados):
                    if horasCotizadas >= 750:
                        return True
                    else:
                        return False
                else:
                    return False
            elif sexo == 'f':
                if self.calcular_edad(anhoUsuario) >= (55 - anhosRebajados):
                    if horasCotizadas >= 750:
                        return True
                    else:
                        return False
                else:
                    return False

    def anho_mayor_que_actual(self, anho):
        return self.anhoActual < anho

    def calcular_edad(self, anho_nacimiento):
        if anho_nacimiento > self.anhoActual:
            return 0

        return self.anhoActual - anho_nacimiento


#p = Pension()
#fechaUsuario = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
#anhoUsuario = fechaUsuario.split("/") #Se crea un vector de la forma [dd,mm,aaaa]
#anhoUsuario = anhoUsuario[2]