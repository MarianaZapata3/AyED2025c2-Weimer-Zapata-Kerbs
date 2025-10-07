#Para el ejercicio 2

from datetime import datetime #fecha

# Nodo del árbol AVL
class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha               # clave (datetime)
        self.temperatura = temperatura   # valor (float)
        self.izq = None #establece el puntero al hijo izquierdo del nodo como None (si hay uno menor se coloca aca)
        self.der = None #establece el puntero al hijo derecho del nodo como None (si hay uno mayor se coloca aca)
        self.altura = 1 #inicia en 1

# Clase donde se guardan las mediciones de temperaturas con AVL
class Temperaturas_DB:
    def __init__(self):
        self.raiz = None #inicia la raiz del arbol como none
        self._cantidad = 0 #contador para saber cuantas mediciones en total

# Métodos auxiliares del AVL
    def altura(self, nodo):
        return nodo.altura if nodo else 0 #devuelve la altura del nodo en el arbol

#indica si el nodo esta equilibrado
    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0 

#se desbalancea hacia la izquierda, se realiza una rotación a la derecha para equilibrarlo
    def rotacion_der(self, y):
        x = y.izq #hijo izq de y
        T2 = x.der #guarda el hijo der de x
        x.der = y #mueve y a la der de x
        y.izq = T2 #el subarbol pasa a ser hijo izq de y
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        return x #nueva raiz del subarbol que se acaba de rotar

#se desbalancea hacia la derecha, se realiza una rotación a la izquierda para equilibrarlo
    def rotacion_izq(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        return y

#Mantener el árbol AVL balanceado después de insertar un nodo nuevo
    def balancear(self, nodo, fecha):
        balance = self.balance(nodo)
        # Izq-Izq
        if balance > 1 and fecha < nodo.izq.fecha:
            return self.rotacion_der(nodo)
        # Der-Der
        if balance < -1 and fecha > nodo.der.fecha:
            return self.rotacion_izq(nodo)
        # Izq-Der
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self.rotacion_izq(nodo.izq)
            return self.rotacion_der(nodo)
        # Der-Izq
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self.rotacion_der(nodo.der)
            return self.rotacion_izq(nodo)
        return nodo

# Cargar desde archivo (corregido)
    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-16") as f:  # <--- importante
            #Recorre cada línea del archivo.
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                #verifica que cada linea tenga fecha y temperatura
                partes = linea.split(";")
                if len(partes) != 2:
                    print(f"Línea inválida ignorada: {linea}")
                    continue
                fecha_str, temp_str = partes
                #modifica el formato de fecha y lo guarda en la base de datos
                try:
                    fecha_obj = datetime.strptime(fecha_str.strip(), "%Y-%m-%d").date()
                    fecha_formato = fecha_obj.strftime("%d/%m/%Y")
                    #self.guardar_temperatura(float(temp_str.strip()), fecha_formato) se ejecuta cuando este def_guardar
                except ValueError as e:
                    print(f"Error procesando línea '{linea}': {e}")
                    continue
