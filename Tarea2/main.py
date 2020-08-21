import loadJson
import loadXml
import loadCsv
import os.path


def menuprin():
    salir = False
    while not salir:
        print("-----------Menu Principal---------")
        print("-    1. Cargar datos .json       -")
        print("-    2. Cargar datos .xml        -")
        print("-    3. Cargar datps .csv        -")
        print("-    4. salir                    -")
        print("----------------------------------\n")
        
        opcMenu = int(input("Seleccionar una opcion : "))

        if opcMenu == 1:
            os.system("cls")
            loadJson.leerjson()
        elif opcMenu == 2:
            os.system("cls")
            loadXml.leerxml()
        elif opcMenu == 3:
            os.system("cls")
            loadCsv.leercsv()
        elif opcMenu == 4:
            salir = True
            os.system("cls")
        else:
            os.system("cls")
            print("####### Introducir un número entre 1 y 4 #######\n")
            

menuprin()
