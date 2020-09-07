def afd(entrada):
    print("Cadena de entrada: " + entrada)
    estado = 0
    for pos in range(len(entrada)):
        if estado ==  0:
            if entrada[pos] == "_":
                estado = 1
            elif entrada[pos].isalpha():
                estado = 2
            else:
                print("Cadena Invalida")
                return
        elif estado == 1:
            if entrada[pos] == "_":
                estado = 1
            elif entrada[pos].isalpha():
                estado = 3
            else:
                print("Cadena Invalida")
                return
        elif estado == 2:
            if entrada[pos].isalpha():
                estado = 2
            elif entrada[pos].isalnum():
                estado = 4
            else:
                print("Cadena Invalida")
                return
        elif estado == 3:
            if entrada[pos].isalpha():
                estado = 3
            elif entrada[pos].isalnum():
                estado = 4
            else:
                print("Cadena Invalida")
                return
        elif estado == 4:
            print("Cadena Invalida")
            break

    print("Cadena Valida")
    print


afd("__servidor1")
afd("3servidor")



