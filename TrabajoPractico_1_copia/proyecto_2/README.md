# 🐍Proyecto “Mazo de Cartas”
Breve descripción del proyecto:

Este proyecto implementa un mazo de cartas usando una lista doblemente enlazada.
Permite:

Agregar cartas al inicio o al final del mazo.

Sacar cartas del mazo de manera controlada.

Obtener el tamaño del mazo y recorrerlo en orden.

Medir el desempeño de las operaciones y analizar su complejidad.
---
## 🏗Arquitectura General

El código está organizado de manera modular:

modulos/mazo.py → contiene la clase Mazo con todas las operaciones del TAD.

modulos/lista.py → lista doblemente enlazada utilizada internamente por el mazo.

main.py → ejecuta pruebas con mazos de distintos tamaños, verifica resultados y genera gráficas de tiempos de ejecución.

data/ → carpeta donde se guardan las gráficas generadas.

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
