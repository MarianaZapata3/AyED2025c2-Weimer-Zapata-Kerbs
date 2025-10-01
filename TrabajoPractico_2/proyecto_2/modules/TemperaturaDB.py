#Para el ejercicio 2
print("2")

from datetime import datetime

# ------------------------------
# Nodo del árbol AVL
# ------------------------------
class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha               # clave (datetime)
        self.temperatura = temperatura   # valor (float)
        self.izq = None
        self.der = None
        self.altura = 1

# ------------------------------
# Base de datos de temperaturas con AVL
# ------------------------------
class Temperaturas_DB:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    # ------------------------------
    # Métodos auxiliares del AVL
    # ------------------------------
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    def _rotacion_der(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        return x

    def _rotacion_izq(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    def _balancear(self, nodo, fecha):
        balance = self._balance(nodo)
        # Izq-Izq
        if balance > 1 and fecha < nodo.izq.fecha:
            return self._rotacion_der(nodo)
        # Der-Der
        if balance < -1 and fecha > nodo.der.fecha:
            return self._rotacion_izq(nodo)
        # Izq-Der
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self._rotacion_izq(nodo.izq)
            return self._rotacion_der(nodo)
        # Der-Izq
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self._rotacion_der(nodo.der)
            return self._rotacion_izq(nodo)
        return nodo
# ------------------------------
# Cargar desde archivo (corregido)
# ------------------------------
    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-16") as f:  # <--- importante
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 2:
                    print(f"Línea inválida ignorada: {linea}")
                    continue
                fecha_str, temp_str = partes
                try:
                    fecha_obj = datetime.strptime(fecha_str.strip(), "%Y-%m-%d").date()
                    fecha_formato = fecha_obj.strftime("%d/%m/%Y")
                    self.guardar_temperatura(float(temp_str.strip()), fecha_formato)
                except ValueError as e:
                    print(f"Error procesando línea '{linea}': {e}")
                    continue
# ------------------------------
# Guardar temperatura
# ------------------------------
    def guardar_temperatura(self, temperatura, fecha):
        fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def _insertar(self, nodo, fecha, temp):
            if not nodo:
                self._cantidad += 1
                return NodoAVL(fecha, temp)
            elif fecha < nodo.fecha:
                nodo.izq = self._insertar(nodo.izq, fecha, temp)
            elif fecha > nodo.fecha:
                nodo.der = self._insertar(nodo.der, fecha, temp)
            else:
                nodo.temperatura = temp  # actualizar si ya existe
                return nodo
            nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
            return self._balancear(nodo, fecha)
