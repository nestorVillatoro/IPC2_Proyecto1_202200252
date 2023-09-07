from nodos import *
# from .nodos import nodofila
# from .nodos import nodosenalinicio

class colaSenal:

    def __init__(self):
        self.inicio = None
        self.final = None
        self.contador = 0
                
    def insertar(self, columnas, nombre):
        nodoNuevo = nodoFila(columnas, nombre)
        self.contador += 1
        if self.inicio == None:
            self.inicio = nodoNuevo
            self.final = nodoNuevo
        else:
            self.final.AsignarSiguiente(nodoNuevo)
            self.final = nodoNuevo

    def CambiarEnfila(self, fila, columna, dato):
        contador = 0
        Auxiliar = self.inicio
        if fila == 0 or fila > self.contador:
            print("No existe la fila!")
            return
        while Auxiliar != None:
            contador += 1
            if contador == fila:
                Aux = Auxiliar.Obtenerfila()
                Aux.modificarDatoenColumna(columna,dato)
                return
            else:
                Auxiliar = Auxiliar.Siguiente

    def buscarEnfila(self, fila, columna):
        contador = 0
        Auxiliar = self.inicio
        if fila == 0 or fila > self.contador:
            print("No existe la fila!")
            return
        while Auxiliar != None:
            contador += 1
            if contador == fila:
                Aux = Auxiliar.Obtenerfila()
                dato = Aux.buscarDatoenColumna(columna)
                return dato
            else:
                Auxiliar = Auxiliar.Siguiente

    def ObtenerDatosfila(self, fila):
        contador = 1 
        Auxiliar = self.inicio
        while Auxiliar != None:
            if contador == fila:
                Aux = Auxiliar.Obtenerfila()
                datos = Aux.Datosfila()
                return datos
            Auxiliar = Auxiliar.Siguiente
            contador += 1

    def obtenerNombrefila(self, fila):
        contador = 1 
        Auxiliar = self.inicio
        while Auxiliar != None:
            if contador == fila:
                nombre = Auxiliar.Obtenerfila().ObtenerNombre()
                return nombre
            Auxiliar = Auxiliar.Siguiente
            contador += 1

    def cambioNombrefila(self, fila, nombre):
        contador = 1 
        Auxiliar = self.inicio
        while Auxiliar != None:
            if contador == fila:
                Aux = Auxiliar.Obtenerfila()
                Aux.cambioNombrefila(nombre)
                Aux.tiempo = "Tiempos "
            Auxiliar = Auxiliar.Siguiente
            contador += 1

    def Eliminarfila(self,fila):
        contador = 1
        Auxiliar = self.inicio
        while Auxiliar != None:
            contador2 = contador + 1 
            if contador2 == fila:
                Auxiliar2 = Auxiliar.Siguiente
                if Auxiliar2.Siguiente != None:
                    Auxiliar.Siguiente = Auxiliar2.Siguiente
                else:
                    Auxiliar.Siguiente = None
            Auxiliar = Auxiliar.Siguiente
            contador += 1
        self.contador -= 1

    def imprimirLista(self):
        Auxiliar = self.inicio
        while Auxiliar != None:
            Auxiliar.Obtenerfila().imprimirfila()
            Auxiliar = Auxiliar.Siguiente
        print("")

class senal: 
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        contador = 0
        self.Siguiente = None
        colasenales = colaSenal()
        while contador < filas:
            colasenales.insertar(columnas, str(contador + 1))
            contador += 1
        self.senal = colasenales

    def imprimir_senal(self):
        self.senal.imprimirLista()

    def buscarDato(self, fila, columna):
        dato = self.senal.buscarEnfila(fila,columna)
        dato2 = dato
        return dato2

    def CambiodeDato(self, fila, columna, dato):
        self.senal.CambiarEnfila(fila,columna,dato)

    def Obtenerfila(self, fila):
        if fila <= self.filas:
            datos = self.senal.ObtenerDatosfila(fila)
            return datos
        else:
            print("No se puede obtener la fila!")
    
    def Eliminarfilas(self, fila):
        self.senal.Eliminarfila(fila)
        self.filas -= 1

    def obtenerNombrefila(self, fila):
        nombre = self.senal.obtenerNombrefila(fila)
        return nombre

    def cambioNombrefila(self, fila, nombre):
        self.senal.cambioNombrefila(fila,nombre)
    
    def Grafica(self, NodoPadre, NoFila):
        a=2
    
class colaSenales:

    def __init__(self):
        self.inicio = None
        self.final = None
        self.contador = 0
                
    def insertar(self, senal):
        nodoNuevo = nodoSenal(senal)
        self.contador += 1
        if self.inicio == None:
            self.inicio = nodoNuevo
            self.final = nodoNuevo
        else:
            self.final.AsignarSiguiente(nodoNuevo)
            self.final = nodoNuevo
    
    def imprimirsenales(self):
        Auxiliar = self.inicio
        while Auxiliar != None:
            print(Auxiliar.Obtenersenal().nombre)
            Auxiliar.Obtenersenal().imprimir_senal()
            Auxiliar = Auxiliar.Siguiente
        print("\n")