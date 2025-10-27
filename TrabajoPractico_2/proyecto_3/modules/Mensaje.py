import os
from collections import deque

# Se almacenan los datos del txt en archivo
archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "aldeas.txt"))

# Union-Find
class UF:
    def __init__(self): self.p,self.r={},{} #diccionarios
    def make(self,x): self.p[x]=x; self.r[x]=0 #se incializa el conjunto
    def find(self,x): #se busca un representante de dicho conjunto
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,x,y): #se unen dos conjuntos cuando no estan conectados
        rx,ry=self.find(x),self.find(y)
        if rx==ry: return False #estan en el mismo conjunto
        if self.r[rx]<self.r[ry]: self.p[rx]=ry
        else:
            self.p[ry]=rx
            if self.r[rx]==self.r[ry]: self.r[rx]+=1
        return True

# Leer archivo y aristas
edges=[]
with open(archivo,"r",encoding="utf-8") as f:
    for l in f:
        p=[x.strip() for x in l.strip().split(",")]
        if len(p)!=3: continue
        a,b,w=p
        try:w=int(w)
        except: continue
        edges.append((a,b,w))
nodes=sorted({n for e in edges for n in e[:2]}, key=lambda s:s.lower()) #lista de aldeas

# Kruskal
uf=UF(); [uf.make(n) for n in nodes]
mst=[]
for u,v,w in sorted(edges,key=lambda x:x[2]): #se ordenan las aristas por su peso
    if uf.union(u,v): mst.append((u,v,w)) #agrega una arista si se conectan componentes

# BFS para organizar desde 'Peligros'
adj={n:[] for n in nodes} #grafo del MST
for u,v,w in mst: adj[u].append((v,w)); adj[v].append((u,w))

root="Peligros"; parent={root:None}; children={n:[] for n in nodes} #de quien recibe y envia cada aldea
edge_w={}; visitados={root}; cola=deque([root])
while cola: #desde peligros para organizar un arbol de mensajes
    act=cola.popleft()
    for v,w in adj[act]:
        if v not in visitados:
            visitados.add(v)
            parent[v]=act #v recibe el mensaje de act
            children[act].append(v) #act envia a v
            edge_w[v]=w
            cola.append(v)

# Mostrar resultados
print("\n=== LISTA ALFABÉTICA DE ALDEAS ===")
for n in nodes: print(n)
print("\n=== RUTAS DE COMUNICACIÓN (desde 'Peligros') ===")
print(f"{'Aldea':20s}|{'Recibe de':15s}|{'Envía a':40s}")
print("-"*80)
for n in nodes:
    r=parent[n] if parent[n] else "-"
    e=", ".join(children[n]) if children[n] else "-"
    print(f"{n:20s}|{r:15s}|{e:40s}")
print("\nDistancia total recorrida:", sum(w for _,_,w in mst),"leguas")