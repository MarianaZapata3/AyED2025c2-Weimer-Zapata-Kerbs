# 🐍Proyecto “Temperaturas_DB”
Breve descripción del proyecto

El proyecto “Temperaturas_DB” implementa una base de datos en memoria para registrar y consultar temperaturas de la Tierra asociadas a fechas específicas.
Cada registro está compuesto por:

Temperatura (°C) — valor numérico flotante.

Fecha de registro — ingresada como cadena "dd/mm/aaaa", y almacenada internamente como objeto datetime para facilitar comparaciones y ordenamiento.

El almacenamiento de las mediciones se realiza mediante un árbol AVL, una estructura de datos auto-balanceada que mantiene sus elementos ordenados y garantiza eficiencia en las operaciones de búsqueda, inserción y eliminación.
Esto permite que el científico Kevin Kelvin realice consultas rápidas incluso cuando el volumen de datos crece significativamente.

---
## 🏗Arquitectura General

El código está organizado en módulos y clases:

modulos/nodo_avl.py → Implementa el nodo del árbol AVL, con atributos fecha, temperatura, altura, izq, der.

modulos/arbol_avl.py → Implementa las operaciones del árbol AVL: inserción, rotaciones, eliminación y recorrido.

temperaturas_db.py → Define la clase principal Temperaturas_DB, que actúa como interfaz de la base de datos y utiliza internamente un árbol AVL.

lector_archivo.py → Contiene funciones para leer archivos de muestras (por ejemplo, CSV o TXT) y cargar automáticamente los registros a la base de datos.

main.py → Permite probar todas las funcionalidades: inserción de muestras, consultas por rango, eliminación y conteo.

data/ → Carpeta donde se almacenan archivos de entrada o resultados de consultas.

docs/ → Carpeta donde se encuentra el informe del proyecto.

Complejidad Teórica:

guardar_temperatura → O(log n)

devolver_temperatura → O(log n)

max_temp_rango → O(k + log n)

min_temp_rango → O(k + log n)

temp_extremos_rango → O(k + log n) 

borrar_temperatura → O(log n)

devolver_temperaturas → O(k + log n)

cantidad_muestras → O(1) 

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Zapata Mariana Gabriela
- Weimer Valentin
- Kerbs Javier
---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
