# Práctica Experimental: Concurrencia en Python

Este repositorio contiene el código y la documentación de la práctica experimental realizada para la asignatura de Sistemas Operativos, en la cual se implementan y evalúan mecanismos de concurrencia en Python utilizando la biblioteca `threading`.

## Objetivo

- **Demostrar el uso de mecanismos de sincronización** en Python (mutex, barreras y eventos).
- **Analizar el impacto de la ejecución concurrente** en el uso de recursos del sistema (CPU y memoria).
- **Practicar la implementación y monitoreo** de procesos concurrentes en un entorno real.

## Contenido

- **mutex.py:** Código que implementa un mecanismo de exclusión mutua utilizando `threading.Lock()`.
- **barreras.py:** Código que sincroniza la ejecución de hilos mediante `threading.Barrier()`.
- **eventos.py:** Código que coordina la activación de tareas a través de `threading.Event()`.

## Entorno de Prueba

- **Procesador:** Intel Core i7-8700 (6 núcleos físicos, 12 hilos)
- **Memoria RAM:** 16 GB
- **Sistema Operativo:** Windows 10 (64 bits)
- **Software:** Python 3.x (se recomienda versión 3.9 o superior)
