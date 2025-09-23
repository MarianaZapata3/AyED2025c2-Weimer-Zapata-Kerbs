def radix_sort(lista):
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10
    return lista

def counting_sort_por_digito(lista, exp):
    n = len(lista)
    salida = [0]*n
    conteo = [0]*10
    
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1
    
    for i in range(1, 10):
        conteo[i] += conteo[i-1]
    
    i = n-1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice]-1] = lista[i]
        conteo[indice] -= 1
        i -= 1
    
    for i in range(n):
        lista[i] = salida[i]
