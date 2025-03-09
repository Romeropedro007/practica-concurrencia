import threading
import time

# Se define un semáforo con capacidad para 2 hilos simultáneos
sem = threading.Semaphore(2)

def acceso_recurso(thread_id):
    print(f"Hilo {thread_id} esperando para acceder al recurso...")
    sem.acquire()
    try:
        print(f"Hilo {thread_id} ha adquirido el recurso.")
        time.sleep(1)  # Simula la ejecución de alguna tarea
    finally:
        sem.release()
        print(f"Hilo {thread_id} ha liberado el recurso.")

# Creación de varios hilos que intentan acceder al recurso
hilos = []
for i in range(5):
    t = threading.Thread(target=acceso_recurso, args=(i,))
    hilos.append(t)

# Inicio de los hilos
for t in hilos:
    t.start()

# Espera a que todos los hilos terminen
for t in hilos:
    t.join()

print("Todos los hilos han finalizado.")
