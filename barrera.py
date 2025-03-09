import threading

# Creación de una barrera para sincronizar 2 hilos
barrera = threading.Barrier(2)

def tarea():
    print("Hilo iniciado")
    # Cada hilo espera en la barrera hasta que ambos lleguen
    barrera.wait()
    print("Hilo continuando")

# Creación de dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Inicio de los hilos
hilo1.start()
hilo2.start()

# Espera a que ambos hilos finalicen
hilo1.join()
hilo2.join()

print("Programa terminado")
