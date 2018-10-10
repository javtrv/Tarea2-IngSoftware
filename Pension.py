import time

class Pension:
    anhoActual = int(time.strftime("%Y"))

    def RecibePension(self, anhoUsuario,sexo,horasCotizadas, anhosInsalubres):
        anhoActual = time.strftime("%Y")
        if anhosInsalubres < 4:
            if self.anho_mayor_que_actual(anhoUsuario) == 0:
                if sexo == 'm':
                    if (int(anhoActual) - anhoUsuario) >= 60:
                        if horasCotizadas >= 750:
                            return False
                        else:
                            return True
                    else:
                        return True
                elif sexo == 'f':
                    if (int(anhoActual) - anhoUsuario) >= 55:
                        if horasCotizadas >= 750:
                            return False
                        else:
                            return True
                    else:
                        return True
        else:
            anhosRebajados = anhosInsalubres / 4
            if anhosRebajados > 5:
                anhosRebajados = 5
            if self.anho_mayor_que_actual(anhoUsuario) == 0:
                if sexo == 'm':
                    if (int(anhoActual) - anhoUsuario) >= 60 - anhosRebajados:
                        if horasCotizadas >= 750:
                            return False
                        else:
                            return True
                    else:
                        return True
                elif sexo == 'f':
                    if (int(anhoActual) - anhoUsuario) >= 55 - anhosRebajados:
                        if horasCotizadas >= 750:
                            return False
                        else:
                            return True
                    else:
                        return True

    def anho_mayor_que_actual(self, anho):
        return self.anhoActual < anho

    def calcular_edad(self, anho_nacimiento):
        return self.anhoActual - anho_nacimiento


#p = Pension()
#fechaUsuario = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
#anhoUsuario = fechaUsuario.split("/") #Se crea un vector de la forma [dd,mm,aaaa]
#anhoUsuario = anhoUsuario[2]