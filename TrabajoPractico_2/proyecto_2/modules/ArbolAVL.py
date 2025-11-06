
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
        self.raiz = None                     # raíz del árbol (inicialmente vacía)
