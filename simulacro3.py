import funciones3 as func

def principal():
    op = "-1"
    v = []
    nom = "Archivo.dat"

    print("opcion 1 - ")
    print("opcion 2 - ")
    print("opcion 3 - ")
    print("opcion 4 - ")
    print("opcion 5 - ")
    print("opcion 9 - SALIO.")

    while op != "9":
        op = input("Ingrese la opcion que desee: ")
        if op == "1":
            n = int(input("Ingrese la cantidad de datos que desee cargar: "))
            if n > 0:
                func.cargar_vector(v, n)
            else:
                print("Ingrese un valor mayor a 0.")
        elif op == "2":
            func.mostrar_vector(v)

            tipo_tribunal_ingersado = int(input("Ingrese el tipo de tribunal que desee filtrar: "))

            func.mostrar_vector2(v, tipo_tribunal_ingersado)
        elif op == "3":
            descripcion_ingresada = input("Ingrese la descripcion que desee filtrar: ")

            func.buscar(v, descripcion_ingresada)
        elif op == "4":
            monto_ingresado = int(input("Ingrese un monto de caso que desee filtrar: "))
            func.crear_archivo(v, nom, monto_ingresado)
        elif op == "5":
            func.mostrar_archivo(nom)
        elif op == "9":
            print("SALIO DEL PROGRAMA.")


if __name__ == "__main__":
    principal()