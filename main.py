import xml.etree.ElementTree as ET
from xml.dom import minidom
from listasColas import *
from nodos import *
import os
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
    archivo = ET.parse(ruta)
    raiz = archivo.getroot()
    global senales
    senales = colaSenales()
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
    binarias = colaSenales()
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
    datosFinales = colaSenales()
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
                    auxSenales2.cambioNombrefila(contadorfila, str(auxSenales2.obtenerNombrefila(contadorfila)) + ", " + str(auxSenales2.obtenerNombrefila(contadorfila2)))
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
    tree = ET.parse(ruta)
    root = tree.getroot()
    data = ET.Element("senales")
    aux = datosFinales.inicio
    while aux != None:
        aux2 = aux.Obtenersenal()  
        items = ET.SubElement(data, "senal")
        items.set("nombre", str(aux2.nombre))
        items.set("t", str(aux2.filas))
        items.set("A", str(aux2.columnas))
        No_filas = 1
        while No_filas <= int(aux2.filas):  
            grupo = ET.SubElement(items, "grupos")
            grupo.set("G", str(No_filas))
            tiempos = ET.SubElement(grupo, "tiempo")
            tiempos.text = str(aux2.obtenerNombrefila(No_filas))
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
    print("Se generó el archivo de salida")

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
    archivo = ET.parse(ruta)
    raiz = archivo.getroot()
    verificadorSenal = False
    archivoOriginal = open("Graficas/Grafica-original.dot", "w")
    nombreSenal = input("Ingrese el nombre de la señal que desea graficar: ")
    for elementos in raiz:
        if nombreSenal == str(elementos.get("nombre")):
            tiempo = str(elementos.get("t"))
            amplitud = str(elementos.get("A"))
            verificadorSenal = True
            graficaOriginal = '''graph ""
    {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]

        subgraph Prueba1
        {
            n1 [label="'''+ nombreSenal +'''"];
            n2 [label="t='''+ tiempo +'''"];
            n3 [label="A='''+ amplitud +'''"];
            n1 -- n2;
            n1 -- n3;
            '''
            archivoOriginal.write(graficaOriginal)
            
            contador = 4
            amp = 1
            contadordup = contador
            for datos in elementos.findall("dato"):
                if amp <= int(amplitud):
                    dato = str(datos.text)
                    graficaOriginal2 = '''
            n'''+ str(contador) +''' [label="'''+ dato + '''"];
            n1 -- n'''+ str(contador) +''';'''
                    contador += 1
                    archivoOriginal.write(graficaOriginal2)
                    amp += 1
                else: 
                    dato = str(datos.text)
                    graficaOriginal2 = '''
            n'''+ str(contador) +''' [label="'''+ dato + '''"];
            n'''+ str(contadordup) + ''' -- n'''+ str(contador) +''';'''
                    contador += 1
                    archivoOriginal.write(graficaOriginal2)
                    contadordup += 1
                    
            archivoOriginal.write('''
                        }
                        }''')
    if verificadorSenal == True:
        archivoOriginal.close()
        os.system("cmd /c dot -Tsvg Graficas/Grafica-original.dot > Graficas/Grafica-original.svg")
        print("Se generó la gráfica original exitosamente!")
    else:
        print("No se encontró la señal original!")
# --------------------------------------------------------------------------------------------------------------------------
    archivo = ET.parse("C:/Users/nyavi/Desktop/cuarto semestre/ipc 2/lab/IPC2_Proyecto1_202200252/Salida-Ejemplo.xml")
    raiz = archivo.getroot()
    verificadorSenal = False
    archivoReducido = open("Graficas/Grafica-reducida.dot", "w")
    for elementos in raiz:
        if nombreSenal == str(elementos.get("nombre")):
            amplitud = str(elementos.get("A"))
            tiempo = int(elementos.get("t"))
            verificadorSenal = True
            graficaReducida = '''graph ""
    {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]

        subgraph Prueba1
        {
            n1 [label="'''+ nombreSenal +'''"];
            n2 [label="A='''+ amplitud +'''"];
            n1 -- n2;
            '''
            archivoReducido.write(graficaReducida)
            contador = 3
            tiemp = 1
            for grupos in elementos.findall("grupos"):
                for tiempos in grupos.findall("tiempo"):
                    if tiemp == 1:
                        Gr = str(grupos.get("G"))
                        time = tiempos.text
                        graficaReducida2 = '''
                n'''+ str(contador) +''' [label="G='''+ Gr + " t = (" + time + ''')"];
                n'''+ str(tiemp) + ''' -- n'''+ str(contador) +''';'''
                        archivoReducido.write(graficaReducida2)
                        contador += 1
                        tiemp += 1
                    else:
                        contador2 = contador-1
                        Gr = str(grupos.get("G"))
                        time = tiempos.text
                        graficaReducida2 = '''
                n'''+ str(contador) +''' [label="G='''+ Gr + " t = (" + time + ''')"];
                n'''+ str(contador2) + ''' -- n'''+ str(contador) +''';'''
                        archivoReducido.write(graficaReducida2)
                        contador += 1
                        tiemp += 1 
            amp = 1
            contador3 = 7
            contador4 = contador3
            for grupos in elementos.findall("grupos"):            
                for datosGrupos in grupos.findall("datosGrupo"):
                    for datosReducidos in datosGrupos.findall("dato"):
                        if amp <= int(amplitud):
                            datoR = str(datosReducidos.text)
                            graficaReducida3 = '''
                    n'''+ str(contador3) +''' [label="'''+ datoR + '''"];
                    n1 -- n'''+ str(contador3) +''';'''
                            contador3 += 1
                            archivoReducido.write(graficaReducida3)
                            amp += 1
                        else: 
                            datoR = str(datosReducidos.text)
                            graficaReducida3 = '''
                    n'''+ str(contador3) +''' [label="'''+ datoR + '''"];
                    n'''+ str(contador4) + ''' -- n'''+ str(contador3) +''';'''
                            contador3 += 1
                            archivoReducido.write(graficaReducida3)
                            contador4 += 1       





            archivoReducido.write('''
                        }
                        }''')
    if verificadorSenal == True:
        archivoReducido.close()
        os.system("cmd /c dot -Tsvg Graficas/Grafica-reducida.dot > Graficas/Grafica-reducida.svg")
        print("Se generó la gráfica reducida exitosamente!")
    else:
        print("No se encontró la señal reducida!")
    input("Presione cualquier tecla para continuar...")

def inicializarSistema(numero):
    print("------ Inicializar sistema ------")
    global inicializador
    inicializador = 203456
    input("Presione cualquier tecla para continuar...")


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
            print(":c")
            menu()
            
        case 7:
            print("Saliendo del programa...")

        case _:
            print("")
            print("Opción no válida")
            print("")
            menu()

menu()

    
