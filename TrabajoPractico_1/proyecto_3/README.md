# 🐍Proyecto “Comparación de Algoritmos de Ordenamiento”
Breve descripción del proyecto

Este proyecto implementa y compara distintos algoritmos de ordenamiento en Python:

Burbuja (Bubble Sort)

Quicksort

Radix Sort (Ordenamiento por residuos)

Se generan listas aleatorias de números de cinco dígitos (mínimo 500 elementos) y se mide el tiempo de ejecución de cada algoritmo para listas de tamaño entre 1 y 1000.
Además, se compara con la función built-in de Python sorted().

---🏗 Arquitectura General

modulos/ordenamiento.py → implementación de los algoritmos: burbuja, quicksort y radix.

main.py → genera listas de prueba, mide tiempos, genera gráficas y compara los algoritmos.

data/ → carpeta donde se guardan las gráficas de tiempos de ejecución.

docs/ → carpeta donde se encuentra el informe completo en PDF.

Las gráficas de resultados están disponibles en data
.
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
