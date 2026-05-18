"""
Sistema de Liquidación de Tours
Proyecto de Lógica de Programación
"""
# ======================================================
# Proyecto: Automatización de Liquidaciones de Tours
# Curso: Lógica de Programación
# Estudiante: Jason Rodolfo Castro Herrera
# ======================================================

# Lista para almacenar las ventas de tours
ventas_tours = []

# Variable para controlar el menú
opcion_menu = 0

# Ciclo principal del programa
while opcion_menu != 5:

    print("\n====================================")
    print(" SISTEMA DE LIQUIDACION DE TOURS")
    print("====================================")
    print("1. Incluir venta")
    print("2. Consultar ventas")
    print("3. Modificar venta")
    print("4. Borrar venta")
    print("5. Salir")

    opcion_menu = int(input("Seleccione una opción: "))

    # ==========================================
    # OPCION 1 - INCLUIR
    # ==========================================
    if opcion_menu == 1:

        print("\n--- REGISTRO DE VENTA ---")

        id_venta = input("Ingrese el ID de la venta: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        nombre_tour = input("Ingrese el nombre del tour: ")
        proveedor_tour = input("Ingrese el proveedor: ")
        cantidad_personas = int(input("Ingrese cantidad de personas: "))
        precio_venta = float(input("Ingrese el precio total: "))
        tarifa_neta = float(input("Ingrese la tarifa neta del proveedor: "))

        # Calculo de comisión
        monto_comision = precio_venta - tarifa_neta

        # Crear registro
        venta = {
            "ID": id_venta,
            "Cliente": nombre_cliente,
            "Tour": nombre_tour,
            "Proveedor": proveedor_tour,
            "Personas": cantidad_personas,
            "Precio": precio_venta,
            "TarifaNeta": tarifa_neta,
            "Comision": monto_comision,
        }

        # Guardar en la lista
        ventas_tours.append(venta)

        print("\nVenta registrada correctamente.")

    # ==========================================
    # OPCION 2 - CONSULTAR
    # ==========================================
    elif opcion_menu == 2:

        print("\n--- CONSULTA DE VENTAS ---")

        if len(ventas_tours) == 0:
            print("No hay ventas registradas.")

        else:
            for venta in ventas_tours:
                print("-----------------------------")
                print("ID:", venta["ID"])
                print("Cliente:", venta["Cliente"])
                print("Tour:", venta["Tour"])
                print("Proveedor:", venta["Proveedor"])
                print("Personas:", venta["Personas"])
                print("Precio:", venta["Precio"])
                print("Tarifa Neta:", venta["TarifaNeta"])
                print("Comisión:", venta["Comision"])

    # ==========================================
    # OPCION 3 - MODIFICAR
    # ==========================================
    elif opcion_menu == 3:

        print("\n--- MODIFICAR VENTA ---")

        id_busqueda = input("Ingrese el ID de la venta a modificar: ")

        encontrado = False

        for venta in ventas_tours:

            if venta["ID"] == id_busqueda:

                nuevo_cliente = input("Nuevo nombre del cliente: ")
                nuevo_precio = float(input("Nuevo precio total: "))
                nueva_tarifa = float(input("Nueva tarifa neta: "))

                nueva_comision = nuevo_precio - nueva_tarifa

                venta["Cliente"] = nuevo_cliente
                venta["Precio"] = nuevo_precio
                venta["TarifaNeta"] = nueva_tarifa
                venta["Comision"] = nueva_comision

                encontrado = True

                print("Venta modificada correctamente.")

        if not encontrado:
            print("No se encontró la venta.")
    # ==========================================
    # OPCION 4 - BORRAR
    # ==========================================
    elif opcion_menu == 4:

        print("\n--- BORRAR VENTA ---")

        id_eliminar = input("Ingrese el ID de la venta a eliminar: ")

        encontrado = False

        for venta in ventas_tours[:]:

            if venta["ID"] == id_eliminar:
                ventas_tours.remove(venta)
                encontrado = True
                print("Venta eliminada correctamente.")
                break

        if not encontrado:
            print("No se encontró la venta.")

    # ==========================================
    # OPCION 5 - SALIR
    # ==========================================
    elif opcion_menu == 5:

        print("\nGracias por utilizar el sistema.")

    # ==========================================
    # OPCION INVALIDA
    # ==========================================
    else:

        print("\nOpción inválida. Intente nuevamente.")
