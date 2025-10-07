'''3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última.'''


# Pedir palabra
palabra = input("Ingrese una palabra: ")

# Contar cuan larga es la palabra
largo_palabra = len(palabra)
# Hacer una iteracion que imprima letra por letra al reves
for i in range(largo_palabra,0,-1):
    print(palabra[i-1])