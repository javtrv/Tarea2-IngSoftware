import time

class Pension:

    def RecibePension(self, anhoUsuario):
        return 0
    
    def CompararFecha(self, anhoUsuario):
        anhoActual = time.strftime("%Y")
        if anhoActual < anhoUsuario:
            return 1
        else:
            return 0

#p = Pension()
#fechaUsuario = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
#anhoUsuario = fechaUsuario.split("/") #Se crea un vector de la forma [dd,mm,aaaa]
#anhoUsuario = anhoUsuario[2]
#p.ObtenerFecha()