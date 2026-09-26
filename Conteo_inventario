inventario = {
    1: {"nombre": "Cafe", "precio": 35, "cantidad": 10},
    2: {"nombre": "Refresco", "precio": 25, "cantidad": 15}
}


def mostrar_inventario():
    print("\n--- INVENTARIO ---")

    for codigo, producto in inventario.items():
        print("Codigo:", codigo)
        print("Producto:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print()


def modificar_producto():
    codigo = int(input("Ingresa el codigo del producto: "))

    if codigo in inventario:
        nuevo_nombre = input("Ingresa el nuevo nombre: ")
        nuevo_precio = float(input("Ingresa el nuevo precio: "))

        inventario[codigo]["nombre"] = nuevo_nombre
        inventario[codigo]["precio"] = nuevo_precio

        print("Producto modificado correctamente.")
    else:
        print("Ese codigo no existe.")


def agregar_producto():
    codigo = int(input("Ingresa el codigo del nuevo producto: "))
    nombre = input("Ingresa el nombre: ")
    precio = float(input("Ingresa el precio: "))
    cantidad = int(input("Ingresa la cantidad: "))

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Producto agregado correctamente.")



continuar = "s"


while continuar == "s":
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Modificar producto")
    print("4. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        modificar_producto()
    elif opcion == "4":
        continuar = "n"
        print("Programa finalizado.")
    else:
        print("Opcion no valida.")