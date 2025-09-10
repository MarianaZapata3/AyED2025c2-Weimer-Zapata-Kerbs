# orden de complejidad del ordenamiento por selección es O(n^2)
# en todos los casos (mejor, peor y promedio) su complejidad es O(n^2)
# ya que siempre recorre toda la lista buscando el mínimo o máximo

# el ordenamiento por selección funciona buscando en cada pasada
# el elemento más grande (o más pequeño) y colocándolo en su lugar correcto.
# en cada iteración, la parte ordenada de la lista crece de a un elemento.

from random import randint

def ordenamiento_por_seleccion(lista):
    for llenar_ranura in range(len(lista) - 1, 0, -1):
        posicion_del_mayor = 0
        for ubicacion in range(1, llenar_ranura + 1):
            if lista[ubicacion] > lista[posicion_del_mayor]:
                posicion_del_mayor = ubicacion
        lista[llenar_ranura], lista[posicion_del_mayor] = lista[posicion_del_mayor], lista[llenar_ranura]
    return lista

if __name__ == '__main__':
    N = 500
    datos = [randint(10000, 99999) for _ in range(N)]
    datos_ordenados = ordenamiento_por_seleccion(datos.copy())
    print("Primeros 20 ordenados (selección):", datos_ordenados[:20])



