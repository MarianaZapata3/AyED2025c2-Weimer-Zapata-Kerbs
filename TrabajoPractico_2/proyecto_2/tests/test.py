# Se crea una base de datos
from modules.TemperaturaDB import Temperaturas_DB

# Se produce una instancia de la base de datos
db = Temperaturas_DB()

# Se carga el archivo de temperaturas
db.cargar_desde_archivo("data/muestras.txt")


# Consultas usando fechas completas del archivo muestras.txt
print("Temperatura del 10/01/2025:", db.devolver_temperatura("10/01/2025"))
print("Temperatura máxima entre 01/01/2025 y 20/01/2025:", db.max_temp_rango("01/01/2025", "20/01/2025"))
print("Temperatura mínima entre 01/01/2025 y 20/01/2025:", db.min_temp_rango("01/01/2025", "20/01/2025"))
print("Extremos entre 01/01/2025 y 30/01/2025:", db.temp_extremos_rango("01/01/2025", "30/01/2025"))
print("Listado completo de temperaturas entre 01/01/2025 y 30/01/2025:", db.devolver_temperaturas("01/01/2025", "30/01/2025"))

# Cantidad de muestras totales
print("Cantidad de muestras:", db.cantidad_muestras())

# Ejemplo de borrar una temperatura
db.borrar_temperatura("10/01/2025")
print("Cantidad de muestras después de borrar:", db.cantidad_muestras())