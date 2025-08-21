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

    


        
    