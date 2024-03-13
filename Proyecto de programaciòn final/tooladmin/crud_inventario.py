import json

def crear(producto,path):
    productos = {}
    with open(path,"r") as file:
        productos=json.load(file)
   
    existe = False
    for p in productos["data"]:
        if p["nombre"] == producto["nombre"]:
            existe = True
            break

    if not existe:
        productos["data"].append(producto)
        with open(path, "w") as file:
            json.dump(productos, file, indent=4)
        print("Producto agregado exitosamente.")
    else:
        print("El producto ya existe en la base de datos.")

def eliminar(nombre_producto, path):
    with open(path, "r") as file:
        productos = json.load(file)

    for i, producto in enumerate(productos["data"]):
        if producto["nombre"] == nombre_producto:
            del productos["data"][i]
            with open(path, "w") as file:
                json.dump(productos, file, indent=4)
            print("Producto eliminado exitosamente.")
            return

    print("El producto no se encontró en la base de datos.")

def buscar(nombre_producto, path):
    with open(path, "r") as file:
        productos = json.load(file)

    for producto in productos["data"]:
        if producto["nombre"] == nombre_producto:
            print("Producto encontrado:")
            print(producto)
            return

    print("El producto no se encontró en la base de datos.")

def actualizar(nombre_producto,categoria, cantidad, precio, path):
    with open(path, "r") as file:
        productos = json.load(file)

    for producto in productos["data"]:
        if producto["nombre"] == nombre_producto:
            producto["categoria"] = categoria
            producto["cantidad"] = cantidad
            producto["precio $"] = precio
            with open(path, "w") as file:
                json.dump(productos, file, indent=4)
            print("Producto actualizado exitosamente.")
            return

    print("El producto no se encontró en la base de datos.")

def mostrar_inventario(path):
    with open(path, "r") as file:
        productos = json.load(file)
    
    if productos["data"]:  # Verifica si la lista de productos no está vacía
        print("Inventario actual:")
        for producto in productos["data"]:
            print(producto)
    else:
        print("El inventario esta vacio.")
