# -*- coding: utf-8 -*-
from random import randint, choices
import time

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]  # 1 = crítico, 2 = moderado, 3 = bajo
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    contador = 0  # sirve para asegurar orden de llegada

    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.timestamp = Paciente.contador
        Paciente.contador += 1 #agrega a la fila al paciente cuando no es de prioridad o hay otro de prioridad atendiendose

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo #riesgo del paciente
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} -> {self.__riesgo}-{self.__descripcion} (llegada {self.timestamp})"