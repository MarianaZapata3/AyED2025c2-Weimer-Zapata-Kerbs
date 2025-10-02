# -*- coding: utf-8 -*-

import time
import datetime
import random
import modules.pacientes as pac
from modules.coladeprioridad import ColaPrioridad

n = 20  # ciclos de simulación

cola_de_espera = ColaPrioridad()

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Crear paciente y encolarlo según riesgo
    paciente = pac.Paciente()
    print('Llega paciente:', paciente)
    cola_de_espera.encolar(paciente, paciente.get_riesgo())

    # Atender paciente en 50% de los casos
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        paciente_atendido = cola_de_espera.desencolar()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)

    print('\nPacientes que faltan atenderse:', len(cola_de_espera))
    for p in cola_de_espera.ver_todos():
        print('\t', p)
    
    print('-*-'*15)
    time.sleep(1)





