from nodos import *
# from .nodos import Nodo_Fila
# from .nodos import Nodo_Senial

class Cola_Senial:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
                
    def Insertar(self, columnas):
        NuevoNodo = Nodo_Fila(columnas)
        self.Contador += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def ImprimirLista(self):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Auxiliar.ObtenerFila().ImprimirFila()
            Auxiliar = Auxiliar.Siguiente
        print("")

    def CambiarEnFila(self, fila, columna, dato):
        Contador = 0
        Auxiliar = self.Inicio
        if fila == 0 or fila > self.Contador:
            print("No existe la fila!")
            return
        while Auxiliar != None:
            Contador += 1
            if Contador == fila:
                Aux = Auxiliar.ObtenerFila()
                Aux.ModificarDatoenColumna(columna,dato)
                return
            else:
                Auxiliar = Auxiliar.Siguiente

    def BuscarEnFila(self, fila, columna):
        Contador = 0
        Auxiliar = self.Inicio
        if fila == 0 or fila > self.Contador:
            print("No existe la fila!")
            return
        while Auxiliar != None:
            Contador += 1
            if Contador == fila:
                Aux = Auxiliar.ObtenerFila()
                dato = Aux.BuscarDatoenColumna(columna)
                return dato
            else:
                Auxiliar = Auxiliar.Siguiente

class Senial: 
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        contador = 0
        self.Siguiente = None
        Cola_Seniales = Cola_Senial()
        while contador < filas:
            Cola_Seniales.Insertar(columnas)
            contador += 1
        self.senial = Cola_Seniales

    def imprimir_senial(self):
        self.senial.ImprimirLista()

    def CambiodeDato(self, fila, columna, dato):
        self.senial.CambiarEnFila(fila,columna,dato)

    def BuscarDato(self, fila, columna):
        dato = self.senial.BuscarEnFila(fila,columna)
        return dato
    
class Cola_Seniales:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
                
    def Insertar(self, senial):
        NuevoNodo = Nodo_Senial(senial)
        self.Contador += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def ImprimirSeniales(self):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            print("Señal: " + Auxiliar.ObtenerSenial().nombre)
            Auxiliar.ObtenerSenial().imprimir_senial()
            Auxiliar = Auxiliar.Siguiente
        print("\n")