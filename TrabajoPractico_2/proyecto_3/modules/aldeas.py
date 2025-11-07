#Usa Grafo y ColaPrioridad del ejercicio anterior para encontrar MST y rutas de comunicación

from Grafo import cargar_grafo_desde_archivo
from ColadePrioridad import ColaPrioridad

#Algoritmo de Prim
def prim(grafo, inicio):
    visitados = []       #lista que guarda los vertices visitados
    mst = []             #lista que contendrá las aristas del arbol de expansión mínima
    cola = ColaPrioridad() #cola de prioridad que permite seleccionar la arista de menor peso
    
    v_inicio = grafo.obtener_vertice(inicio)  #se obtiene el vertice inicial a partir del nombre
    if v_inicio is None:       #si el vértice no existe en el grafo, no se puede continuar
        return None
    
    visitados.append(v_inicio)  #se marca el vertice inicial como visitado
    
    #Se encolan las aristas desde el inicio
    for destino, peso in v_inicio.adyacentes:
        cola.encolar((v_inicio, destino, peso), peso) #encola tupla (origen, destino, peso) con prioridad = peso
    
    #mientras que haya aristas en la cola de prioridad 
    while not cola.esta_vacia():
        origen, destino, peso = cola.desencolar() #se desencola la arista de menor peso
        if destino not in visitados:              #si el destino aun no fue visitado
            visitados.append(destino)             #se marca como visitado
            mst.append((origen.nombre, destino.nombre, peso))  #se agrega la arista al arbol de expansion minima
            #se encolan las aristas que salen del nuevo vertice
            for vecino, p in destino.adyacentes:
                if vecino not in visitados:    #se evita volver a vértices ya visitados
                    cola.encolar((destino, vecino, p), p)
    
    return mst   #se retorna la lista de aristas que forman el árbol de expansión mínima


#construccion de los diccionarios de padres e hijos a partir del MST obtenido
def construir_arbol(mst, inicio):
    padre = {inicio: None}              #diccionario que almacena el padre de cada aldea
    hijos = {}                          #diccionario que almacena los hijos de cada aldea
    
    #se recorre cada arista (u, v) del árbol MST
    for u, v, _ in mst:
        hijos.setdefault(u, []).append(v)  #agregamos v como hijo de u
        hijos.setdefault(v, []).append(u)  #y u como hijo de v (ya que es un árbol no dirigido)
    
    visitados = [inicio]      #lista de aldeas visitadas
    cola = [inicio]           #cola para recorrer el árbol en anchura (BFS)
    
    #se recorre el árbol para construir la jerarquía padre-hijo
    while cola:
        actual = cola.pop(0)           #se saca el primer elemento de la cola
        for vecino in hijos.get(actual, []):  #se recorren los vecinos del nodo actual
            if vecino not in visitados:       #si aún no fue visitado
                visitados.append(vecino)      #se marca como visitado
                padre[vecino] = actual        #y se guarda su padre
                cola.append(vecino)           #luego se agrega a la cola para seguir recorriendo
    return padre, hijos                      #retornamos ambos diccionarios



if __name__ == "__main__":

    grafo = cargar_grafo_desde_archivo("aldeas.txt")   #se carga el grafo con las aldeas y sus conexiones

    #aplicamos el algoritmo de Prim partiendo desde la aldea "Peligros"
    mst = prim(grafo, "Peligros")
    #construimos los diccionarios de padres e hijos a partir del arbol de minimos
    padre, hijos = construir_arbol(mst, "Peligros")
    
    #se muestran las aldeas ordenadas alfabéticamente
    print("\nAldeas ordenadas alfabéticamente:")
    for v in sorted(grafo.vertices, key=lambda x: x.nombre.lower()):
        print(" -", v.nombre)
    
    #se muestra la tabla de rutas de comunicación entre aldeas
    print("\nRutas de comunicación (desde 'Peligros'):")
    print(f"{'Aldea':20s}|{'Recibe de':15s}|{'Envía a':40s}")
    print("-"*80)
    
    #se recorre cada aldea en orden alfabético
    for v in sorted(grafo.vertices, key=lambda x: x.nombre.lower()):
        n = v.nombre                              #nombre de la aldea actual
        recibe = str(padre.get(n, "-"))           #aldea de la que recibe (o "-" si no tiene padre)
        
        #se buscan las aldeas que reciben mensajes desde esta (hijos)
        envia = [h for h, p in padre.items() if p == n]
        envia_str = ", ".join(sorted(envia)) if envia else "-"  # Unimos en una cadena o mostramos "-"
        
        #se muestra fila correspondiente a esta aldea
        print(f"{n:20s}|{recibe:15s}|{envia_str:40s}")

    #y se calcula la distancia total recorrida por todas las palomas (suma de los pesos del MST)
    dist_total = sum(p for _, _, p in mst)
    print(f"\nDistancia total recorrida por todas las palomas: {dist_total} leguas")