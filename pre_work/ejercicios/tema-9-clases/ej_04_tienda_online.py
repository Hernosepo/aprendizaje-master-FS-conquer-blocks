'''TIENDA ONLINE 
Crea una clase "Producto" con atributos como nombre, precio y cantidad en 
stock. Luego, crea una clase "Tienda" que contenga una lista de productos 
disponibles y métodos para agregar productos, mostrar el inventario y 
realizar una compra. '''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        pass

class Tienda:
    def __init__(self):
        self.disponible = []

    def agregar_producto(self, producto):
        self.disponible.append(producto)
        
    def mostrar_inventario(self):
        for producto in self.disponible:
            print(f'{producto.nombre} vale {producto.precio} y hay {producto.stock}')

    def realizar_compra(self, nombre, cantidad):
        for producto in self.disponible:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Total: {producto.precio * cantidad}")
                else:
                    print("No hay suficiente stock.")

                return

        print("Producto no encontrado")        
        pass

tienda_virtual = Tienda()
nuevo_producto_1 = Producto('Remera', 10, 100)
nuevo_producto_2 = Producto('Pantalon', 20, 50)


tienda_virtual.agregar_producto(nuevo_producto_1)
tienda_virtual.agregar_producto(nuevo_producto_2)
tienda_virtual.mostrar_inventario()

tienda_virtual.realizar_compra('Remera', 25)  # Intentar comprar 55 camisetas
tienda_virtual.mostrar_inventario()  # Mostrar el inventario después de intentar la compra
