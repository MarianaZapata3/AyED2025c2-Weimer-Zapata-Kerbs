# tiempos.py
# -----------------------------------
# mide los tiempos de ejecución de
# selección, burbuja y shell

from random import randint
import time
from ordenamientoseleccion import ordenamiento_por_seleccion
from ordenamientoburbuja import ordenamiento_burbuja
from ordenamientoradixsort import radix_sort

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



