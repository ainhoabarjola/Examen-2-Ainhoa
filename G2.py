import heapq
from datetime import datetime

# Inicializar lista de tareas y completadas
tareas_pendientes = []
tareas_completadas = set()

# Función para agregar una tarea
def agregar_tarea(prioridad, nombre, depende_de, fecha_vencimiento):
    fecha_vencimiento_dt = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
    tarea = {
        "nombre": nombre,
        "depende de": depende_de,
        "fecha vencimiento": fecha_vencimiento_dt,
    }
    heapq.heappush(tareas_pendientes, (prioridad, nombre, tarea))
    print(f"Tarea '{nombre}' agregada con prioridad {prioridad} y vencimiento {fecha_vencimiento}.")

# Función para marcar una tarea como completada
def completar_tarea(nombre):
    global tareas_pendientes
    nueva_cola = []
    encontrada = False
    while tareas_pendientes:
        prioridad, nombre_tarea, tarea = heapq.heappop(tareas_pendientes)
        if nombre_tarea == nombre:
            tareas_completadas.add(nombre)
            encontrada = True
            print(f"Tarea '{nombre}' marcada como completada.")
        else:
            heapq.heappush(nueva_cola, (prioridad, nombre_tarea, tarea))
    tareas_pendientes.extend(nueva_cola)
    if not encontrada:
        print(f"Tarea '{nombre}' no encontrada en pendientes.")

# Función para mostrar tareas disponibles (sin dependencias pendientes)
def mostrar_tareas_disponibles():
    print("\nTareas disponibles:")
    for prioridad, nombre, tarea in sorted(tareas_pendientes):
        if tarea["depende de"] == "nada" or tarea["depende de"] in tareas_completadas:
            print(f"  - {nombre} (Prioridad: {prioridad}, Vence: {tarea['fecha vencimiento'].strftime('%Y-%m-%d')})")

# Función para procesar tareas pendientes
def procesar_tareas():
    print("\nProcesando tareas...")
    nueva_cola = []
    while tareas_pendientes:
        prioridad, nombre, tarea = heapq.heappop(tareas_pendientes)
        if tarea["depende de"] == "nada" or tarea["depende de"] in tareas_completadas:
            print(f"Ejecutando: {nombre} (Prioridad: {prioridad}, Vence: {tarea['fecha vencimiento'].strftime('%Y-%m-%d')})")
            tareas_completadas.add(nombre)
        else:
            heapq.heappush(nueva_cola, (prioridad, nombre, tarea))
            print(f"No se puede ejecutar '{nombre}' porque depende de '{tarea['depende de']}'.")
    tareas_pendientes.extend(nueva_cola)

# Ejemplo inicial de tareas
agregar_tarea(2, "Allanar el terreno", "Comprar el terreno", "2024-12-31")
agregar_tarea(1, "Comprar el terreno", "nada", "2024-12-15")
agregar_tarea(3, "Comprar materiales", "Vender la casa", "2025-01-15")
agregar_tarea(1, "Contratar trabajadores", "Vender la casa", "2025-01-10")
agregar_tarea(2, "Crear los planos", "Contratar trabajadores", "2024-12-20")
agregar_tarea(1, "Pedir permisos", "nada", "2024-12-10")
agregar_tarea(4, "Vender la casa", "Comprar el terreno", "2025-02-01")

# Interfaz de usuario
while True:
    print("\nOpciones:")
    print("1. Mostrar tareas disponibles")
    print("2. Procesar tareas")
    print("3. Agregar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_tareas_disponibles()
    elif opcion == "2":
        procesar_tareas()
    elif opcion == "3":
        nombre = input("Nombre de la tarea: ")
        prioridad = int(input("Prioridad (1-5, siendo 1 la más alta): "))
        depende_de = input("Depende de (escriba 'nada' si no depende de otra tarea): ")
        fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
        agregar_tarea(prioridad, nombre, depende_de, fecha_vencimiento)
    elif opcion == "4":
        nombre = input("Nombre de la tarea a completar: ")
        completar_tarea(nombre)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")