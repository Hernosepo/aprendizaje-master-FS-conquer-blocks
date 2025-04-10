
'''COMPAÑÍA DE AUTOMÓVILES:
Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.'''

serieUno = 20000
seriePlus = 35000
todoTerreno = 60000

ventasUno = int(input("Ingrese autos vendidos tipo RBM Serie Uno:\n"))
ventasPlus = int(input("Ingrese autos vendidos tipo RBM Serie Plus:\n"))
ventasTodo = int(input("Ingrese autos vendidos tipo RBM Todo Terreno:\n"))

ventasMes = (serieUno * ventasUno) * 0.03 + (seriePlus * ventasPlus) * 0.05 + (todoTerreno * ventasTodo) * 0.07

print("Su comisión por ventas en este mes es: $", ventasMes)


