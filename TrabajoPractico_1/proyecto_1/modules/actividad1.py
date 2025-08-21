# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el 
#TP1 Actividad 1

# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# Clase Lista doblemente enlazada
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0 #Devuelve True si la lista está vacía

    def agregar_al_inicio(self, item):
        nodo = Nodo(item)            #Agrega un nuevo ítem al inicio de la lista
        if self.esta_vacia():
            self.cabeza = self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nodo = Nodo(item)             #Agrega un nuevo ítem al final de la lista
        if self.esta_vacia():
            self.cabeza = self.cola = nodo
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:              #Inserta un nuevo ítem en la posición indicada
            self.agregar_al_final(item)   #Si no se pasa posición, lo inserta al final
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


        
    