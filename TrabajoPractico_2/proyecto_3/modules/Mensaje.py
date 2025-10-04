grafo = {}  # Aquí vamos a guardar las aldeas y sus vecinos

with open("data/aldeas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()  # Quitar espacios al inicio y fin
        if not linea:          # Ignorar líneas vacías
            continue
        partes = [p.strip() for p in linea.split(",")]  # Separar por coma
        if len(partes) != 3:   # Si no hay 3 partes, ignorar línea
            print(f"Línea inválida ignorada: {linea}")
            continue
        a1, a2, dist = partes
        dist = int(dist)        # Convertir la distancia a número
        # Guardar vecinos de forma bidireccional
        grafo.setdefault(a1, []).append((a2, dist))
        grafo.setdefault(a2, []).append((a1, dist))

origen = "Peligros"
visitados = set([origen])
heap = []

for vecino, peso in grafo[origen]:
    heapq.heappush(heap, (peso, origen, vecino))

mst = []
while heap and len(visitados) < len(grafo):
    peso, desde, hacia = heapq.heappop(heap)
    if hacia not in visitados:
        visitados.add(hacia)
        mst.append((desde, hacia, peso))
        for vecino, w in grafo[hacia]:
            if vecino not in visitados:
                heapq.heappush(heap, (w, hacia, vecino))
