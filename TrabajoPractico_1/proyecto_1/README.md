# 🐍Proyecto “Lista Doble Enlazada”
Breve descripción del proyecto:

Este proyecto implementa un Tipo Abstracto de Datos (TAD) de lista doblemente enlazada.
Permite:

Insertar elementos al inicio o al final de la lista.

Eliminar elementos de la lista.

Recorrer la lista hacia adelante o hacia atrás.

Medir la eficiencia de las operaciones y analizar su complejidad.

---
## 🏗Arquitectura General

El código está organizado de manera modular:

modulos/lista.py → contiene la clase ListaDobleEnlazada con todas las operaciones del TAD.

main.py → ejecuta pruebas con listas de distintos tamaños, verifica resultados y genera gráficas de tiempos de ejecución.

data/ → carpeta donde se guardan las gráficas generadas.

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
---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
