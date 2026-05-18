"""
Caso 2 - Jason Castro
Ejercicio 2
Lógica de Programación
"""

# Crear matriz de 5 filas y 4 columnas
asientos = []

# Llenar la matriz con "Vacío"
for fila in range(5):

    fila_asientos = []

    for columna in range(4):
        fila_asientos.append("Vacío")

    asientos.append(fila_asientos)

# =========================
# REGISTRAR PASAJEROS
# =========================

cantidad_pasajeros = int(input("¿Cuántos pasajeros desea registrar?: "))

for i in range(cantidad_pasajeros):

    print("\nPasajero", i + 1)

    nombre = input("Ingrese el nombre del pasajero: ")

    fila = int(input("Ingrese la fila (0 a 4): "))
    columna = int(input("Ingrese el asiento (0 a 3): "))

    # Validar espacio vacío
    if asientos[fila][columna] == "Vacío":

        asientos[fila][columna] = nombre
        print("Asiento asignado correctamente.")

    else:
        print("Ese asiento ya está ocupado.")

# =========================
# MOSTRAR MATRIZ
# =========================

print("\n===== ASIENTOS DEL AVION =====")

for fila in range(5):

    for columna in range(4):

        print("Fila", fila,
              "Asiento", columna,
              ":", asientos[fila][columna])

# =========================
# CONSULTAR ASIENTO
# =========================

print("\n===== CONSULTAR ASIENTO =====")

fila_consulta = int(input("Ingrese la fila a consultar: "))
columna_consulta = int(input("Ingrese el asiento a consultar: "))

print("Pasajero en el asiento:",
      asientos[fila_consulta][columna_consulta])
