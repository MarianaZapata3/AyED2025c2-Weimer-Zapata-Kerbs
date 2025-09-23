# tiempos.py
# -----------------------------------
# mide los tiempos de ejecución de
# burbuja, quicksort y radix sort

from random import randint
import time
import matplotlib.pyplot as plt
import sys
import os

#Agregar la carpeta actual al path
#para que Python encuentre los módulos

sys.path.append(os.path.dirname(__file__))

#Importar algoritmos
from ordenamientoburbuja import ordenamiento_burbuja
from ordenamientoquicksort import quicksort
from ordenamientoradixsort import radix_sort

#Función para medir tiempos

def medir_tiempos(metodo, tamanos):
    tiempos = []
    for n in tamanos:
        datos = [randint(10000, 99999) for _ in range(n)]
        inicio = time.perf_counter()
        metodo(datos.copy())
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        print(f"{metodo.__name__} n={n}: {fin - inicio:.6f}s")
    return tiempos

#Ejecución principal

if __name__ == '__main__':
    tamanos = [1, 10, 50, 100, 200, 500, 700, 1000]

    tiempos_burbuja = medir_tiempos(ordenamiento_burbuja, tamanos)
    tiempos_quicksort = medir_tiempos(quicksort, tamanos)
    tiempos_radix = medir_tiempos(radix_sort, tamanos)
    tiempos_sorted = medir_tiempos(sorted, tamanos)

    #Graficar resultados

    plt.figure(figsize=(10,6))
    plt.plot(tamanos, tiempos_burbuja, marker='o', label='Burbuja')
    plt.plot(tamanos, tiempos_quicksort, marker='s', label='Quicksort')
    plt.plot(tamanos, tiempos_radix, marker='^', label='Radix Sort')
    plt.plot(tamanos, tiempos_sorted, marker='x', label='Python sorted')
    plt.xlabel("Tamaño de lista")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()

