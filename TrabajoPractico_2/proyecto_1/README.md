<<<<<<< HEAD

## 🐍 Proyecto “Sala de Emergencias”
🏥 Breve descripción del proyecto

Este proyecto implementa un sistema de triaje que simula la atención de pacientes en una sala de emergencias.
Cada paciente se clasifica según su nivel de riesgo clínico:

1: Crítico

2: Moderado

3: Bajo

El objetivo principal es gestionar la atención prioritaria de los pacientes de acuerdo con su nivel de riesgo, garantizando que el sistema atienda primero a quienes requieren asistencia urgente.

Para ello, se desarrolla una estructura de datos genérica basada en una cola de prioridad (Priority Queue), que permite insertar y eliminar elementos según su prioridad.
Si dos pacientes tienen el mismo nivel de riesgo, se utiliza un segundo criterio de desempate: el orden de llegada.

---
## 🏗Arquitectura General
El código está organizado de manera modular:

modulos/cola_prioridad.py → Implementa el TAD genérico de cola de prioridad utilizando un montículo binario (heap).

modulos/paciente.py → Define la clase Paciente, con atributos como nombre, riesgo y número de llegada.

simulacion.py → Contiene la simulación del proceso de triaje y atención de pacientes.

main.py → Ejecuta el programa principal, mostrando el orden de atención de los pacientes.

data/ → Carpeta donde pueden guardarse resultados o registros de la simulación.

docs/ → Carpeta donde se encuentra el informe completo del proyecto en formato PDF.

Complejidad Teorica:

Inserción → O(log n)

Eliminación → O(log n)

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
