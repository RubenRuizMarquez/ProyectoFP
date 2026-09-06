inventario = {
	1: {"nombre": "Cafe", "precio": 35, "cantidad": 10},
	2: {"nombre": "Refresco", "precio": 25, "cantidad": 15}
}


def mostrar_inventario():
	print("\n--- INVENTARIO ---")

	for codigo in inventario:
		producto = inventario[codigo]
		print("Codigo:", codigo)
		print("Producto:", producto["nombre"])
		print("Precio: $", producto["precio"])
		print("Cantidad disponible:", producto["cantidad"])
		print()


while True:
	print("--- SISTEMA DE INVENTARIO ---")
	print("1. Ver inventario")
	print("2. Salir")

	opcion = input("Selecciona una opcion: ")

	if opcion == "1":
		mostrar_inventario()
	elif opcion == "2":
		print("Programa finalizado.")
		break
	else:
		print("Opcion no valida.")
