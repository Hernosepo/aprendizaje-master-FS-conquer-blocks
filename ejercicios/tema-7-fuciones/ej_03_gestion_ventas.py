
stock = []

def bbdd_stock(producto,precio):

    dic_stock = {
        'producto': producto,
        'precio': precio
        }
    stock.append(dic_stock)

def productos_inventario():

    for dic_stock in stock:
        print('Producto: ', dic_stock['producto'])
        print('Precio: ', dic_stock['precio'])

bbdd_stock("Camisa", 25.99)
bbdd_stock("Pantalon", 39.95)
bbdd_stock("Zapatos", 61.25)

productos_inventario()