'''TARJETA DE CRÉDITO:
Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678.'''


nroTdc = str(input("Ingrese el numero de su TDC: "))


for i in range(0, nroTdc - 4):
    nroAsterisco = nroTdc.replace(i,"*")

    
print(nroAsterisco)