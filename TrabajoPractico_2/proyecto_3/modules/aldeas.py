# PROBLEMA: Comunicación eficiente entre aldeas con palomas
# Objetivo: Encontrar la forma más eficiente (mínimo recorrido) para que todas las aldeas reciban la noticia desde "Peligros"
# usando el Algoritmo de Prim (Árbol de Expansión Mínima).
# Se pide que muestre: la lista de aldeas en orden alfabético, para cada aldea de qué vecina debe recibir la noticia (padre) y a qué vecinas debe enviar réplicas (hijos)
# y la suma total de todas las distancias recorridas (peso total del MST)

import os          
import heapq                
from collections import defaultdict, deque  


# Se carga el contenido del archivo aldeas.txt
archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "aldeas.txt"))

# Se crea un diccionario donde cada aldea tiene una lista de aldeas vecinas con su distancia
grafo = defaultdict(list)

# Se abre el archivo en modo lectura
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        # Se separa la línea con comas y se eliminan los espacios entre ellas
        partes = [x.strip() for x in linea.strip().split(",")]
        # Si la línea no tiene exactamente 3 elementos, se salta
        if len(partes) != 3:
            continue
        # Se extraen los datos: nombre de las aldeas y la distancia
        a, b, w = partes
        # Se intenta convertir la distancia en un número entero
        try:
            w = int(w)
        except:
            # Si no se puede convertir, se ignora esa línea
            continue
        # Como el grafo es no dirigido, se agrega la conexión en ambos sentidos
        grafo[a].append((b, w))
        grafo[b].append((a, w))



# Algoritmo Prim
# Aldea desde donde se inicia la comunicación
origen = "Peligros"

# Conjunto que almacenará las aldeas ya conectadas
visitados = {origen}

# Se arma la cola de prioridad con las aristas que salen desde Peligros
# Cada elemento tiene la forma (peso, desde, hasta)
heap = [(w, origen, v) for v, w in grafo[origen]]

# Se transforma la lista en un min-heap (una cola ordenada por peso)
heapq.heapify(heap)

# Lista donde se guardarán las aristas seleccionadas del Árbol de Expansión Mínima
mst = []

# Mientras haya aristas disponibles y no se hayan conectado todas las aldeas
while heap and len(visitados) < len(grafo):
    # Se saca la arista con menor peso (distancia)
    w, u, v = heapq.heappop(heap)
    
    # Si la aldea de destino aún no fue visitada, se agrega al MST
    if v not in visitados:
        visitados.add(v)         # Se marca como conectada
        mst.append((u, v, w))    # Se guarda la conexión (u-v con peso w)
        
        # Se agregan las nuevas aristas que salen desde esta aldea
        for vecino, peso in grafo[v]:
            if vecino not in visitados:
                heapq.heappush(heap, (peso, v, vecino))



# Construccion del árbol
# Se arma una nueva estructura de adyacencia a partir del MST
# Esto servirá para recorrer fácilmente las conexiones del árbol final
adj = defaultdict(list)
for u, v, w in mst:
    adj[u].append((v, w))
    adj[v].append((u, w))  # Como es no dirigido, se agrega en ambos sentidos



# Se determina a quien envia y quien recibe el mensaje
# Diccionario que guarda quién es el "padre" (quién le envió la noticia)
padre = {origen: None}

# Diccionario que guarda a quiénes debe enviar cada aldea (sus "hijos")
hijos = defaultdict(list)

# Diccionario que guarda la distancia usada en cada conexión
distancia = {}

# Se usa una cola para recorrer el árbol desde "Peligros"
cola = deque([origen])
visitados = {origen}

# Bucle principal del recorrido
while cola:
    actual = cola.popleft()  # Se saca una aldea de la cola
    for vecino, w in adj[actual]:  # Se recorren sus vecinos conectados
        if vecino not in visitados:
            visitados.add(vecino)      # Se marca como visitado
            padre[vecino] = actual     # Se registra quién le mandó la noticia
            hijos[actual].append(vecino)  # Se agrega a quiénes reenvía
            distancia[vecino] = w      # Se guarda la distancia de esa conexión
            cola.append(vecino)        # Se agrega el vecino a la cola para seguir el recorrido


# Resultados
# Se muestran las aldeas en orden alfabético
print("\nAldeas ordenadas alfabeticamente:")
for n in sorted(grafo.keys(), key=lambda s: s.lower()):
    print(f" - {n}")

# Tabla de aldea, de donde viene y hacia donde envia
print("\nRutas de comunicacion (desde 'Peligros'):")
print(f"{'Aldea':20s}|{'Recibe de':15s}|{'Envía a':40s}")
print("-" * 80)

# Recorre las aldeas ordenadas y muestra sus relaciones
for n in sorted(grafo.keys(), key=lambda s: s.lower()):
    # Quién le envía la noticia (si es Peligros, muestra "-")
    recibe = padre[n] if padre.get(n) else "-"
    
    # A quiénes reenvía la noticia
    envia = ", ".join(sorted(hijos[n])) if hijos[n] else "-"
    
    # Imprime la información
    print(f"{n:20s}|{recibe:15s}|{envia:40s}")


# Cálculo de la distancia total recorrida
# Se suman todas las distancias del MST para obtener el costo mínimo total
dist_total = sum(w for _, _, w in mst)

# Se muestra el resultado final
print(f"\nDistancia total recorrida por todas las palomas: {dist_total} leguas")