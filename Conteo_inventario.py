from datetime import date


fecha_registro = input("Ingresa la fecha en que se registra el inventario (DD/MM/AAAA): ")

inventario = {
    1: {"nombre": "Cafe", "precio": 35, "cantidad": 10, "fecha_cambio": fecha_registro},
    2: {"nombre": "Refresco", "precio": 25, "cantidad": 15, "fecha_cambio": fecha_registro}
}


def mostrar_inventario():
    print("\n--- INVENTARIO ---")
    productos_bajos = []

    for codigo, producto in inventario.items():
        print("Codigo:", codigo)
        print("Producto:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("Fecha del ultimo registro o cambio:", producto["fecha_cambio"])
        print()
        if producto["cantidad"] <= 5:
            productos_bajos.append(producto["nombre"])

    if productos_bajos:
        print("Productos con pocas unidades:", productos_bajos)


def modificar_producto():
    codigo = int(input("Ingresa el codigo del producto: "))

    if codigo in inventario:
        nuevo_nombre = input("Ingresa el nuevo nombre: ")
        nuevo_precio = float(input("Ingresa el nuevo precio: "))

        inventario[codigo]["nombre"] = nuevo_nombre
        inventario[codigo]["precio"] = nuevo_precio
        inventario[codigo]["fecha_cambio"] = date.today().strftime("%d/%m/%Y")

        print("Producto modificado correctamente.")
        print("Fecha del cambio:", inventario[codigo]["fecha_cambio"])
    else:
        print("Ese codigo no existe.")


def agregar_producto():
    codigo = int(input("Ingresa el codigo del nuevo producto: "))

    if codigo in inventario:
        print("Ese codigo ya existe. Usa la opcion de modificar producto.")
        return

    nombre = input("Ingresa el nombre: ")
    precio = float(input("Ingresa el precio: "))
    cantidad = int(input("Ingresa la cantidad: "))

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "fecha_cambio": date.today().strftime("%d/%m/%Y")
    }

    print("Producto agregado correctamente.")
    print("Fecha de registro:", inventario[codigo]["fecha_cambio"])


def realizar_venta():
    total = 0
    agregar_otro = "s"

    while agregar_otro == "s":
        codigo = int(input("Ingresa el codigo del producto que deseas vender: "))

        if codigo in inventario:
            cantidad = int(input("Ingresa la cantidad que deseas vender: "))

            if cantidad > 0 and cantidad <= inventario[codigo]["cantidad"]:
                inventario[codigo]["cantidad"] -= cantidad
                inventario[codigo]["fecha_cambio"] = date.today().strftime("%d/%m/%Y")
                subtotal = cantidad * inventario[codigo]["precio"]
                total += subtotal
                print("Producto agregado a la venta. Subtotal: $", subtotal)
                print("Fecha del cambio en inventario:", inventario[codigo]["fecha_cambio"])
            else:
                print("La cantidad no es valida o no hay suficiente inventario.")
        else:
            print("Ese codigo no existe.")

        agregar_otro = input("Deseas agregar otro producto? (s/n): ").lower()

    if total > 0:
        print("Total de la venta: $", total)



continuar = "s"


while continuar == "s":
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Modificar producto")
    print("4. Realizar venta")
    print("5. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        modificar_producto()
    elif opcion == "4":
        realizar_venta()
    elif opcion == "5":
        continuar = "n"
        print("Programa finalizado.")
    else:
        print("Opcion no valida.")
