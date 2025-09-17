# mazo.py
from modules.actividad1.lista_doble1 import ListaDobleEnlazada  # tu implementación del TP1

class DequeEmptyError(Exception):
    """Se lanza si se intenta sacar carta de un mazo vacío"""
    pass

class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()  # usa lista doblemente enlazada

    def poner_carta_arriba(self, carta):
        """Agrega carta al inicio del mazo"""
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Agrega carta al final del mazo"""
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Extrae carta del inicio del mazo"""
        if self._cartas.esta_vacia():
            raise DequeEmptyError("No se puede sacar carta de un mazo vacío")
        carta = self._cartas.extraer(0)  # extrae el nodo de la posición 0
        if mostrar:
            print(f"Se sacó: {carta}")
        return carta

    def __len__(self):
        return self._cartas.tamanio

    def __str__(self):
        """Muestra todas las cartas del mazo"""
        actual = self._cartas.cabeza
        lista = []
        while actual:
            lista.append(str(actual.dato))
            actual = actual.siguiente
        return ' '.join(lista)
