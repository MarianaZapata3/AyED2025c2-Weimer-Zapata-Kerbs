from random import randint, choices

#módulo que define la clase Paciente y genera datos aleatorios para simular

#listas de los posibles pacientes, niveles de riesgo y probabilidad de paciente
nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']
niveles_de_riesgo = [1, 2, 3]  # 1 = crítico, 2 = moderado, 3 = bajo
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6] #probabilidades de aparición de cada tipo de paciente


#clase paciente que cuenta cuántos pacientes se generaron
class Paciente:
    #sirve para asignar un "orden de llegada" global
    contador = 0
    #funcion que crea un paciente y nivel de riesgo aleatorios
    def __init__(self):
        """Constructor: crea un paciente con datos y nivel de riesgo aleatorios."""
        n = len(nombres)  # cantidad total de nombres disponibles
        #selecciona nombre y apellido al azar
        self.__nombre = nombres[randint(0, n - 1)]
        self.__apellido = apellidos[randint(0, n - 1)]
        #asigna un nivel de riesgo según las probabilidades definidas
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        #traduce el nivel numérico a una descripcion
        self.__descripcion = descripciones_de_riesgo[self.__riesgo - 1]
        #orden de llegada para usar en la cola
        self.timestamp = Paciente.contador
        Paciente.contador += 1  # incrementa el contador global
    
    
    #métodos “get” para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo #riesgo del paciente
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    #representación en texto del paciente
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} -> {self.__riesgo}-{self.__descripcion} (llegada {self.timestamp})"
    

