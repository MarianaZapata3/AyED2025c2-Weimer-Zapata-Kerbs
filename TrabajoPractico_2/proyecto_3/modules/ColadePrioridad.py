#Clase que implementa una Cola de Prioridad usando un montículo binario (heap)
class ColaPrioridad:
    def __init__(self):
        #es una lista interna que almacena las tuplas (prioridad, contador, item)
        #tiene un contador que asegura orden de llegada cuando las prioridades son iguales
        self._heap = []
        self._contador = 0  
    
    #funcion que devuelve True si el elemento en posición i tiene menor prioridad que el de j
    def esmenor(self, i, j):
        #y se comparan los dos primeros valores|| (prioridad, contador)
        return tuple(self._heap[i][:2]) < tuple(self._heap[j][:2])
    
    #funcion que restaura la propiedad del montículo moviendo el elemento hacia arriba
    def arriba(self, idx):
        #se usa al insertar un nuevo elemento al final del heap
        while idx > 0:  #mientras no estemos en la raíz
            padre = (idx - 1) // 2  #indice del nodo padre
            if self.esmenor(idx, padre):  #si el hijo tiene menor prioridad que el padre se intercambian las posiciones
                self._heap[idx], self._heap[padre] = self._heap[padre], self._heap[idx]
                idx = padre  #se actualizanel índice y se sigue subiendo
            else:
                break  #si el padre ya tiene menor prioridad, se detiene el ajuste
    
    #funcion que restaura la propiedad del montículo moviendo el elemento hacia abajo
    def abajo(self, idx):
        #se usa al eliminar el elemento raíz (menor prioridad)
        n = len(self._heap)  #tamaño actual del heap
        while True:
            izq = 2 * idx + 1  #indice del hijo izquierdo
            der = 2 * idx + 2  #indice del hijo derecho
            menor = idx         #se asume que el menor es el nodo actual
            
            #comparamos con el hijo izquierdo
            if izq < n and self.esmenor(izq, menor):
                menor = izq
            #comparamos con el hijo derecho
            if der < n and self.esmenor(der, menor):
                menor = der
            #si el nodo actual ya es menor que ambos hijos, salimos
            if menor == idx:
                break
            #se intercambia el nodo con su hijo menor
            self._heap[idx], self._heap[menor] = self._heap[menor], self._heap[idx]
            idx = menor  #se continua bajando en el heap
    
    #funcion que inserta un nuevo elemento en la cola con su prioridad
    def encolar(self, item, prioridad):
        entrada = [prioridad, self._contador, item]  #se crea la entrada completa
        self._contador += 1                          #se incrementa el contador para el siguiente
        self._heap.append(entrada)                   #agregamos el elemento al final del heap
        self.arriba(len(self._heap) - 1)             #y ajustamos su posición hacia arriba

    #funcion que extrae y devuelve el elemento de mayor prioridad
    def desencolar(self):
        if not self._heap:           #si el monticulo está vacío, no hay nada que extraer
            return None
        raiz = self._heap[0][2]      #el elemento con mayor prioridad está en la raíz
        ultimo = self._heap.pop()    #se quita el último elemento
        if self._heap:               #si aun quedan elementos
            self._heap[0] = ultimo   #se mueve el último a la raíz
            self.abajo(0)            #y se ajusta hacia abajo para restaurar el orden
        return raiz                  #luego se devuelve el elemento extraído
    
    #funcion que devuelve True si la cola de prioridad esta vacia
    def esta_vacia(self):
        return len(self._heap) == 0