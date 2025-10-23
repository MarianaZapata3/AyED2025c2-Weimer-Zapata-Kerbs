import os, heapq

#Cargamos los datos txt en un archivo
archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "aldeas.txt"))

#Creacion del grafo:
grafo = {}
with open(archivo, "r", encoding="utf-8") as f:
    for l in f:
        p = [x.strip() for x in l.strip().split(",")] #separa a,b y peso
        if len(p) != 3: continue #ignora cualquier linea que es invalida
        a,b,w = p
        try: w=int(w) #convierte la distancia en un numero
        except: continue
        #guarda los vecinos bidireccionalmente
        grafo.setdefault(a,[]).append((b,w))
        grafo.setdefault(b,[]).append((a,w))

# Prim
origen="Peligros"
visitados={origen} #aldeas incluidas en el MST
heap=[(w,origen,v) for v,w in grafo[origen]]; heapq.heapify(heap) #cola de prioridad para aristas
mst=[] #lista donde se guardan las aristas
while heap and len(visitados)<len(grafo):
    w,f,t = heapq.heappop(heap) #se selecciona la arista mas pequeña
    if t not in visitados:
        visitados.add(t) #marca la aldea que se visito
        mst.append((f,t,w)) #agrega la arista al MST
        #se agregan nuevas aristas a la cola
        for v,ww in grafo[t]:
            if v not in visitados: heapq.heappush(heap,(ww,t,v))

# Resultado
print("=== MST (Prim) ===")
for f,t,w in mst: print(f"{f} — {t} : {w} leguas")
print("Costo total:", sum(w for _,_,w in mst),"leguas")


