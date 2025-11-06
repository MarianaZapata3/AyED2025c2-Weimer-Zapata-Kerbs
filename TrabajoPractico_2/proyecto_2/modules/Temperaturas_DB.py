from datetime import datetime
from modules.ArbolAVL import ArbolAVL  # importa la clase ArbolAVL para usarla dentro de la base de datos

#Clase que implementa la base de datos de temperaturas usando internamente un árbol AVL
class Temperaturas_DB:
    def __init__(self):
        self.arbol = ArbolAVL()  #se crea un árbol AVL vacío
        self._cantidad = 0       #contador de muestras totales

    #función que guarda una medida de temperatura asociada a una fecha
    def guardar_temperatura(self, temperatura, fecha):
        #intenta detectar si la fecha tiene guiones o barras
        try:
            if "-" in fecha:
                fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
            elif "/" in fecha:
                fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()
            else:
                raise ValueError("Formato de fecha no reconocido.")
        except ValueError:
            print(f"Fecha con formato inválido: {fecha}")
            return

        existente = self.arbol.buscar(self.arbol.raiz, fecha_obj)  #busca si ya existe un registro con esa fecha
        self.arbol.insertar(fecha_obj, temperatura)  #inserta la nueva temperatura en el árbol AVL
        if not existente:  #si no existía previamente, incrementa la cantidad de muestras
            self._cantidad += 1

    #función que devuelve la temperatura registrada en una fecha determinada
    def devolver_temperatura(self, fecha):
        if "-" in fecha:
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
        else:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()
        nodo = self.arbol.buscar(self.arbol.raiz, fecha_obj)  #busca el nodo con la fecha indicada
        if nodo:
            return nodo.temperatura  #si se encuentra, devuelve la temperatura
        else:
            return "No hay datos para esa fecha"  #si no existe, muestra mensaje de error

    #función que devuelve la temperatura máxima entre dos fechas
    def max_temp_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1.replace("/", "-"), "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2.replace("/", "-"), "%Y-%m-%d").date()
        return self.arbol.max_en_rango(self.arbol.raiz, f1, f2)

    #función que devuelve la temperatura mínima entre dos fechas
    def min_temp_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1.replace("/", "-"), "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2.replace("/", "-"), "%Y-%m-%d").date()
        return self.arbol.min_en_rango(self.arbol.raiz, f1, f2)

    #función que devuelve la temperatura mínima y máxima entre dos fechas
    def temp_extremos_rango(self, fecha1, fecha2):
        return (self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2))

    #función que devuelve un listado ordenado con las mediciones entre dos fechas
    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1.replace("/", "-"), "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2.replace("/", "-"), "%Y-%m-%d").date()
        lista = []  #almacena las mediciones en el rango
        self.arbol.listar_rango(self.arbol.raiz, f1, f2, lista)  #llama al método del árbol AVL
        #formatea la salida con el formato “yyyy-mm-dd: temperatura ºC”
        return [f"{fecha.strftime('%Y-%m-%d')}: {temp} ºC" for fecha, temp in lista]

    #función que devuelve la cantidad de muestras registradas
    def cantidad_muestras(self):
        return self._cantidad

    #función que elimina una medición por fecha
    def borrar_temperatura(self, fecha):
        if "-" in fecha:
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
        else:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()
        existente = self.arbol.buscar(self.arbol.raiz, fecha_obj)
        if existente:
            #en este caso no se implementa borrado físico (no requerido en el TP)
            self._cantidad -= 1

    #función que lee un archivo y carga todas las mediciones a la base de datos
    def cargar_desde_archivo(self, ruta_archivo):
        try:
            with open(ruta_archivo, "r", encoding="utf-16") as archivo:
                for linea in archivo:
                    if not linea.strip():  #salta líneas vacías
                        continue
                    try:
                        #separa por punto y coma
                        fecha, temp = linea.strip().split(";")
                        #guarda cada dato en el árbol
                        self.guardar_temperatura(float(temp.strip()), fecha.strip())
                    except ValueError:
                        print(f"Línea con formato incorrecto: {linea.strip()}")
        except FileNotFoundError:
            print(f"Error: no se encontró el archivo '{ruta_archivo}'")


#Se carga el archivo de temperaturas
if __name__ == "__main__":
    db = Temperaturas_DB()  # crea una base de datos vacía
    db.cargar_desde_archivo("data/muestras.txt")

    #Consultas usando fechas del archivo muestras.txt
    print("Temperatura del 2025-01-10:", db.devolver_temperatura("2025-01-10"))
    print("Temperatura máxima entre 2025-01-01 y 2025-01-20:", db.max_temp_rango("2025-01-01", "2025-01-20"))
    print("Temperatura mínima entre 2025-01-01 y 2025-01-20:", db.min_temp_rango("2025-01-01", "2025-01-20"))
    print("Extremos entre 2025-01-01 y 2025-01-30:", db.temp_extremos_rango("2025-01-01", "2025-01-30"))
    print("Listado completo entre 2025-01-01 y 2025-01-30:", db.devolver_temperaturas("2025-01-01", "2025-01-30"))
    print("Cantidad total de muestras:", db.cantidad_muestras())

    #Ejemplo de borrar una temperatura
    db.borrar_temperatura("2025-01-10")
    print("Cantidad de muestras después de borrar:", db.cantidad_muestras())
