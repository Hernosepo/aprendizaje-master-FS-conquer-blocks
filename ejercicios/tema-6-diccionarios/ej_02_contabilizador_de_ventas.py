
'''Lo que quiero hacer es lo siguiente:
Creo un diccionario vacio

Opcion 1: While
Pregunto si el producto es nuevo (1) o existente (2)
    Existente (2)
        Si el producto es existente
            Pregunto cuanto se vendio
            Sumo el numero al valor del producto existente
            Sumo el numero al valor general
    Nuevo (1)
        Si el producto no existe
            Se crea la entrada al diccionario
            Pregunto cuantas unidades se vendieron
            Sumo el numero al valor general
Muestro las unidades vendidas por producto y las ventas generales
Pregunto si desea continuar
    Si responde SI volvemos al principio del loop
    Si responde NO el programa se despide
    
'''

registro_ventas = {}
def creador_numero_producto(producto_ingresado,contador):
    string_producto = 'Producto'
    string_final = string_producto+str(contador)
    return string_final


ingresar_nueva_venta = 'S'
contador = 0
while ingresar_nueva_venta.upper().strip() == 'S':
    venta_nueva = input("Nueva Venta\n Seleccione un numero:\n Producto Nuevo (1) - Producto Existente (2) ")
    if venta_nueva == '1':
        producto_ingresado = input("Nombre comercial del producto: ")
        cantidad_venta_producto_nuevo = int(input("Cuantas unidades vendió? "))
        contador += 1
        producto_nuevo_def = creador_numero_producto(producto_ingresado,contador)
        registro_ventas[producto_nuevo_def] = {'nombre' : producto_ingresado, 'ventas' : cantidad_venta_producto_nuevo}    
    else:
        producto_ingresado = input("Nombre comercial del producto: ")
        for producto in registro_ventas:
            if registro_ventas[producto]['nombre'] == producto_ingresado:
                cantidad_venta_producto_existente = int(input("Cuantas unidades vendió? "))
                registro_ventas[producto]['ventas'] += cantidad_venta_producto_existente    
    suma = 0            
    for producto in registro_ventas:
        suma = registro_ventas[producto]['ventas'] + suma
        print("\nResumen de ventas por producto:")
    for producto in registro_ventas:
        nombre = registro_ventas[producto]['nombre']
        ventas = registro_ventas[producto]['ventas']
        print(f"- {nombre}: {ventas} unidades vendidas")    
    print("El total actualizado de ventas hasta el momento es: ",suma)

    ingresar_nueva_venta = input("Ingresar nueva venta? S/N\n")
    if ingresar_nueva_venta.upper().strip() == "N":
        ingresar_nueva_venta = False
        print("Nos vemos la proxima")
    


       
         


