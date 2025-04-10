'''OPERACIONES ARITMÉTICAS:
a. Crea un script que muestre por pantalla el resultado de la siguiente operación aritmética: (3 + 2 / 2 * 5 )2
b. Escribe un programa que lea un entero positivo, n, introducido por el usuario y después
muestre por pantalla el resultado de la siguiente operación: n (n + 1) 2
c. Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los
números de entrada, el cociente y el resto.'''


# operacionA
resultadoA = ((3+2) / (2*5))**2
print(resultadoA)

# operacionB
numEnt = int(input("Ingrese un numero entero: "))
resultadoB = (numEnt*(numEnt+1))/2
print(resultadoB)

# operacionC
num1 = int(input("ingrese un numero "))
num2 = int(input("ingrese otro numero "))

cos = num1 // num2
rest = num1 % num2

print(num1, num2)
print(cos)
print(rest)
