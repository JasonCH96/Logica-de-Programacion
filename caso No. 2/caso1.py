"""
Caso 2 - Jason Castro
Ejercicio 1
Lógica de Programación
"""

# Lista para guardar las ganancias
ganancias = []

# Variable para total
total_semana = 0

# Variable para mayor ganancia
mayor_ganancia = 0
dia_mayor = 0

# Ciclo para pedir los 7 días
for dia in range(1, 8):

    monto = float(input("Ingrese lo ganado en el día " + str(dia) + ": "))

    # Guardar en la lista
    ganancias.append(monto)

    # Sumar al total
    total_semana = total_semana + monto

    # Verificar mayor ganancia
    if monto > mayor_ganancia:
        mayor_ganancia = monto
        dia_mayor = dia

# Mostrar resultados
print("\n===== RESULTADOS =====")
print("Total ganado en la semana:", total_semana)
print("El día que ganó más dinero fue el día:", dia_mayor)
print("Monto mayor ganado:", mayor_ganancia)
