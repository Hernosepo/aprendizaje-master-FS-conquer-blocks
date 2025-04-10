'''ARRAYS 2D
9. Crea un arrays lleno de 1s con una longitud dada por el usuario
10.Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
11.Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)
12.Concatena ambas estructuras horizontalmente y verticalmente
(Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy)'''

import numpy as np

array_de_unos = int(input("Ingresa un numero: "))

array_de_unos = np.ones(array_de_unos)

print(array_de_unos)

print("Ahora deberas ingresar 2 numeros que multiplicados den tu numero seleccionado")
array_de_filas = int(input("Ingresa un numero: "))
array_de_columnas = int(input("Ingresa otro numero: "))

array_reshape = array_de_unos.reshape(array_de_filas,array_de_columnas)

print(array_reshape)

matrix_identidad = np.eye(array_de_filas,array_de_columnas)
print(matrix_identidad)

array_concatenado = np.concatenate((array_reshape, matrix_identidad))
print(array_concatenado)

array_hstack = np.hstack((array_reshape, matrix_identidad))
print(array_hstack)
array_vstack = np.vstack((array_reshape, matrix_identidad))
print(array_vstack)