from random import randint

#Ordenamiento port sorted()

def ordenamiento_sorted(lista):
    #sorted() devuelve una nueva lista ordenada sin modificar la original
    return sorted(lista)

#Prueba

if __name__ == '__main__':
    #Lista de prueba: mínimo 500 números de 5 dígitos
    N = 500
    datos = [randint(10000, 99999) for _ in range(N)]

    #Usamos sorted()
    datos_ordenados = ordenamiento_sorted(datos.copy())
    print("Primeros 20 ordenados (sorted()):", datos_ordenados[:20])

    #Verificación
    print("¿Lista ordenada correctamente?", all(datos_ordenados[i] <= datos_ordenados[i+1] for i in range(len(datos_ordenados)-1)))
