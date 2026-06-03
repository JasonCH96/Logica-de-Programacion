"""
Sistema de Liquidación de Tours
Proyecto de Lógica de Programación
"""
# ======================================================
# Proyecto: Automatización de Liquidaciones de Tours
# Curso: Lógica de Programación
# Estudiante: Jason Rodolfo Castro Herrera
# ======================================================

# ==========================================
# ARREGLOS PARA ALMACENAR LAS VENTAS
# ==========================================

ids_ventas = []
clientes = []
tours = []
proveedores = []
cantidades_personas = []
precios_venta = []
tarifas_netas = []
comisiones = []

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

        monto_comision = precio_venta - tarifa_neta

        # Guardar en los arreglos
        ids_ventas.append(id_venta)
        clientes.append(nombre_cliente)
        tours.append(nombre_tour)
        proveedores.append(proveedor_tour)
        cantidades_personas.append(cantidad_personas)
        precios_venta.append(precio_venta)
        tarifas_netas.append(tarifa_neta)
        comisiones.append(monto_comision)

        print("\nVenta registrada correctamente.")

    # ==========================================
    # OPCION 2 - CONSULTAR
    # ==========================================
    elif opcion_menu == 2:

        print("\n--- CONSULTA DE VENTAS ---")

        if len(ids_ventas) == 0:

            print("No hay ventas registradas.")

        else:
            for i in range(len(ids_ventas)):
                print("-----------------------------")
                print("ID:", ids_ventas[i])
                print("Cliente:", clientes[i])
                print("Tour:", tours[i])
                print("Proveedor:", proveedores[i])
                print("Personas:", cantidades_personas[i])
                print("Precio:", precios_venta[i])
                print("Tarifa Neta:", tarifas_netas[i])
                print("Comisión:", comisiones[i])

    # ==========================================
    # OPCION 3 - MODIFICAR
    # ==========================================
    elif opcion_menu == 3:

        print("\n--- MODIFICAR VENTA ---")

        id_busqueda = input("Ingrese el ID de la venta a modificar: ")

        encontrado = False

        for i in range(len(ids_ventas)):

            if ids_ventas[i] == id_busqueda:

                nuevo_cliente = input("Nuevo nombre del cliente: ")
                nuevo_precio = float(input("Nuevo precio total: "))
                nueva_tarifa = float(input("Nueva tarifa neta: "))

                clientes[i] = nuevo_cliente
                precios_venta[i] = nuevo_precio
                tarifas_netas[i] = nueva_tarifa
                comisiones[i] = nuevo_precio - nueva_tarifa

                encontrado = True

                print("Venta modificada correctamente.")
                break

        if not encontrado:
            print("No se encontró la venta.")

    # ==========================================
    # OPCION 4 - BORRAR
    # ==========================================
    elif opcion_menu == 4:

        print("\n--- BORRAR VENTA ---")

        id_eliminar = input("Ingrese el ID de la venta a eliminar: ")

        encontrado = False

        for i in range(len(ids_ventas)):

            if ids_ventas[i] == id_eliminar:

                ids_ventas.pop(i)
                clientes.pop(i)
                tours.pop(i)
                proveedores.pop(i)
                cantidades_personas.pop(i)
                precios_venta.pop(i)
                tarifas_netas.pop(i)
                comisiones.pop(i)

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
