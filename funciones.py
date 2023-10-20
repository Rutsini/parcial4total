import pickle
import random
import os


class Facturaciones():
    def __init__(self, identificacion, nombre_titular, tipo_cliente, tipo_producto, monto_facturacion):
        self.identificacion = identificacion
        self.nombre_titular = nombre_titular
        self.tipo_cliente = tipo_cliente
        self.tipo_producto = tipo_producto
        self.monto_facturacion = monto_facturacion

    def __str__(self):
        return "identificacion: " + str(self.identificacion) + " " + "nombre_titular: " + "" + str(
            self.nombre_titular) + " " + "tipo_cliente: " + str(
            self.tipo_cliente) + " " + "tipo_producto: " + str(self.tipo_producto) + " " + "monto_facturacion: " + str(
            self.monto_facturacion)


def nombres():
    nombre = ("Facu", "Chini", "Lucas", "Mar", "Manu")
    return random.choice(nombre)


def cargar_vector(v, n):
    for i in range(n):
        identificacion = random.randint(10000, 999999)
        nombre_titular = nombres()
        tipo_cliente = random.randint(0, 8)
        tipo_producto = random.randint(0, 15)
        monto_facturacion = random.randint(500, 50000)

        dato = Facturaciones(identificacion, nombre_titular, tipo_cliente, tipo_producto, monto_facturacion)
        add_in_order(v, dato)


def add_in_order(v, dato):
    n = len(v)
    pos = n

    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].identificacion == dato.identificacion:
            pos = c
            break
        if v[c].identificacion > dato.identificacion:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [dato]


def mostrar_vector(v):
    for i in v:
        print(i)


def buscar(v, x):
    band = False
    n = len(v)
    pos = n

    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].identificacion == x:
            pos = c
            band = True
            break
        if v[c].identificacion > x:
            der = c - 1
        else:
            izq = c + 1

    if band:
        print(v[pos])
    else:
        print("La identificacion que busca no se encontró.")


def count(v):
    cc, cf = 9, 16

    matrix = [[0] * cc for i in range(cf)]

    for i in v:
        c = i.tipo_cliente
        f = i.tipo_producto
        matrix[f][c] += 1

    for fil in range(cf):
        for col in range(cc):
            if matrix[fil][col] != 0:
                print("Tipo de cliente:", col, "Tipo de producto:", fil, "Cantidad de clientes:", matrix[fil][col])


def crear_archivo(v, nom, x):
    archivo_b = open(nom, "wb")

    for i in v:
        if i.tipo_cliente == x:
            if i.tipo_producto != 2 and i.tipo_producto != 3 and i.tipo_producto != 4:
                dato = i

                pickle.dump(dato, archivo_b)

    archivo_b.close()


def mostrar_archivo(nom):
    if os.path.exists(nom):
        acum = 0
        tam = os.path.getsize(nom)
        archivo_b = open(nom, "rb")

        while tam > archivo_b.tell():
            dato = pickle.load(archivo_b)
            acum += dato.monto_facturacion

            print(dato)
        print("El total facturado de todos los datos de el archivo es de:", acum, "$.")
    else:
        print("El archivo aun no existe.")


def buscar_op6(v, x):
    acum = 0
    acum1 = 0

    for i in v:
        acum += i.monto_facturacion

        if i.tipo_producto == x:
            acum1 += i.monto_facturacion
    print("El total facturado fue de:", acum1)
    print("El total facturado de todo el arreglo es:", acum)

    return porcentaje(acum, acum1)


def porcentaje(v1, v2):
    porcen = (v2 * 100) / v1
    print("El procentaje es:", porcen, "%.")
