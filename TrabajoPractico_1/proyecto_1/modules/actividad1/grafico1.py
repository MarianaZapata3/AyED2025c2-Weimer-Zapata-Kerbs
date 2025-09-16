#grafico para actividad 1
import time
import matplotlib.pyplot as plt
from lista_doble1 import ListaDobleEnlazada  # tu implementación

if __name__ == "__main__":
    import time
    import matplotlib.pyplot as plt
    import random

    # Tamaños de prueba
    N_list = list(range(100, 10001, 500))
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for N in N_list:
        lde = ListaDobleEnlazada()
        for i in range(N):
            lde.agregar_al_final(random.randint(0, 1000))

        start = time.perf_counter()
        _ = len(lde)
        end = time.perf_counter()
        tiempos_len.append(end - start)

        start = time.perf_counter()
        _ = lde.copiar()
        end = time.perf_counter()
        tiempos_copiar.append(end - start)

        start = time.perf_counter()
        lde.invertir()
        end = time.perf_counter()
        tiempos_invertir.append(end - start)

    plt.figure(figsize=(10,6))
    plt.plot(N_list, tiempos_len, marker='o', label='len()')
    plt.plot(N_list, tiempos_copiar, marker='s', label='copiar()')
    plt.plot(N_list, tiempos_invertir, marker='^', label='invertir()')
    plt.xlabel('Número de elementos N')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución vs tamaño de lista')
    plt.legend()
    plt.grid(True)
    plt.show()