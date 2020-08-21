import json
import os

def leerjson():
    cont = 1
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../tarea2/libros.json")
    with open(path) as mislibros:
        lista = json.loads(mislibros.read())
        print("------JSON------\n")
        print(type(lista))
        print()
        for libro in lista:
            print("Libro No.: " + str(cont))
            print("Titulo de libro : " + libro.get("nombre"))
            print("Autor : "+ libro.get("autor"))
            print("Genero : "+ libro.get("genero"))
            print("Fecha de Publicacion: " + str(libro.get("fecha")))
            print("")
            
            cont += 1