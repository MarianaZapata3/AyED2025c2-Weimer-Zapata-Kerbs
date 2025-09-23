from matplotlib import pyplot as plt
from random import randint
import time
from modules.ordenamientoburbuja import ordenamiento_burbuja

tamanos = [1, 10, 100, 200, 500, 700, 1000]

tiempos = {
    "quicksort": [],
    "burbuja": [],
    "radix": [],
    "sorted": []
}

for n in tamanos:
    datos = [randint(10000, 99999) for _ in range(n)]

    # Quicksort
    

    # Burbuja
    inicio = time.perf_counter()
    ordenamiento_burbuja(datos.copy())
    fin = time.perf_counter()
    tiempos["burbuja"].append(fin - inicio)

    # Radix Sort


    # Sorted
    inicio = time.perf_counter()
    sorted(datos)
    fin = time.perf_counter()
    tiempos["sorted"].append(fin - inicio)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos["burbuja"], marker='o', label="Burbuja O(n^2)")
plt.plot(tamanos, tiempos["sorted"], marker='o', label="Python sorted O(n log n)")

plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de tiempos de ordenamiento")
plt.legend()
plt.grid()
plt.show()








