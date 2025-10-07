'''ARRAYS 1D PARTE 1:
1. Crea un array_1 lleno ceros con una longitud de 8 elementos.
2. Haz que todos los elementos de este array sean igual a 2
3. Crea un array_2 que contenga todos los números pares del 1 al 10.
4. Suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. 
Compara los resultados
5. Revierte array_2 y guárdalo en una variable independiente.
6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y
array_2_revertido (Pista: Investiga el uso de intersect1d() de numpy)
7. Crea un arrays lleno de 1s con una longitud dada por el usuario'''

import numpy as np

print("Puntos 1 y 2")
array_1 = np.zeros((8))
print(array_1)
array_1[:] = 2
print(array_1)

print("----------------------")

print("Punto 3, 4, 5 y 6")

array_2 = np.arange(1,11)
print(array_2)
suma_array = 0

for numero in array_2:
    suma_array = suma_array + numero
print(suma_array)
suma_metodo = array_2.sum()
print(suma_metodo)

array_2_reves = np.flip(array_2)
print(array_2_reves)

array_intersec_uno = np.intersect1d(array_1, array_2)
array_intersec_reves =np.intersect1d(array_2, array_2_reves)

print(array_intersec_uno)
print(array_2_reves)


print("----------------------")

print("Punto 7")
numero_array = int(input("Igrese un numero: "))
imprenta_array = np.ones(numero_array)
print(imprenta_array)
