<<<<<<< HEAD
# 🐍Proyecto “Lista Doble Enlazada”
Breve descripción del proyecto:

Este proyecto implementa un Tipo Abstracto de Datos (TAD) de lista doblemente enlazada.
Permite:

Insertar elementos al inicio o al final de la lista.

Eliminar elementos de la lista.

Recorrer la lista hacia adelante o hacia atrás.

Medir la eficiencia de las operaciones y analizar su complejidad.
=======
# 🐍Proyecto “Estructuras y Algoritmos de Cartas”

Breve descripción del proyecto:

Este proyecto implementa estructuras de datos y algoritmos para manejar listas y mazos de cartas usando listas doblemente enlazadas.
Permite:

Crear y manipular mazos de cartas (agregar arriba/abajo, sacar cartas, recorrer).

Implementar y probar listas doblemente enlazadas con distintas operaciones.

Medir tiempos de ejecución y analizar la complejidad de las operaciones.

Generar gráficas que muestran el comportamiento de cada estructura/algoritmo
>>>>>>> 3c1e468 (agregado)

---
## 🏗Arquitectura General

<<<<<<< HEAD
El código está organizado de manera modular:

modulos/lista.py → contiene la clase ListaDobleEnlazada con todas las operaciones del TAD.

main.py → ejecuta pruebas con listas de distintos tamaños, verifica resultados y genera gráficas de tiempos de ejecución.

data/ → carpeta donde se guardan las gráficas generadas.
=======
El proyecto está organizado en módulos y una aplicación principal:

modulos/ → contiene los TADs y clases principales:

lista.py → implementación de la lista doblemente enlazada (Ejercicio 1)

mazo.py → implementación del mazo de cartas (Ejercicio 2)

simulacion.py → medición de tiempos y gráficos para análisis de complejidad (Ejercicio 3)

main.py → ejecuta los tres ejercicios, mide tiempos y genera gráficos.

data/ → carpeta donde se guardan las gráficas generadas por Python.
>>>>>>> 3c1e468 (agregado)

docs/ → carpeta donde se encuentra el informe completo en PDF.

Las gráficas de los resultados están disponibles en la carpeta data
 del proyecto.
El informe completo está disponible en la carpeta docs
 del proyecto.

 Ejercicio 1 – Lista Doble Enlazada

Implementa un TAD de lista doblemente enlazada.

Operaciones principales: insertar al inicio o al final, eliminar nodos, recorrer adelante o atrás.

Se realizaron pruebas con listas de 500 elementos aleatorios para verificar que todas las operaciones funcionan correctamente.

Se midieron tiempos de ejecución para cada operación y se generaron gráficas comparando los resultados con la complejidad teórica:

Inserción/Eliminación en extremos → O(1)

Búsqueda/Recorrido → O(n)

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
<<<<<<< HEAD
=======

>>>>>>> 3c1e468 (agregado)
---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
