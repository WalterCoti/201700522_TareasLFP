import csv
import os

def leercsv():
    cont = 1
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../tarea2/libros.csv")

    with open(path, newline='') as file:
        lista = csv.reader(file)
        print("------CSV------\n")
        print(type(lista))
        print()
        for libro in lista:
            print("Libro No. : " + str(cont))
            print("Nombre : " + libro[0])
            print("Autor : " + libro[1])
            print("Genero : " + libro[2])
            print("Fecha Publicacion : " + libro[3])
            print()
            cont += 1