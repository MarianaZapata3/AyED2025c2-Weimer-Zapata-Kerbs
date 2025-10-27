import heapq

class ColaPrioridad:
    def __init__(self):
        self._heap = []
        self._contador = 0  # para mantener orden de llegada

    def encolar(self, item, prioridad):
        heapq.heappush(self._heap, (prioridad, self._contador, item))
        self._contador += 1 #suma un paciente a la cola por cada ciclo

    def desencolar(self):
        if self._heap:
            return heapq.heappop(self._heap)[2]
        return None

    def esta_vacia(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def ver_todos(self):
        return [x[2] for x in sorted(self._heap)]