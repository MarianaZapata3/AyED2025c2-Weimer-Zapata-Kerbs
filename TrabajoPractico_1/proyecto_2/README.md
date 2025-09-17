# 🐍Proyecto “Estructuras y Algoritmos de Cartas”

Breve descripción del proyecto:

Este proyecto implementa estructuras de datos y algoritmos para manejar listas y mazos de cartas usando listas doblemente enlazadas.
Permite:

Crear y manipular mazos de cartas (agregar arriba/abajo, sacar cartas, recorrer).

Implementar y probar listas doblemente enlazadas con distintas operaciones.

Medir tiempos de ejecución y analizar la complejidad de las operaciones.

Generar gráficas que muestran el comportamiento de cada estructura/algoritmo

---
## 🏗Arquitectura General

El proyecto está organizado en módulos y una aplicación principal:

modulos/ → contiene los TADs y clases principales:

lista.py → implementación de la lista doblemente enlazada (Ejercicio 1)

mazo.py → implementación del mazo de cartas (Ejercicio 2)

simulacion.py → medición de tiempos y gráficos para análisis de complejidad (Ejercicio 3)

main.py → ejecuta los tres ejercicios, mide tiempos y genera gráficos.

data/ → carpeta donde se guardan las gráficas generadas por Python.

docs/ → carpeta donde se encuentra el informe completo en PDF.

Las gráficas de los resultados están disponibles en la carpeta data
 del proyecto.
El informe completo está disponible en la carpeta docs
 del proyecto.

Ejercicio 2 – Mazo de Cartas

Implementa un mazo de cartas usando la lista doblemente enlazada.

Operaciones principales:

poner_carta_arriba → O(1)

poner_carta_abajo → O(1)

sacar_carta_arriba → O(1)

__len__ → O(1)

__str__ → O(n)

Se realizaron pruebas con mazos de 500 cartas aleatorias.

Se verificó que las operaciones mantienen el orden esperado y que los resultados son correctos.

Se pueden generar gráficas de la evolución del tamaño del mazo durante la ejecución.
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
