# orden de complejidad del ordenamiento burbuja es O(n^2)
# en el mejor caso es O(n) y en el peor caso es O(n^2)
# el mejor caso se da cuando la lista está ordenada
# el peor caso se da cuando la lista está ordenada en orden inverso

# el ordenamiento burbuja es un algoritmo de ordenamiento simple
# que compara cada elemento de la lista con el siguiente y los intercambia si están en el orden incorrecto
# el algoritmo se repite varias veces
# en cada pasada se coloca el elemento más grande en su lugar correcto
# el algoritmo se detiene cuando no se realizan intercambios en una pasada

# orden de complejidad del ordenamiento burbuja corto es O(n^2)

from random import randint

def ordenamiento_burbuja(lista):
    for num_pasadas in range(len(lista)-1, 0, -1):
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenamiento_burbuja_corto(lista):
    intercambiado = True
    num_pasadas = len(lista)-1
    while num_pasadas > 0 and intercambiado:
        intercambiado = False
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        num_pasadas -= 1
    return lista

if __name__ == '__main__':
    # Lista de prueba: mínimo 500 números de 5 dígitos
    N = 500
    datos = [randint(10000, 99999) for _ in range(N)]
    datos_ordenados = ordenamiento_burbuja(datos.copy())
    print("Primeros 20 ordenados (burbuja):", datos_ordenados[:20])






