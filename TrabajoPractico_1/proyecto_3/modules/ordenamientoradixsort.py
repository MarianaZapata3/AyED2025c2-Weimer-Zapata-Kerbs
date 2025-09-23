from random import randint

#Ordenamiento  por radix sort

def counting_sort_por_digito(lista, digito):
    
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10  #Dígitos 0-9

    #Contar ocurrencias del dígito actual
    for numero in lista:
        indice = (numero // digito) % 10
        conteo[indice] += 1

    #Sumarización del conteo
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    #Construir la lista ordenada según el dígito
    i = n - 1
    while i >= 0:
        indice = (lista[i] // digito) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    #Copiar resultados a la lista original
    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    #Encontrar el número máximo para determinar la cantidad de dígitos
    max_num = max(lista)

    #Ordenar por cada dígito: unidades, decenas, centenas, ...
    digito = 1
    while max_num // digito > 0:
        counting_sort_por_digito(lista, digito)
        digito *= 10

    return lista

#Prueba

if __name__ == '__main__':
    #Lista de prueba: mínimo 500 números de 5 dígitos
    N = 500
    datos = [randint(10000, 99999) for _ in range(N)]

    #Usamos Radix Sort
    datos_ordenados = radix_sort(datos.copy())
    print("Primeros 20 ordenados (Radix Sort):", datos_ordenados[:20])
