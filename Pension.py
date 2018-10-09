import time

class Pension:

    def RecibePension(self, anhoUsuario,sexo,horasCotizadas, anhosInsalubres):
        anhoActual = time.strftime("%Y")
        if anhosInsalubres < 4:
            if self.CompararFecha(anhoUsuario) == 0:
                if sexo == 'm':
                    if (int(anhoActual) - anhoUsuario) >= 60:
                        if horasCotizadas >= 750:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
                elif sexo == 'f':
                    if (int(anhoActual) - anhoUsuario) >= 55:
                        if horasCotizadas >= 750:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
        else:
            anhosRebajados = anhosInsalubres / 4
            if anhosRebajados > 5:
                anhosRebajados = 5
            if self.CompararFecha(anhoUsuario) == 0:
                if sexo == 'm':
                    if (int(anhoActual) - anhoUsuario) >= 60 - anhosRebajados:
                        if horasCotizadas >= 750:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
                elif sexo == 'f':
                    if (int(anhoActual) - anhoUsuario) >= 55 - anhosRebajados:
                        if horasCotizadas >= 750:
                            return 0
                        else:
                            return 1
                    else:
                        return 1

    def CompararFecha(self, anhoUsuario):
        anhoActual = time.strftime("%Y")
        if int(anhoActual) < anhoUsuario:
            return 1
        else:
            return 0

#p = Pension()
#fechaUsuario = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
#anhoUsuario = fechaUsuario.split("/") #Se crea un vector de la forma [dd,mm,aaaa]
#anhoUsuario = anhoUsuario[2]