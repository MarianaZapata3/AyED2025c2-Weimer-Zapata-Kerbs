#Para el ejercicio 2

from datetime import datetime #fecha

#Nodo del árbol AVL
class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha               # clave (datetime)
        self.temperatura = temperatura   # valor (float)
        self.izq = None #establece el puntero al hijo izquierdo del nodo como None (si hay uno menor se coloca aca)
        self.der = None #establece el puntero al hijo derecho del nodo como None (si hay uno mayor se coloca aca)
        self.altura = 1 #inicia en 1

#Clase donde se guardan las mediciones de temperaturas con AVL
class Temperaturas_DB:
    def __init__(self):
        self.raiz = None #inicia la raiz del arbol como none
        self._cantidad = 0 #contador para saber cuantas mediciones en total

# Métodos auxiliares del AVL
    def altura(self, nodo):
        return nodo.altura if nodo else 0 #devuelve la altura del nodo en el árbol

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

#se mantiene el árbol AVL balanceado después de insertar un nodo nuevo
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



#Métodos
    # Guarda una nueva temperatura asociada a una fecha
    def guardar_temperatura(self, temperatura, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()
        self.raiz = self._insertar(self.raiz, fecha_obj, temperatura)
        self._cantidad += 1

    # Devuelve la temperatura de una fecha especifica
    def devolver_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()
        nodo = self._buscar(self.raiz, fecha_obj)
        return nodo.temperatura if nodo else None

    # Devuelve la cantidad de muestras registradas
    def cantidad_muestras(self):
        return self._cantidad

    # Devuelve temperaturas entre dos fechas (ordenadas)
    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
        resultados = []
        self._rango_fechas(self.raiz, f1, f2, resultados)
        resultados.sort(key=lambda x: x[0])
        return [f"{f.strftime('%d/%m/%Y')}: {t} ºC" for f, t in resultados]

    # Devuelve la temperatura máxima entre dos fechas
    def max_temp_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
        temperaturas = []
        self._rango_fechas(self.raiz, f1, f2, temperaturas)
        return max([t for _, t in temperaturas]) if temperaturas else None

    # Devuelve la temperatura mínima entre dos fechas
    def min_temp_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
        temperaturas = []
        self._rango_fechas(self.raiz, f1, f2, temperaturas)
        return min([t for _, t in temperaturas]) if temperaturas else None

    # Devuelve temperatura mínima y máxima entre dos fechas
    def temp_extremos_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
        temperaturas = []
        self._rango_fechas(self.raiz, f1, f2, temperaturas)
        if not temperaturas:
            return None, None
        vals = [t for _, t in temperaturas]
        return min(vals), max(vals)

    # Elimina una medición por fecha
    def borrar_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()
        self.raiz = self._eliminar(self.raiz, fecha_obj)
        self._cantidad -= 1



#Métodos auxiliares del árbol AVL
# Inserta un nodo en el árbol 
    def _insertar(self, nodo, fecha, temperatura):
        if not nodo:
            return NodoAVL(fecha, temperatura)
        elif fecha < nodo.fecha:
            nodo.izq = self._insertar(nodo.izq, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.der = self._insertar(nodo.der, fecha, temperatura)
        else:
            nodo.temperatura = temperatura  # Actualiza si la fecha ya existe
            return nodo

        # Actualiza la altura del árbol y lo balancea
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))
        return self.balancear(nodo, fecha)

# Busca un nodo por fecha
    def _buscar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha == nodo.fecha:
            return nodo
        elif fecha < nodo.fecha:
            return self._buscar(nodo.izq, fecha)
        else:
            return self._buscar(nodo.der, fecha)

# Recorre el árbol entre dos fechas
    def _rango_fechas(self, nodo, f1, f2, resultados):
        if not nodo:
            return
        if f1 <= nodo.fecha <= f2:
            resultados.append((nodo.fecha, nodo.temperatura))
        if nodo.fecha > f1:
            self._rango_fechas(nodo.izq, f1, f2, resultados)
        if nodo.fecha < f2:
            self._rango_fechas(nodo.der, f1, f2, resultados)

# Elimina un nodo por fecha
    def _eliminar(self, nodo, fecha):
        if not nodo:
            return nodo
        if fecha < nodo.fecha:
            nodo.izq = self._eliminar(nodo.izq, fecha)
        elif fecha > nodo.fecha:
            nodo.der = self._eliminar(nodo.der, fecha)
        else:
            # Nodo con 1 o ningún hijo
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq
            # Nodo con 2 hijos: es reemplazado por el sucesor (el nodo menor del subárbol decercho)
            temp = self._min_nodo(nodo.der)
            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura
            nodo.der = self._eliminar(nodo.der, temp.fecha)
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))
        return self.balancear(nodo, fecha)

# Encuentra el nodo con la fecha mínima
    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

# Cargar desde archivo (corregido)
    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-16") as f: 
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
                    self.guardar_temperatura(float(temp_str.strip()), fecha_formato) #se ejecuta cuando este def_guardar
                except ValueError as e:
                    print(f"Error procesando línea '{linea}': {e}")
                    continue