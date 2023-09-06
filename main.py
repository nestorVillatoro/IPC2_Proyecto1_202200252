import xml.etree.ElementTree as ET
from xml.dom import minidom
from listasColas import *
from nodos import *
import os
# from listasColas import colasenales
inicializador = 0
ruta = ""
# C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Entrada-Ejemplo.xml

def cargarArchivo():
    print("------ Cargar archivo ------")
    global ruta
    ruta = input("Ingrese la ruta del archivo: ")   
    input("Presione cualquier tecla para continuar...")
    
def procesarArchivo():
    print("------ Procesar archivo ------")
    print("Mostrando datos originales...")
    archivo = ET.parse("C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Entrada-Ejemplo.xml")
    raiz = archivo.getroot()
    global senales
    senales = colasenales()
    for elementos in raiz:
        nombreSenal = elementos.get("nombre")
        tiempo = int(elementos.get("t"))
        amplitud = int(elementos.get("A"))
        nuevaSenal = senal(nombreSenal, tiempo, amplitud)
        if tiempo > 0 and tiempo <= 3600:
            if amplitud > 0 and amplitud <= 130:
                for datos in elementos.findall("dato"):
                    t = int(datos.get("t"))
                    A = int(datos.get("A"))
                    nuevaSenal.CambiodeDato(t, A, int(datos.text))
                senales.insertar(nuevaSenal)
            else:
                print("La señal " + nombreSenal + " fue rechazada por tener una amplitud de " + str(amplitud))
                input("Presione cualquier tecla para continuar...")
        else:
            print("La señal " + nombreSenal + " fue rechazada por tener un tiempo de " + str(tiempo))
            input("Presione cualquier tecla para continuar...")
        
        
    senales.imprimirsenales()

    print("Convirtiendo a binario...")
    global binarias
    binarias = colasenales()
    aux = senales.inicio
    while aux != None:
        auxi = aux.Obtenersenal()
        senalBi = senal(auxi.nombre + " en binario", int(auxi.filas), int(auxi.columnas))
        No_filas = 1
        while No_filas <= int(auxi.filas):
            No_columnas = 1
            while No_columnas <= int(auxi.columnas):
                dato = auxi.buscarDato(No_filas, No_columnas)
                if dato > 0: 
                    senalBi.CambiodeDato(No_filas, No_columnas, 1)
                No_columnas += 1
            No_filas += 1
        binarias.insertar(senalBi)
        aux = aux.Siguiente
    binarias.imprimirsenales()

    print("Generando datos de salida...")
    global datosFinales
    datosFinales = colasenales()
    auxBinarias = binarias.inicio
    auxSenales = senales.inicio
    while auxBinarias != None:
        auxBinarias2 = auxBinarias.Obtenersenal()
        auxSenales2 = auxSenales.Obtenersenal()
        columnas = int(auxBinarias2.columnas)
        contadorfila = 1
        while contadorfila <= auxBinarias2.filas:
            auxBinarias3 = auxBinarias2.Obtenerfila(contadorfila)
            contadorfila2 = contadorfila + 1
            while contadorfila2 <= auxBinarias2.filas:
                auxBinarias4 = auxBinarias2.Obtenerfila(contadorfila2)
                if auxBinarias3 == auxBinarias4:
                    contadorColumnas = 1
                    while contadorColumnas <= columnas:
                        dato = auxSenales2.buscarDato(contadorfila, contadorColumnas) + auxSenales2.buscarDato(contadorfila2, contadorColumnas)
                        auxSenales2.CambiodeDato(contadorfila, contadorColumnas, dato)
                        contadorColumnas += 1
                    auxSenales2.CambioNombrefila(contadorfila, str(auxSenales2.ObtenerNombrefila(contadorfila)) + ", " + str(auxSenales2.ObtenerNombrefila(contadorfila2)))
                    auxBinarias2.Eliminarfilas(contadorfila2)
                    auxSenales2.Eliminarfilas(contadorfila2)
                else: 
                    contadorfila2 += 1
            contadorfila += 1 
        datosFinales.insertar(auxSenales2)
        auxBinarias = auxBinarias.Siguiente
        auxSenales = auxSenales.Siguiente
    datosFinales.imprimirsenales()

    input("Presione cualquier tecla para continuar...")

def escribirArchivoSalida():
    print("------ Escribir archivo salida ------")
    tree = ET.parse("C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Entrada-Ejemplo.xml")
    root = tree.getroot()
    data = ET.Element("senales")
    aux = datosFinales.inicio
    while aux != None:
        aux2 = aux.Obtenersenal()  
        items = ET.SubElement(data, "senal")
        items.set("name", str(aux2.nombre))
        items.set("t", str(aux2.filas))
        items.set("A", str(aux2.columnas))
        No_filas = 1
        while No_filas <= int(aux2.filas):  
            grupo = ET.SubElement(items, "grupos")
            grupo.set("G", str(No_filas))
            tiempos = ET.SubElement(grupo, "tiempo")
            tiempos.text = str(aux2.ObtenerNombrefila(No_filas))
            datosGrupo = ET.SubElement(grupo, "datosGrupo")
            No_columnas = 1
            while No_columnas <= int(aux2.columnas):
                item = ET.SubElement(datosGrupo, "dato")
                item.set("t", str(No_filas))
                item.set("A", str(No_columnas))
                dato = aux2.buscarDato(No_filas, No_columnas)
                item.text = str(dato)
                No_columnas += 1
            No_filas += 1
        aux = aux.Siguiente    

    myData = minidom.parseString(ET.tostring(data)).toprettyxml(indent="\t")
    myFile = open("Salida-Ejemplo.xml", "w")
    myFile.write(myData)
    myFile.close()

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
    archivo = ET.parse("C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Entrada-Ejemplo.xml")
    raiz = archivo.getroot()

    for elementos in raiz:
        nombreSenal = elementos.get("nombre")
        tiempo = int(elementos.get("t"))
        amplitud = int(elementos.get("A"))
        for datos in elementos.findall("dato"):
            t = int(datos.get("t"))
            A = int(datos.get("A"))

    auxFinales = datosFinales.inicio
    auxBinarias = binarias.inicio
    auxFinales2 = auxFinales.Obtenersenal
    auxBinarias2 = auxBinarias.Obtenersenal
    verificadorSenal = False
    nombreSenal = input("Ingrese el nombre de la señal que desea graficar: ")
    for elementos in raiz:
        if nombreSenal == str(elementos.get("nombre")):
            verificadorSenal = True
            graficaOriginal = '''graph ""
    {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]

        subgraph Prueba1 
        {
            n1 [label="EJEMPLO 1"];
        
            n2 [label="t=5"];
            n3 [label="A=4"];
            n1 -- n2;
            n1 -- n3;
            
            # Fila 1
            n4 [label="2"];
            n1 -- n4;
            n5 [label="3"];
            n1 -- n5;
            n6 [label="0"];
            n1 -- n6;
            n7 [label="4"];
            n1 -- n7;
            
            n8 [label="0"];
            n4 -- n8;
            n9 [label="0"];
            n5 -- n9;
            n10 [label="6"];
            n6 -- n10;
            n11 [label="3"];
            n7 -- n11;
            
            n12 [label="3"];
            n8 -- n12;
            n13 [label="4"];
            n9 -- n13;
            n14 [label="0"];
            n10 -- n14;
            n15 [label="2"];
            n11 -- n15;
            
            n16 [label="1"];
            n12 -- n16;
            n17 [label="0"];
            n13 -- n17;
            n18 [label="1"];
            n14 -- n18;
            n19 [label="5"];
            n15 -- n19;
            
            n20 [label="0"];
            n16 -- n20;
            n21 [label="0"];
            n17 -- n21;
            n22 [label="3"];
            n18 -- n22;
            n23 [label="1"];
            n19 -- n23;
        }
    }
'''
    if verificadorSenal == True:
        archivoOriginal = open("Graficas/Grafica-original.dot", "w")
        archivoOriginal.write(graficaOriginal)
        archivoOriginal.close()
        os.system("cmd /c dot -Tsvg Graficas/Grafica-original.dot > Graficas/Grafica-original.svg")
    else: 
        print("No se encontró la señal!")
    input("Presione cualquier tecla para continuar...")

def inicializarSistema():
    print("------ Inicializar sistema ------")
    global inicializador
    inicializador = 203456
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
            
        case 7:
            salir()
        case _:
            print("")
            print("Opción no válida")
            print("")
            menu()

menu()
if inicializador == 203456:
    menu()
    
