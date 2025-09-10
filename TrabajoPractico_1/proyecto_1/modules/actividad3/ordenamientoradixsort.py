# orden de complejidad del ordenamiento shell es O(n^2)
# en el mejor caso es O(n log n) y en el peor caso es O(n^2)
# el mejor caso se da cuando la lista está casi ordenada
# el peor caso se da cuando la lista está ordenada en orden inverso

# el ordenamiento shell es una variante del ordenamiento por inserción
# que divide la lista en sublistas más pequeñas según un valor de brecha (gap)
# luego aplica ordenamiento por inserción dentro de esas sublistas
# reduciendo la brecha progresivamente hasta llegar a 1

from random import randint

def counting_sort_por_digito(lista, digito_exp):
    n = len(lista)
    salida = [0] * n
    cuenta = [0] * 10  # base decimal 0-9

    for numero in lista:
        indice = (numero // digito_exp) % 10
        cuenta[indice] += 1

    for i in range(1, 10):
        cuenta[i] += cuenta[i - 1]

    for i in range(n - 1, -1, -1):
        numero = lista[i]
        indice = (numero // digito_exp) % 10
        salida[cuenta[indice] - 1] = numero
        cuenta[indice] -= 1

    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10
    return lista

if __name__ == "__main__":
    N = 500
    datos = [randint(10000, 99999) for _ in range(N)]
    print("Primeros 20 ordenados (radix sort):", radix_sort(datos.copy())[:20])
