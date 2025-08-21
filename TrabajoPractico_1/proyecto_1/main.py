lista = ListaDobleEnlazada()

print("¿Está vacía?:", lista.esta_vacia())  # True

lista.agregar_al_inicio(10)
lista.agregar_al_final(20)
lista.agregar_al_final(30)

print("Lista:", lista)  # 10 <-> 20 <-> 30

lista.insertar(5, 0)   # al inicio
lista.insertar(25, 3)  # en el medio
lista.insertar(40)     # al final

print("Lista después de insertar:", lista)
# 5 <-> 10 <-> 20 <-> 25 <-> 30 <-> 40

print("Tamaño:", len(lista))  # 6
