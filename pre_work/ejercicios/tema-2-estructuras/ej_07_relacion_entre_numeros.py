'''RELACION ENTRE NÚMEROS:
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos.'''

# Pedir tres numeros
numero_uno = int(input("Numero 1: "))
numero_dos = int(input("Numero 2: "))
numero_tres = int(input("Numero 3: "))

if numero_uno == numero_dos + numero_tres:
    print("Los numeros: ", numero_dos, " y ", numero_tres, " suman: ", numero_uno)
elif numero_dos == numero_uno + numero_tres:
    print("Los numeros: ", numero_uno, " y ", numero_tres, " suman: ", numero_dos)
elif numero_tres == numero_uno + numero_dos:
    print("Los numeros: ", numero_dos, " y ", numero_uno, " suman: ", numero_tres)     
else:
    print("Dos numeros no logran sumar el valor de uno")