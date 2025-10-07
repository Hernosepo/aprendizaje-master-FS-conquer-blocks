'''BUCLES:
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
*
**
***
****
*****
****
***
**
*
'''


# 1

# Pedir al usuario un numero
max_estrellas = int(input("Ingrese un numero "))

# Iniciar en el 0 hasta el numero imprimiendo *
for i in range(max_estrellas):
    print("*"*(i+1))
for i in range(max_estrellas, 1,-1):
    print("*"*(i-1))