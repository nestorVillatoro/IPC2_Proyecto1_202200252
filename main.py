def cargarArchivo():
    print("------ Cargar archivo ------")
    input("Ingrese la ruta del archivo: ")

def procesarArchivo():
    print("------ Procesar archivo ------")

def escribirArchivoSalida():
    print("------ Escribir archivo salida ------")

def MostrarDatosEstud():
    print("------ Mostrar datos del estudiante ------")
    print("Néstor Enrique Villatoro Avendaño")
    print("202200252")
    print("Introduccion a la programación y computación 2 sección C")
    print("Ingeniería en ciencias y sistemas")
    print("4to semestre")

def generarGraficas():
    print("------ Generar gráfica ------")

def inicializarSistema():
    print("------ Inicializar sistema ------")

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