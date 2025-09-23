from random import randint

# ----------------------------------
# Ordenamiento burbuja optimizado
# (se corta si la lista ya está ordenada)
# ----------------------------------
def ordenamiento_burbuja(lista):
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

    # Usamos burbuja 
    datos_ordenados = ordenamiento_burbuja(datos.copy())
    print("Primeros 20 ordenados (burbuja clásico):", datos_ordenados[:20])







