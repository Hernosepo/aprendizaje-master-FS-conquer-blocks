'''EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla.'''


# Ingresar numeros
numero_uno = int(input("Numero Uno: "))
numero_dos = int(input("Numero Dos: "))
numero_tres = int(input("Numero Tres: "))
numero_cuatro = int(input("Numero Cuatro: "))

# El numero mas grande entre 1 y 2 pasa al siguiente contra 3
if numero_uno > numero_dos:
    numero_mayor_uno = numero_uno
else:
    numero_mayor_uno = numero_dos
if numero_mayor_uno > numero_tres:
    numero_mayor_dos = numero_mayor_uno
else:
    numero_mayor_dos = numero_tres
if numero_mayor_dos > numero_cuatro:
    print("El numero mayor es: ", numero_mayor_dos)
else:
    print("El numero mayor es: ", numero_cuatro)        

