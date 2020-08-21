from xml.dom import minidom
import os

def leerxml():
    cont = 1
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../tarea2/libros.xml")
    docxml = minidom.parse(path)
    lista = docxml.getElementsByTagName("libro")
    os.system("cls")
    print("------XML------\n")
    print(type(lista))
    print()
    
    for libro in lista: 
        nombre = libro.getElementsByTagName("nombre")[0]
        autor = libro.getElementsByTagName("autor")[0]
        genero = libro.getElementsByTagName("genero")[0]
        anio = libro.getElementsByTagName("año")[0]

        print("Libro No. : " + str(cont))
        print("Nombre : "+ nombre.firstChild.data)
        print("Autor : "+ autor.firstChild.data)
        print("Genero : " + genero.firstChild.data)
        print("Año Publicacion :" + anio.firstChild.data)
        print()
        cont+=1