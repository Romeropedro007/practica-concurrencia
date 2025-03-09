import threading

# Variable global compartida
contador_global = 0

# Creación del mutex (Lock)
mutex = threading.Lock()

# Función para incrementar la variable global de forma segura
def incrementar():
    global contador_global
    # Adquirir el lock para entrar a la sección crítica
    mutex.acquire()
    try:
        contador_global += 1
    finally:
        # Liberar el lock para que otros hilos puedan acceder
        mutex.release()

# Función que ejecuta la tarea de incrementar el contador
def tarea():
    for _ in range(100000):
        incrementar()

# Creación de dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Inicio de los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos finalicen
hilo1.join()
hilo2.join()

print("El valor final del contador global es:", contador_global)
