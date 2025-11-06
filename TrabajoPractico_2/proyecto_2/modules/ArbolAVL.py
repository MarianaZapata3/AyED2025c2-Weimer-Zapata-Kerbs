from datetime import datetime #fecha

#Nodo del árbol AVL
class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha               #clave 
        self.temperatura = temperatura   #valor
        self.izq = None #establece el puntero al hijo izquierdo del nodo como None (si hay uno menor se coloca aca)
        self.der = None #establece el puntero al hijo derecho del nodo como None (si hay uno mayor se coloca aca)
        self.altura = 1 #inicia en 1 porque un nodo hoja tiene altura = 1

#Arbol AVL
class ArbolAVL:
    def __init__(self):
        self.raiz = None #raíz del árbol (inicialmente vacía)
    
    #inserta un nodo nuevo en el árbol
    def insertar(self, fecha, temperatura):
        self.raiz = self._insertar(self.raiz, fecha, temperatura)  #llama al método recursivo privado 

    #inserta rotaciones
    def _insertar(self, nodo, fecha, temperatura):
        if not nodo:
            return NodoAVL(fecha, temperatura) #crea un nodo
        elif fecha < nodo.fecha:
            nodo.izq = self._insertar(nodo.izq, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.der = self._insertar(nodo.der, fecha, temperatura)
        else:
            nodo.temperatura = temperatura  #actualiza si la fecha ya existe
            return nodo 

        #actualiza la altura del árbol y lo balancea
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))
        #obtener el factor de balance para saber si se desbalanceó
        balance = self.balance(nodo)
        #Izq-Izq
        if balance > 1 and fecha < nodo.izq.fecha:
            return self.rotacion_der(nodo)
        #Der-Der
        if balance < -1 and fecha > nodo.der.fecha:
            return self.rotacion_izq(nodo)
        #Izq-Der
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self.rotacion_izq(nodo.izq)
            return self.rotacion_der(nodo)
        #Der-Izq
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self.rotacion_der(nodo.der)
            return self.rotacion_izq(nodo)
        return nodo
    
    #busca un nodo por fecha
    def buscar(self, nodo, fecha):                  
        if not nodo:                                 #si el nodo no existe, no se encuentra la fecha
            return None
        if fecha == nodo.fecha:                      #si la fecha coincide, se devuelve la temperatura
            return nodo
        elif fecha < nodo.fecha:                     #si la fecha es menor, busca a la izquierda
            return self.buscar(nodo.izq, fecha)
        else:                                        #si es mayor, busca a la derecha
            return self.buscar(nodo.der, fecha)
    
    #busca la temperatura minima en el rango de fechas
    def min_en_rango(self, nodo, f1, f2):
        if not nodo:
            return float('inf')                         #valor muy grande si no hay datos
        if nodo.fecha < f1:                             #si la fecha está antes del rango, ir a la derecha
            return self.min_en_rango(nodo.der, f1, f2)
        elif nodo.fecha > f2:                           #si la fecha está después del rango, ir a la izquierda
            return self.min_en_rango(nodo.izq, f1, f2)
        else:
            #compara el valor actual con los mínimos del subárbol
            return min(nodo.temperatura,
                       self.min_en_rango(nodo.izq, f1, f2),
                       self.min_en_rango(nodo.der, f1, f2))
    
    #busca la temperatura maxima en el rango de fechas
    def max_en_rango(self, nodo, f1, f2):
        if not nodo:
            return float('-inf')                        #valor muy pequeño si no hay datos
        if nodo.fecha < f1:
            return self.max_en_rango(nodo.der, f1, f2)
        elif nodo.fecha > f2:
            return self.max_en_rango(nodo.izq, f1, f2)
        else:
            return max(nodo.temperatura,
                       self.max_en_rango(nodo.izq, f1, f2),
                       self.max_en_rango(nodo.der, f1, f2))
        
    #recorre el arbol y demuestra una lista ordenada del rango de fechas
    def listar_rango(self, nodo, f1, f2, lista):
        if nodo:
            if f1 <= nodo.fecha <= f2:                       #si la fecha está dentro del rango
                self.listar_rango(nodo.izq, f1, f2, lista)   #recorre primero el subárbol izquierdo
                lista.append((nodo.fecha, nodo.temperatura)) #agrega la medición actual
                self.listar_rango(nodo.der, f1, f2, lista)   #luego recorre el derecho
            elif nodo.fecha < f1:                            #si la fecha es menor al rango, avanza a la derecha
                self.listar_rango(nodo.der, f1, f2, lista)
            else:                                            #si es mayor, va a la izquierda
                self.listar_rango(nodo.izq, f1, f2, lista)
    
    #devuelve la altura del nodo en el árbol
    def altura(self, nodo):
        return nodo.altura if nodo else 0 
    
    #indica si el nodo esta equilibrado
    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0 
    
    #si se desbalancea hacia la izquierda, se realiza una rotación a la derecha para equilibrarlo
    def rotacion_der(self, y):
        x = y.izq #hijo izq de y
        T2 = x.der #guarda el hijo der de x
        x.der = y #mueve y a la der de x
        y.izq = T2 #el subárbol pasa a ser hijo izq de y
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        return x #nueva raiz del subarbol que se acaba de rotar

    #si se desbalancea hacia la derecha, se realiza una rotación a la izquierda para equilibrarlo
    def rotacion_izq(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        return y

