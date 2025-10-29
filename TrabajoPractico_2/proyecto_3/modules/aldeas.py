"""
Propósito:
- Leer un archivo `aldeas.txt` con aristas: cada línea contiene "origen destino distancia"
  (separador puede ser espacio o coma). Ejemplo:  Peligros Aldea2 10
- Construir el grafo no dirigido ponderado
- Calcular el Árbol de Expansión Mínima (MST) usando Prim, arrancando en 'Peligros'
- Se tiene que mostrar:
    1) Lista de aldeas en orden alfabético
    2) Para cada aldea: de qué vecina debe recibir la noticia (padre) y a qué vecinas debe enviar réplicas (hijos)
    3) Suma total de todas las distancias recorridas (peso total del MST)

Notas:
- Si 'Peligros' no está en el grafo, el script avisará e iniciará Prim desde un nodo arbitrario.
- Si el grafo no es conexo, se mostrará un MST por componente y la suma total será la suma de todos los componentes mínimos (pero en ese caso no existe una forma de alcanzar *todas* las aldeas desde Peligros).

"""
import os
import heapq
from collections import defaultdict, deque

#Se carga el archivo desde aldeas.txt
#Formato de cada línea: aldea1, aldea2, distancia
archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "aldeas.txt"))

#Se crea un grafo como diccionario de listas
grafo = defaultdict(list)
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        partes = [x.strip() for x in linea.strip().split(",")]
        if len(partes) != 3:
            continue
        a, b, w = partes
        try:
            w = int(w)
        except:
            continue
        #Grafo no dirigido (es bidireccional)
        grafo[a].append((b, w))
        grafo[b].append((a, w))

#Algoritmo de Prim
origen = "Peligros"              #aldea de inicio
visitados = {origen}             #conjunto de aldeas visitadas
heap = [(w, origen, v) for v, w in grafo[origen]]  # cola de prioridad (min-heap)
heapq.heapify(heap)

mst = []  #lista de aristas del árbol mínimo

while heap and len(visitados) < len(grafo):
    w, u, v = heapq.heappop(heap)
    if v not in visitados:
        visitados.add(v)
        mst.append((u, v, w))
        for vecino, peso in grafo[v]:
            if vecino not in visitados:
                heapq.heappush(heap, (peso, v, vecino))

#Construcción del árbol de comunicación
adj = defaultdict(list)
for u, v, w in mst:
    adj[u].append((v, w))
    adj[v].append((u, w))

#Determinar quién recibe y a quién envía (BFS desde "Peligros")
padre = {origen: None}
hijos = defaultdict(list)
distancia = {}

cola = deque([origen])
visitados = {origen}

while cola:
    actual = cola.popleft()
    for vecino, w in adj[actual]:
        if vecino not in visitados:
            visitados.add(vecino)
            padre[vecino] = actual
            hijos[actual].append(vecino)
            distancia[vecino] = w
            cola.append(vecino)

#Resultados
print("\nAldeas ordenadas alfabéticamente")
for n in sorted(grafo.keys(), key=lambda s: s.lower()):
    print(n)

print("\nRutas de comunicación (desde 'Peligros')")
print(f"{'Aldea':20s}|{'Recibe de':15s}|{'Envía a':40s}")
print("-"*80)
for n in sorted(grafo.keys(), key=lambda s: s.lower()):
    recibe = padre[n] if padre.get(n) else "-"
    envia = ", ".join(sorted(hijos[n])) if hijos[n] else "-"
    print(f"{n:20s}|{recibe:15s}|{envia:40s}")

#Distancia total mínima
dist_total = sum(w for _, _, w in mst)
print(f"\nDistancia total recorrida: {dist_total} leguas")
