import os

class Producto:
    def __init__(self,nombre,stock):
        self.nombre = nombre
        self.stock = stock

    def __str__(self):
        return f'{self.nombre} {self.stock}'

inventario = []

def  agregarProducto():
    nombre = input("Ingrese el nombre del producto: ")
    stockInicial = int(input("Ingrese el stock inicial: "))
    producto: Producto = Producto(nombre=nombre, stock=stockInicial)
    inventario.append(producto)

def listarProducto():
    if len(inventario) == 0:
        print("No hay productos en el inventario")
        return

    for producto in inventario:
        print(producto)

while True:
    print("1. Listar inventario\n2. Crear Producto\n3. Salir")
    opcion = int(input("Ingrese una opción [1-3]: "))
    if opcion == 1:
        os.system("cls")
        listarProducto()
    elif opcion == 2:
        os.system("cls")
        agregarProducto()
    elif opcion == 3:
        os.system("cls")
        break
    else:
        os.system("cls")
        print("Opción inválida, reintente")