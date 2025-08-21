# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el 
#TP1 Act1

#Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def agregar_al_inicio(self, item):
        nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nodo
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return
        if posicion == self.tamanio:
            self.agregar_al_final(item)
            return

        nodo = Nodo(item)
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nodo.anterior = actual.anterior
        nodo.siguiente = actual
        actual.anterior.siguiente = nodo
        actual.anterior = nodo
        self.tamanio += 1


        
    