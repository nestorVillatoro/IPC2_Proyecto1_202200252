from listasColas import *

class fila:

    def __init__(self, nombre):
        self.nombre = nombre
        self.tiempo = "Tiempo "
        self.inicio = None
        self.final = None
        self.contador = 0

    def insertar(self):
        nodoNuevo = nodoDato()
        self.contador += 1
        if self.inicio == None:
            self.inicio = nodoNuevo
            self.final = nodoNuevo
        else:
            self.final.AsignarSiguiente(nodoNuevo)
            self.final = nodoNuevo
    
    def imprimirfila(self):
        Auxiliar = self.inicio
        fila = ""
        while Auxiliar != None:
            fila = fila + " | " + (str(Auxiliar.ObtenerDato()))
            Auxiliar = Auxiliar.Siguiente
        print(fila + " | ")

    def buscarDatoenColumna(self, columna):
        contador = 0
        Auxiliar = self.inicio
        if columna == 0 or columna > self.contador:
            print("No existe la columna!")
            return
        else:
            while Auxiliar != None:
                contador += 1
                if contador == columna:
                    dato = Auxiliar.ObtenerDato()
                    return dato
                else:
                    Auxiliar = Auxiliar.Siguiente

    def modificarDatoenColumna(self, columna, dato):
        contador = 0
        Auxiliar = self.inicio
        if columna == 0 or columna > self.contador:
            print("No existe la columna!")
            return
        else:
            while Auxiliar != None:
                contador += 1
                if contador == columna:
                    Auxiliar.CambiarDato(dato)
                else:
                    Auxiliar = Auxiliar.Siguiente

    def Datosfila(self):
        Auxiliar = self.inicio
        datosfila = ""
        while Auxiliar != None:
            datoColumna = str(Auxiliar.ObtenerDato())
            datosfila = datosfila + datoColumna + " "
            Auxiliar = Auxiliar.Siguiente
        return datosfila
    
    def cambioNombrefila(self, nombre):
        self.nombre = nombre

    def ObtenerNombre(self):
        nombre = self.nombre
        return nombre

class nodoDato:
    def __init__(self):
        self.dato = 0
        self.Siguiente = None

    def AsignarSiguiente(self, nodorandom):
        self.Siguiente = nodorandom

    def ObtenerDato(self):
        dato = self.dato
        return dato
    
    def CambiarDato(self, Nuevo_Dato):
        self.dato = Nuevo_Dato

class nodoFila:
    def __init__(self, columnas, nombre):
        contador = 0
        self.Siguiente = None
        filas = fila(nombre)
        while contador < columnas:
            filas.insertar()
            contador += 1
        self.fila = filas

    def AsignarSiguiente(self, nodorandom):
        self.Siguiente = nodorandom

    def Obtenerfila(self):
        return self.fila
    
    def DevolverSiguiente(self):
        return self.Siguiente

class nodoSenal:
    def __init__(self, senal):
        self.senal  = senal
        self.Siguiente = None

    def AsignarSiguiente(self, nodorandom):
        self.Siguiente = nodorandom

    def Obtenersenal(self):
        return self.senal
    
