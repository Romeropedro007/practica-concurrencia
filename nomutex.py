import threading
import time

# Variable global compartida
contador_global = 0

# Función para incrementar la variable global sin utilizar mutex
def incrementar():
    global contador_global
    # Leer el valor actual
    valor = contador_global
    # Introducimos un pequeño retardo para aumentar la posibilidad de intercalación
    time.sleep(0.00001)
    # Actualizamos el contador
    contador_global = valor + 1

# Función que ejecuta la tarea de incrementar el contador
def tarea():
    for _ in range(100000):
        incrementar()

# Creación de dos hilos que ejecutarán la misma tarea sin sincronización
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Inicio de los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos finalicen
hilo1.join()
hilo2.join()

# Imprimir el valor final del contador global
print("El valor final del contador global es:", contador_global)
