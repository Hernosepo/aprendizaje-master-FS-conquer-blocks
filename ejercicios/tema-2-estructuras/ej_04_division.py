'''DIVISION:
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
divisor es cero el programa debe mostrar un error.'''

numero_uno = int(input("Numero Uno: "))
numero_dos = int(input("Numero Dos: "))

calculo = numero_uno / numero_dos

if calculo == 0:
    print("Error")
else:
    print(calculo)    
