from matplotlib import pyplot as plt
from random import randint
import time
from ordenamientoseleccion import ordenamiento_por_seleccion
from ordenamientoburbuja import ordenamiento_burbuja
from ordenamientoradixsort import radix_sort

tamanos = [1, 10, 100, 200, 500, 700, 1000]

tiempos = {
    "seleccion": [],
    "burbuja": [],
    "radix": [],
    "sorted": []
}

for n in tamanos:
    datos = [randint(10000, 99999) for _ in range(n)]

    # Selección
    inicio = time.perf_counter()
    ordenamiento_por_seleccion(datos.copy())
    fin = time.perf_counter()
    tiempos["seleccion"].append(fin - inicio)

    # Burbuja
    inicio = time.perf_counter()
    ordenamiento_burbuja(datos.copy())
    fin = time.perf_counter()
    tiempos["burbuja"].append(fin - inicio)

    # Radix Sort
    inicio = time.perf_counter()
    radix_sort(datos.copy())
    fin = time.perf_counter()
    tiempos["radix"].append(fin - inicio)

    # Sorted
    inicio = time.perf_counter()
    sorted(datos)
    fin = time.perf_counter()
    tiempos["sorted"].append(fin - inicio)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos["seleccion"], marker='o', label="Selección O(n^2)")
plt.plot(tamanos, tiempos["burbuja"], marker='o', label="Burbuja O(n^2)")
plt.plot(tamanos, tiempos["radix"], marker='o', label="Radix Sort O(n·d)")
plt.plot(tamanos, tiempos["sorted"], marker='o', label="Python sorted O(n log n)")

plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de tiempos de ordenamiento")
plt.legend()
plt.grid()
plt.show()




