# test_tiempos.py
# -----------------------------------
# mide y grafica los tiempos de ejecución de los algoritmos:
# selección, burbuja y shell

from random import randint
from modules.actividad3.ordenamientoburbuja import ordenamiento_burbuja
from modules.actividad3.ordenamientoseleccion import ordenamiento_por_seleccion
from modules.actividad3.ordenamientoradixsort import radix_sort

# Generar lista de prueba con 500 números aleatorios de 5 dígitos
N = 500
datos = [randint(10000, 99999) for _ in range(N)]

# Copias para cada método
datos_burbuja = datos.copy()
datos_seleccion = datos.copy()
datos_radix = datos.copy()
datos_sorted = datos.copy()

# --- Ordenamiento Burbuja ---
resultado_burbuja = ordenamiento_burbuja(datos_burbuja)
print("Burbuja - primeros 20:", resultado_burbuja[:20])

# --- Ordenamiento Selección ---
resultado_seleccion = ordenamiento_por_seleccion(datos_seleccion)
print("Selección - primeros 20:", resultado_seleccion[:20])

# --- Ordenamiento Radix Sort ---
resultado_radix = radix_sort(datos_radix)
print("Radix Sort - primeros 20:", resultado_radix[:20])

# --- Función built-in sorted ---
resultado_sorted = sorted(datos_sorted)
print("Sorted - primeros 20:", resultado_sorted[:20])

# --- Verificar que todos los resultados sean iguales ---
if resultado_burbuja == resultado_seleccion == resultado_radix == resultado_sorted:
    print("✅ Todos los métodos se ordenaron correctamente")
else:
    print("❌ Hay diferencias entre los métodos")
