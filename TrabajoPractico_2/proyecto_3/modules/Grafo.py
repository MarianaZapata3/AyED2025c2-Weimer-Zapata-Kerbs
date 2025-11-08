#Clase que representa un vértice dentro de un grafo
class Vertice:
    def __init__(self, nombre):
        #cada vértice tiene un nombre que lo identifica
        self.nombre = nombre
        #lista de vértices adyacentes con sus respectivos pesos
        #cada elemento es una tupla: (vertice_destino, peso)
        self.adyacentes = []
    
    #funcion que agrega un vértice destino con el peso de la arista que los conecta
    def agregar_adyacente(self, destino, peso):
        self.adyacentes.append((destino, peso))


#Clase que representa un grafo no dirigido y ponderado
class Grafo:
    #funcion que genera una lista que almacena todos los vértices del grafo
    def __init__(self):
        self.vertices = []
    
    #funcion que agrega un vértice solo si no existe otro con el mismo nombre
    def agregar_vertice(self, nombre):
        if self.obtener_vertice(nombre) is None:
            self.vertices.append(Vertice(nombre))
    
    #funcion que busca y devuelve el vértice cuyo nombre coincide con el indicado
    def obtener_vertice(self, nombre):
        for v in self.vertices:
            if v.nombre == nombre:
                return v
        #si no se encuentra, devuelve None
        return None
    
    #funcion que busca los vértices de origen y destino dentro del grafo
    def agregar_arista(self, origen, destino, peso):
        v_origen = self.obtener_vertice(origen)
        v_destino = self.obtener_vertice(destino)
        if v_origen and v_destino:
            v_origen.agregar_adyacente(v_destino, peso)
            v_destino.agregar_adyacente(v_origen, peso)  #no dirigido


import os
#funcion externa para cargar el archivo
def cargar_grafo_desde_archivo(nombre_archivo):
    grafo = Grafo()
    
    #se contruye la ruta absoluta al archivo dentro de la carpeta "data"
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", nombre_archivo))
    print("📂 Buscando archivo en:", ruta)  # <- línea útil para depurar
    
    #se lee el archivo y cargan datos
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            partes = [x.strip() for x in linea.strip().split(",")]
            if len(partes) != 3:
                continue
            origen, destino, peso = partes
            try:
                peso = int(peso)
            except:
                continue
            grafo.agregar_vertice(origen)
            grafo.agregar_vertice(destino)
            grafo.agregar_arista(origen, destino, peso)
    
    return grafo



