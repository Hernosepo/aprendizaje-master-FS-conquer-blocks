'''PAR O IMPAR:
Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)'''


numero_uno = int(input("Ingrese un numero: "))
numero_dos = int(input("Ingrese otro numero: "))

calculo = numero_uno ** numero_dos

if calculo % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")    