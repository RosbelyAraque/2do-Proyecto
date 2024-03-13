from tooladmin.crud_inventario import crear,eliminar,buscar,actualizar,mostrar_inventario
path= "database.json"
nombre_producto=0
opcion=0

while opcion != 6:
        print("Bienvenido al sistema de gestión de inventario de la farmacia.")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ").lower()
            categoria = input("Ingrese la categoría del producto: ").lower()
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio del producto $ "))
            producto = {"nombre": nombre, "categoria": categoria, "cantidad": cantidad, "precio $": precio}
            crear(producto, path)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
            eliminar(nombre, path)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ").lower()
            buscar(nombre, path)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a actualizar: ").lower()
            categoria = input("Ingrese la nueva categoría del producto:").lower()
            cantidad = int(input("Ingrese la nueva cantidad en stock: "))
            precio = float(input("Ingrese el nuevo precio del producto $ "))
            actualizar(nombre,categoria, cantidad, precio, path)
        elif opcion == "5":
            mostrar_inventario(path)
        elif opcion == "6":
            print("Gracias por usar nuestro sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")



