from listasColas import *

class Fila:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    def Insertar(self):
        NuevoNodo = Nodo_Dato()
        self.Contador += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def ImprimirFila(self):
        Auxiliar = self.Inicio
        fila = ""
        while Auxiliar != None:
            fila = fila + " | " + (str(Auxiliar.ObtenerDato()))
            Auxiliar = Auxiliar.Siguiente
        print(fila + "|")

    def ModificarDatoenColumna(self, columna, dato):
        Contador = 0
        Auxiliar = self.Inicio
        if columna == 0 or columna > self.Contador:
            print("No existe la columna!")
            return
        else:
            while Auxiliar != None:
                Contador += 1
                if Contador == columna:
                    Auxiliar.CambiarDato(dato)
                else:
                    Auxiliar = Auxiliar.Siguiente

    def BuscarDatoenColumna(self, columna):
        Contador = 0
        Auxiliar = self.Inicio
        if columna == 0 or columna > self.Contador:
            print("No existe la columna!")
            return
        else:
            while Auxiliar != None:
                Contador += 1
                if Contador == columna:
                    dato = Auxiliar.ObtenerDato()
                    return dato
                else:
                    Auxiliar = Auxiliar.Siguiente

class Nodo_Dato:
    def __init__(self):
        self.dato = 0
        self.Siguiente = None

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random

    def ObtenerDato(self):
        return self.dato
    
    def CambiarDato(self, Nuevo_Dato):
        self.dato = Nuevo_Dato

class Nodo_Fila:
    def __init__(self, columnas):
        contador = 0
        self.Siguiente = None
        Filas = Fila()
        while contador < columnas:
            Filas.Insertar()
            contador += 1
        self.fila = Filas

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random

    def ObtenerFila(self):
        return self.fila

class Nodo_Senial:
    def __init__(self, senial):
        self.senial  = senial
        self.Siguiente = None

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random

    def ObtenerSenial(self):
        return self.senial
    
