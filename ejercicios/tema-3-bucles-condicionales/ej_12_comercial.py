'''EL COMERCIAL:
Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las
ventas. Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades...'''

lista_ventas = [["Producto 1", 30.0, 3], ["Producto 2", 9.8, 1], ["Producto 5", 71.5, 7], ["Producto 6", 44.0, 2], ["Producto 9", 25.3, 4]]
venta_unitaria = 0
suma_venta_total = 0


for ventas in lista_ventas:
    venta_unitaria = (float(ventas[1]) * int(ventas[2]))
    print(venta_unitaria)
    suma_venta_total = suma_venta_total + venta_unitaria
    #venta_unitaria = 0
print(suma_venta_total)
