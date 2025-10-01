# -*- coding: utf-8 -*-
import time
import datetime
import random
import modules.pacientes as pac
from modules.coladeprioridad import ColaPrioridad

n = 20  # cantidad total de pacientes que llegarán

cola_de_espera = ColaPrioridad()
pacientes_llegados = 0  # contador de pacientes que ya llegaron

while pacientes_llegados < n or not cola_de_espera.esta_vacia():
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Crear paciente y encolarlo según riesgo si aún no llegaron todos
    if pacientes_llegados < n:
        paciente = pac.Paciente()
        pacientes_llegados += 1
        print('Llega paciente:', paciente)
        cola_de_espera.encolar(paciente, paciente.get_riesgo())

    # Atender paciente en 50% de los casos
    if not cola_de_espera.esta_vacia() and random.random() < 0.5:
        paciente_atendido = cola_de_espera.desencolar()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)

    print('\nPacientes que faltan atenderse:', len(cola_de_espera))
    for p in cola_de_espera.ver_todos():
        print('\t', p)
    
    print('-*-'*15)
    time.sleep(1)

    



