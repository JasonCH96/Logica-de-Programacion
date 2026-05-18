"""
Caso 2 - Jason Castro
Ejercicio 3
Lógica de Programación
"""

# Cantidad de estudiantes y actividades
CANTIDAD_ESTUDIANTES = 5
CANTIDAD_ACTIVIDADES = 4

# Matriz para guardar notas
notas = []

# Lista para nombres
nombres = []

# =========================
# INGRESO DE DATOS
# =========================

for estudiante in range(CANTIDAD_ESTUDIANTES):

    print("\nEstudiante", estudiante + 1)

    nombre = input("Ingrese el nombre del estudiante: ")
    nombres.append(nombre)

    fila_notas = []

    for actividad in range(CANTIDAD_ACTIVIDADES):

        nota = float(input("Ingrese la nota de la actividad "
                           + str(actividad + 1) + ": "))

        fila_notas.append(nota)

    notas.append(fila_notas)

# =========================
# CALCULAR PROMEDIOS
# =========================

mayor_promedio = -1
mejor_estudiante = ""

print("\n===== RESULTADOS FINALES =====")

for estudiante in range(CANTIDAD_ESTUDIANTES):

    suma_notas = 0

    for actividad in range(CANTIDAD_ACTIVIDADES):

        suma_notas += notas[estudiante][actividad]

    promedio = suma_notas / CANTIDAD_ACTIVIDADES

    print("Estudiante:", nombres[estudiante])
    print("Nota final:", promedio)

    # Buscar promedio más alto
    if promedio > mayor_promedio:

        mayor_promedio = promedio
        mejor_estudiante = nombres[estudiante]

# =========================
# MOSTRAR MEJOR ESTUDIANTE
# =========================

print("\n===== MEJOR ESTUDIANTE =====")
print("Nombre:", mejor_estudiante)
print("Promedio:", mayor_promedio)
