#se implementa una cola de prioridad usando un montículo (heap) propio para asegurar que siempre se atienda primero al paciente con mayor riesgo

class ColaPrioridad:
    def __init__(self):
        #lista interna que almacena las tuplas (prioridad, llegada, contador, item)
        self._heap = []
        #contador interno para romper empates en ciertos casos
        self._contador = 0
    
    #función que compara dos elementos del montículo según su prioridad y llegada
    def esmenor(self, i, j):
        #devuelve true si el elemento en la posición i tiene mayor prioridad (o llegó antes) que el de j
        return tuple(self._heap[i][:3]) < tuple(self._heap[j][:3])
    
    #función que acomoda hacia arriba un elemento recién insertado 
    #el nuevo elemento va subiendo niveles en el árbol hasta que esta en el lugar correcto
    def arriba(self, idx):
        while idx > 0:
            padre = (idx - 1) // 2
            #si el nodo hijo tiene mayor prioridad que su padre, se intercambian
            if self.esmenor(idx, padre):
                self._heap[idx], self._heap[padre] = self._heap[padre], self._heap[idx]
                idx = padre
            else:
                break

    #función que acomoda hacia abajo un elemento (después de eliminar la raíz)
    def abajo(self, idx):
        n = len(self._heap) #cantidad de elementos en el montículo
        while True:
            izq = 2 * idx + 1 #hijo izquierdo
            der = 2 * idx + 2 #hijo derecho
            menor = idx #asumimos que el elemento actual es el menor
            #se elige el hijo con mayor prioridad (menor valor en la tupla)
            if izq < n and self.esmenor(izq, menor):
                menor = izq
            if der < n and self.esmenor(der, menor):
                menor = der
            if menor == idx:
                break
            #se intercambian posiciones y se continúa descendiendo
            self._heap[idx], self._heap[menor] = self._heap[menor], self._heap[idx]
            idx = menor
    
    #función que encola (ingresa) un nuevo elemento con su prioridad y orden de llegada
    def encolar(self, item, prioridad, llegada=None):
        #si no se pasa llegada, se busca el atributo timestamp del paciente
        if llegada is None:
            llegada = getattr(item, "timestamp", None)
            #si el item no tiene timestamp, se usa el contador interno como llegada
            if llegada is None:
                llegada = self._contador
        #se crea una entrada con la prioridad, la llegada y el contador interno
        entrada = [prioridad, llegada, self._contador, item]
        self._contador += 1  #se incrementa el contador interno
        self._heap.append(entrada)  #se agrega el nuevo elemento al final
        self.arriba(len(self._heap) - 1)  #se reacomoda hacia arriba según la prioridad

    #función que desencola (extrae) el elemento de mayor prioridad
    def desencolar(self):
        if not self._heap:
            return None  #si la cola está vacía, no se puede extraer
        raiz = self._heap[0][3]  #se guarda el item de mayor prioridad
        ultimo = self._heap.pop()  #se quita el último elemento
        if self._heap:
            self._heap[0] = ultimo  #se mueve al principio el último
            self.abajo(0)      #se reacomoda hacia abajo
        return raiz  #se devuelve el item extraído

    #función que devuelve todos los elementos ordenados por prioridad y llegada (sin modificar el monticulo)
    def ver_todos(self):
        #se ordena temporalmente según prioridad, llegada y el contador
        ordenados = sorted(self._heap, key=lambda e: (e[0], e[1], e[2]))
        return [e[3] for e in ordenados]
    
    #función que devuelve True si la cola está vacía
    def esta_vacia(self):
        return len(self._heap) == 0

    #función que devuelve la cantidad de elementos en la cola
    def __len__(self):
        return len(self._heap)

        



