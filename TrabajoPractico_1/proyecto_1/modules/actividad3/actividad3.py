
#Prueba de la act3

import random
import time
import matplotlib.pyplot as plt

lista=[random.randint(1,1000) for _ in range(500)]

#Burbuja
def OrdenamientoBurbuja(lista):
    for numPasada in range(len(lista) - 1, 0, -1):
        for i in range(numPasada):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


#HAY QUE ARREGLAR ESTE, PORQUE NO TIENE QUE SER SELECCION, ES QUICKSORT
def OrdenamientoPorSeleccion(lista):
    for LlenarRanura in range(len(lista)-1,0,-1):
        PosicionMayor=0
        for ubicacion in range(1,LlenarRanura+1):
            if lista[ubicacion]>lista[PosicionMayor]:
                PosicionMayor=ubicacion
        
        temp=lista[LlenarRanura]
        lista[LlenarRanura]=lista[PosicionMayor]
        lista[PosicionMayor]=temp
OrdenamientoPorSeleccion(lista)
print(lista)


#Residuo
def OrdenamientoPorResiduo(lista):
    num_mayor = max(lista)
    exponente = 1

    while num_mayor // exponente > 0:
        # Crear buckets (0-9)
        buckets = [[] for _ in range(10)]

        # Clasificar los elementos en el bucket correspondiente
        for num in lista:
            indice = (num // exponente) % 10
            buckets[indice].append(num)

        # Reconstruir la lista a partir de los buckets
        lista = [num for bucket in buckets for num in bucket]

        exponente *= 10

    return lista




# ---------------------------
# MEDICIÓN DE TIEMPOS
# ---------------------------
tamanos = [100, 200, 300, 500, 1000]

tiempos_burbuja=[]
tiempos_seleccion=[]
tiempos_residuo=[]
tiempos_sorted = []

for n in tamanos:
    lista = [random.randint(10000, 99999) for _ in range(n)]

    # Burbuja
    inicio = time.time()
    OrdenamientoBurbuja(lista[:])
    fin = time.time()
    tiempos_burbuja.append(fin - inicio)

    # Quicksort
    inicio = time.time()
    OrdenamientoPorSeleccion(lista[:])
    fin = time.time()
    tiempos_seleccion.append(fin - inicio)

    # Residuo
    inicio = time.time()
    OrdenamientoPorResiduo(lista[:])
    fin = time.time()
    tiempos_residuo.append(fin - inicio)

    # Built-in sorted
    inicio = time.time()
    sorted(lista[:])
    fin = time.time()
    tiempos_sorted.append(fin - inicio)


# ---------------------------
# PRUEBAS DE FUNCIONAMIENTO
# ---------------------------
lista = [random.randint(10000, 99999) for _ in range(500)]
print("Lista original (primeros 20):", lista[:20])
print("Burbuja:", OrdenamientoBurbuja(lista[:])[:20])
print("Quicksort:", OrdenamientoPorResiduo(lista[:])[:20])
print("Residuo:", OrdenamientoPorResiduo(lista[:])[:20])



# ---------------------------
# GRAFICAR RESULTADOS
# ---------------------------
plt.plot(tamanos, tiempos_burbuja, marker="o", label="Burbuja")
plt.plot(tamanos, tiempos_seleccion, marker="o", label="Seleccion")
plt.plot(tamanos, tiempos_residuo, marker="o", label="Radix (residuo)")
plt.plot(tamanos, tiempos_sorted, marker="o", label="sorted (built-in)")

plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid(True)
plt.show()
