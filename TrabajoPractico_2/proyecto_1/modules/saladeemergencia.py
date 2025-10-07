# -*- coding: utf-8 -*-

import time
import datetime
import random
import modules.pacientes as pac
from modules.coladeprioridad import ColaPrioridad

n = 20  # ciclos de simulación

cola_de_espera = ColaPrioridad() #se llama a la clase cola de prioridad

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente y se lo encola según el riesgo que es aleatorio
    paciente = pac.Paciente()
    print('Llega paciente:', paciente)
    cola_de_espera.encolar(paciente, paciente.get_riesgo())

    # Se atende un paciente en el 50% de los casos 
    #se tiene en cuenta que una clinica puede atender a un numero n de pacientes por dia (dependiendo las horas de trabajo)
    if random.random() < 0.5 and not cola_de_espera.esta_vacia(): #y si la cola no esta vacia
        paciente_atendido = cola_de_espera.desencolar()#quita al paciente que esta al inicio de la lista y que es de mayor riesgo
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        pass

    print('\nPacientes que faltan atenderse:', len(cola_de_espera))
    for p in cola_de_espera.ver_todos():
        print('\t', p)
    
    print('-*-'*15)
    time.sleep(1)





