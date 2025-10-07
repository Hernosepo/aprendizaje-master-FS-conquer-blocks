'''CASA DE CAMBIOS: Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario de el resultante en dólares.

1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)
2. La casa de cambios se queda un 10% en concepto de tasas de gestión. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario.'''



aCambiar = int(input("Cuantos EUROS quiere cambiar?\n "))
print(" ")
print(" ")

cambioEuro = (aCambiar * 1.2) 
cambio = cambioEuro - (cambioEuro * 0.1)
tasa = cambioEuro * 0.1

print("La cotzación es 1 EURO = 1.2 u$s ")
print("Su Total: u$s", cambio, " Cargo por servicio: u$s", tasa)