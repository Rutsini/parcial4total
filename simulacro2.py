import funciones as func


def principal():
    op = "-1"
    v = []
    nom = "Archivo.dat"

    print("Opcion 1 - ")
    print("Opcion 2 - ")
    print("Opcion 3 - ")
    print("Opcion 4 - ")
    print("Opcion 5 - ")
    print("Opcion 6 - ")
    print("Opcion 9 - SALIR.")

    while op != "9":
        op = input("Ingrese la opcion que desee: ")

        if op == "1":
            n = int(input("Ingrese la cantidad de datos que desee: "))
            if n > 0:
                func.cargar_vector(v, n)
        elif op == "2":
            func.mostrar_vector(v)
        elif op == "3":
            identificacion_ingresada = int(input("Ingrese la identificacion que desea filtrar: "))
            func.buscar(v, identificacion_ingresada)
        elif op == "4":
            func.count(v)
        elif op == "5":
            cliente_ingresada = int(input("Ingrese el tipo de cliente que desea filtrar: "))

            func.crear_archivo(v, nom, cliente_ingresada)
            func.mostrar_archivo(nom)
        elif op == "6":
            producto_ingresado = int(input("Ingrese el tipo de producto que desea filtrar: "))

            func.buscar_op6(v, producto_ingresado)
        elif op == "9":
            print("SALIO DEL PROGRAMA.")


if __name__ == "__main__":
    principal()