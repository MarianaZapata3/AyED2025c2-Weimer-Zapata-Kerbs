from matplotlib import pyplot as plt
from random import randint
import time
from modules.actividad3.ordenamientoburbuja import ordenamiento_burbuja

# tamaños de listas a probar
tamanos = [1, 10, 100, 200, 500, 700, 1000]

# listas para guardar los tiempos de cada método
tiempos_burbuja = []
tiempos_quicksort = []
tiempos_radix = []
tiempos_sorted = []

# figsize es el tamaño de la figura en pulgadas (width, height)
plt.figure(figsize=(10, 6))

for n in tamanos:
    # lista de n números aleatorios de 5 dígitos
    datos = [randint(10000, 99999) for _ in range(n)]

    # --- Burbuja ---
    inicio = time.perf_counter()
    ordenamiento_burbuja(datos.copy())
    fin = time.perf_counter()
    tiempos_burbuja.append(fin - inicio)

    # --- quicksort ---
    

    # --- Radix Sort ---
    

    # --- Sorted (built-in) ---
    inicio = time.perf_counter()
    sorted(datos)
    fin = time.perf_counter()
    tiempos_sorted.append(fin - inicio)

# Graficar los resultados
plt.plot(tamanos, tiempos_burbuja, marker='o', label="Burbuja O(n^2)")
plt.plot(tamanos, tiempos_sorted, marker='o', label="Python sorted O(n log n)")

plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ordenamiento')
plt.legend()
plt.grid()
plt.show()
