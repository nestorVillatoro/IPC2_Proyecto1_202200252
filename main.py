import xml.etree.ElementTree as ET
from listasColas import *
# from listasColas import Cola_Seniales



ruta = ""
# C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Entrada-Ejemplo.xml


def cargarArchivo():
    print("------ Cargar archivo ------")
    global ruta
    ruta = input("Ingrese la ruta del archivo: ")   
    input("Presione cualquier tecla para continuar...")
    
def procesarArchivo():
    print("------ Procesar archivo ------")
    archivo = ET.parse("C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Entrada-Ejemplo.xml")
    raiz = archivo.getroot()
    senales = Cola_Seniales()
    for elementos in raiz:
        nombreSenal = elementos.get("nombre")
        tiempo = int(elementos.get("t"))
        amplitud = int(elementos.get("A"))
        nuevaSenal = Senial(nombreSenal, tiempo, amplitud)
        if tiempo > 0 and tiempo <= 3600:
            if amplitud > 0 and amplitud <= 130:
                for datos in elementos.findall("dato"):
                    t = int(datos.get("t"))
                    A = int(datos.get("A"))
                    nuevaSenal.CambiodeDato(t, A, int(datos.text))
            else:
                print("La señal " + nombreSenal + " fue rechazada por tener una amplitud de " + str(amplitud))
        else:
            print("La señal " + nombreSenal + " fue rechazada por tener un tiempo de " + str(tiempo))
        senales.Insertar(nuevaSenal)
        
    senales.ImprimirSeniales()

    print("Convirtiendo a binario...")

    binarias = Cola_Seniales()
    finales = Cola_Seniales()
    aux = senales.Inicio
    while aux != None:
        auxi = aux.ObtenerSenial()
        senalBi = Senial(auxi.nombre + " en binario", int(auxi.filas), int(auxi.columnas))
        No_filas = 1
        while No_filas <= int(auxi.filas):
            No_columnas = 1
            while No_columnas <= int(auxi.columnas):
                dato = auxi.BuscarDato(No_filas, No_columnas)
                if dato > 0: 
                    senalBi.CambiodeDato(No_filas, No_columnas, 1)
                No_columnas += 1
            No_filas += 1
        binarias.Insertar(senalBi)
        aux = aux.Siguiente
    binarias.ImprimirSeniales()

    input("Presione cualquier tecla para continuar...")

def escribirArchivoSalida():
    print("------ Escribir archivo salida ------")
    input("Presione cualquier tecla para continuar...")

def MostrarDatosEstud():
    print("------ Mostrar datos del estudiante ------")
    print("Néstor Enrique Villatoro Avendaño")
    print("202200252")
    print("Introduccion a la programación y computación 2 sección C")
    print("Ingeniería en ciencias y sistemas")
    print("4to semestre")
    input("Presione cualquier tecla para continuar...")

def generarGraficas():
    print("------ Generar gráfica ------")
    input("Presione cualquier tecla para continuar...")

def inicializarSistema():
    print("------ Inicializar sistema ------")
    input("Presione cualquier tecla para continuar...")

def salir():
    print("Saliendo del programa...")

def menu():
    print("--------------------MENU--------------------")
    print("| 1. Cargar archivo                        |")
    print("| 2. Procesar archivo                      |")
    print("| 3. Escribir archivo salida               |")
    print("| 4. Mostrar datos del estudiante          |")
    print("| 5. Generar gráfica                       |")
    print("| 6. Inicializar sistema                   |")
    print("| 7. Salida                                |")
    print("--------------------------------------------")
    opc = int(input("Ingrese una opción: "))
    match opc:
        case 1:
            cargarArchivo()
            menu()
        case 2:
            procesarArchivo()
            menu()
        case 3:
            escribirArchivoSalida()
            menu()
        case 4:
            MostrarDatosEstud()
            menu()
        case 5:
            generarGraficas()
            menu()
        case 6:
            inicializarSistema()
            menu()
        case 7:
            salir()
        case _:
            print("")
            print("Opción no válida")
            print("")
            menu()

menu()