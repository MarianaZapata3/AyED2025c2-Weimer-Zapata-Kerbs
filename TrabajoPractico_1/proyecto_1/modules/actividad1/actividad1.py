# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el 
#TP1 Actividad 1

# Clase Nodo: representa un elemento de la lista doblemente enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato        # Guarda el valor del nodo
        self.siguiente = None   # Referencia al siguiente nodo (inicialmente None)
        self.anterior = None    # Referencia al nodo anterior (inicialmente None)

# Clase ListaDobleEnlazada: maneja la lista completa
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None      # Primer nodo de la lista
        self.cola = None        # Último nodo de la lista
        self.tamanio = 0        # Cantidad de elementos en la lista

    # Método para verificar si la lista está vacía
    def esta_vacia(self):
        return self.tamanio == 0  # Devuelve True si no hay elementos

    # Método para agregar un elemento al inicio de la lista
    def agregar_al_inicio(self, item):
        nodo = Nodo(item)            # Crea un nuevo nodo con el dato recibido
        if self.esta_vacia():        # Si la lista está vacía
            self.cabeza = self.cola = nodo  # El nuevo nodo es cabeza y cola
        else:                        # Si la lista NO está vacía
            nodo.siguiente = self.cabeza    # El siguiente del nuevo nodo apunta a la antigua cabeza
            self.cabeza.anterior = nodo     # La antigua cabeza apunta atrás al nuevo nodo
            self.cabeza = nodo              # El nuevo nodo pasa a ser la cabeza
        self.tamanio += 1           # Incrementa el tamaño de la lista

    # Método para agregar un elemento al final de la lista
    def agregar_al_final(self, item):
        nodo = Nodo(item)             # Crea un nuevo nodo con el dato recibido
        if self.esta_vacia():         # Si la lista está vacía
            self.cabeza = self.cola = nodo  # El nuevo nodo es cabeza y cola
        else:                         # Si la lista NO está vacía
            nodo.anterior = self.cola     # El anterior del nuevo nodo apunta a la antigua cola
            self.cola.siguiente = nodo    # La antigua cola apunta al nuevo nodo
            self.cola = nodo              # El nuevo nodo pasa a ser la cola
        self.tamanio += 1            # Incrementa el tamaño de la lista

    # Método para insertar un elemento en una posición específica
    def insertar(self, item, posicion=None):
        if posicion is None:               # Si no se indica posición
            self.agregar_al_final(item)    # Inserta el elemento al final
            return

        if posicion < 0 or posicion > self.tamanio:  # Si la posición es inválida
            raise Exception("Posición inválida")    # Lanza un error

        if posicion == 0:                  # Si la posición es 0
            self.agregar_al_inicio(item)   # Inserta al inicio
            return
        if posicion == self.tamanio:       # Si la posición es igual al tamaño
            self.agregar_al_final(item)    # Inserta al final
            return

        nodo = Nodo(item)                  # Crea un nuevo nodo con el dato recibido
        actual = self.cabeza               # Comienza a recorrer desde la cabeza
        for _ in range(posicion):          # Avanza hasta la posición deseada
            actual = actual.siguiente

        # Ajusta los punteros del nuevo nodo y los nodos vecinos
        nodo.anterior = actual.anterior    # El anterior del nuevo nodo apunta al nodo anterior al actual
        nodo.siguiente = actual            # El siguiente del nuevo nodo apunta al nodo actual
        actual.anterior.siguiente = nodo   # El siguiente del nodo anterior apunta al nuevo nodo
        actual.anterior = nodo             # El anterior del nodo actual apunta al nuevo nodo
        self.tamanio += 1                  # Incrementa el tamaño de la lista

    #Extraer
    def extraer(self, posicion=None):    
        if self.esta_vacia():
            raise Exception("La lista está vacía")

        if posicion is None:
            posicion = self.tamanio - 1

        if posicion < 0:
            posicion += self.tamanio

        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")

        if posicion < self.tamanio // 2:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.tamanio - 1, posicion, -1):
                actual = actual.anterior

        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente

        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        else:
            self.cola = actual.anterior

        self.tamanio -= 1
        return actual.dato

    #Copiar
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    #Invertir
    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza  # Intercambiar cabeza y cola
        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior  # Como intercambiamos, avanzar por "anterior"

    #Concatenar
    def concatenar(self, otra_lista):
        otra = otra_lista.copiar()  # <-- aseguramos que los punteros sean limpios
        if otra.esta_vacia():
            return self

        if self.esta_vacia():
            self.cabeza = otra.cabeza
            self.cola = otra.cola
        else:
            self.cola.siguiente = otra.cabeza
            otra.cabeza.anterior = self.cola
            self.cola = otra.cola

        self.cabeza.anterior = None
        self.tamanio += otra.tamanio
        return self

    
    #__len__(): devuelve el número de ítems de la lista
    def __len__(self):
        return self.tamanio

    #__add__(self, otra_lista): suma de dos listas
    def __add__(self, otra_lista):
        if not isinstance(otra_lista, ListaDobleEnlazada):
            raise Exception("Solo se pueden sumar listas dobles enlazadas")

        # Usamos copiar() para no modificar la lista original
        nueva = self.copiar()
        nueva.concatenar(otra_lista.copiar())  # Concatenamos una copia de la otra lista
        return nueva

    #__iter__(): permite recorrer la lista con un for
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

#grafico para actividad 1 (NO EJECUTAR HASTA TENER TODO)
import time
import matplotlib.pyplot as plt
from modules.actividad1.actividad1 import ListaDobleEnlazada
import random

# Tamaños de prueba
N_list = list(range(100, 10001, 500))
# Guardamos los tiempos
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for N in N_list:
    lde = ListaDobleEnlazada()
    for i in range(N):
        lde.agregar_al_final(random.randint(0, 1000))

    # medir len
    start = time.perf_counter()
    _ = len(lde)
    end = time.perf_counter()
    tiempos_len.append(end - start)

    # medir copiar
    start = time.perf_counter()
    _ = lde.copiar()
    end = time.perf_counter()
    tiempos_copiar.append(end - start)

    # medir invertir
    start = time.perf_counter()
    lde.invertir()
    end = time.perf_counter()
    tiempos_invertir.append(end - start)

# Graficar
plt.figure(figsize=(10,6))
plt.plot(N_list, tiempos_len, marker='o', label='len()')
plt.plot(N_list, tiempos_copiar, marker='s', label='copiar()')
plt.plot(N_list, tiempos_invertir, marker='^', label='invertir()')
plt.xlabel('Número de elementos N')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución vs tamaño de lista')
plt.legend()
plt.grid(True)
plt.show()


        
    