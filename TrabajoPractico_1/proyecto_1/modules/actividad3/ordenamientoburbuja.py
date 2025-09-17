from random import randint

# ---------------------------
# Ordenamiento burbuja clásico
# ---------------------------
def ordenamiento_burbuja(lista):
    # Bucle externo: controla las pasadas
    for num_pasadas in range(len(lista)-1, 0, -1):
        # Bucle interno: recorre hasta num_pasadas
        for j in range(num_pasadas):
            # Comparación entre elementos adyacentes
            if lista[j] > lista[j+1]:
                # Intercambio si están desordenados
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


# ----------------------------------
# Ordenamiento burbuja optimizado
# (se corta si la lista ya está ordenada)
# ----------------------------------
def ordenamiento_burbuja_corto(lista):
    intercambiado = True                 # bandera para detectar cambios
    num_pasadas = len(lista)-1           # cantidad de pasadas posibles
    while num_pasadas > 0 and intercambiado:
        intercambiado = False            # se reinicia en cada pasada
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                # Intercambio si están desordenados
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True     # hubo un cambio → la lista no está ordenada
        num_pasadas -= 1                 # en cada pasada el mayor queda al final
    return lista


# ---------------------------
# Bloque de prueba
# ---------------------------
if __name__ == '__main__':
    # Lista de prueba: mínimo 500 números de 5 dígitos
    N = 500
    datos = [randint(10000, 99999) for _ in range(N)]

    # Usamos burbuja clásico
    datos_ordenados = ordenamiento_burbuja(datos.copy())
    print("Primeros 20 ordenados (burbuja clásico):", datos_ordenados[:20])

    # Usamos burbuja optimizado
    datos_ordenados_corto = ordenamiento_burbuja_corto(datos.copy())
    print("Primeros 20 ordenados (burbuja corto):  ", datos_ordenados_corto[:20])






