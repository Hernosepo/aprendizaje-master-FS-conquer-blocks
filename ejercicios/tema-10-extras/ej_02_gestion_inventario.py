
def gestion_inventario(inventario, codigo, inicio, fin):
    medio = (inicio + fin) // 2
    if inventario[medio]['codigo'] == codigo:
        print('Del producto:', codigo, 'hay: ',inventario[medio]['cantidad'])
    elif inicio > fin:
        print('El código ingresado no existe')    
    else:
        if inventario[medio]['codigo'] < codigo:
            return gestion_inventario(inventario, codigo, medio + 1, fin)
        elif inventario[medio]['codigo'] > codigo:
            return gestion_inventario(inventario, codigo, inicio, medio - 1)




inventario = [
    {'codigo': 101, 'cantidad': 25},
    {'codigo': 203, 'cantidad': 50},
    {'codigo': 307, 'cantidad': 80},
    {'codigo': 412, 'cantidad': 10},
]

gestion_inventario(inventario, 307, 0, len(inventario) -1)