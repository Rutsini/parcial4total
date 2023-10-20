import os
import random
import pickle


class Casos():
    def __init__(self, identificacion, descripcion, monto_caso, tipo_asunto, numero_tribunal):
        self.identificacion = identificacion
        self.descripcion = descripcion
        self.monto_caso = monto_caso
        self.tipo_asunto = tipo_asunto
        self.numero_tribunal = numero_tribunal

    def __str__(self):
        return "Identificacion: " + str(self.identificacion) + " " + "descripcion: " + str(
            self.descripcion) + " " + "monto_caso: " + str(self.monto_caso) + " " + "tipo_asunto: " + str(
            self.tipo_asunto) + " " + "numero_tribunal: " + str(self.numero_tribunal)


def descripciones():
    descrp = ("Asunto A", "Asunto B", "Asunto C", "Asunto D", "Asunto E", "Asunto F")
    return random.choice(descrp)


def cargar_vector(v, n):
    for i in range(n):
        identificacion = random.randint(10000, 999999)
        descripcion = descripciones() + str(i)
        monto_caso = random.randint(1000, 50000)
        tipo_asunto = random.randint(0, 19)
        numero_tribunal = random.randint(1, 10)

        dato = Casos(identificacion, descripcion, monto_caso, tipo_asunto, numero_tribunal)
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

def mostrar_vector2(v, t):
    for i in v:
        if i.numero_tribunal != t:
            print(i)


def buscar(v, des):
    band = False
    for i in v:
        if i.descripcion == des:
            print(i)
            band = True
            break

    if not band:
        print("No existe al descripcion buscada.")


def crear_archivo(v, nom, x):
    archivo_b = open(nom, "wb")

    for i in v:
        if i.tipo_asunto == 3 or i.tipo_asunto == 4:
            if i.monto_caso < x:
                dato = i
                pickle.dump(dato , archivo_b)

    archivo_b.close()

def mostrar_archivo(nom):
    if os.path.exists(nom):
        cont = 0
        tam = os.path.getsize(nom)
        archivo_b = open(nom, "rb")

        while tam > archivo_b.tell():
            cont += 1
            dato = pickle.load(archivo_b)
            print(dato)
        print("La cantidad de datos mostrados es de:", cont)
    else:
        print("El archivo aun no existe.")
