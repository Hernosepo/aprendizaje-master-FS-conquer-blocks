'''ARRAYS 1D PARTE 2:
1. Crea un array con 15 números enteros aleatorios entre 1 y 100
2. Multiplica todos los elementos del array usando un bucle y después usando un
método de numpy. Compara los resultados
3. Crea otro array con 15 números decimales aleatorios entre 0 y 1
4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
operador y después con una función de numpy (Pista: busca en google que función de numpy hace esto)
5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
(Pista: busca en google que función de numpy hace esto)
6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y
después con una función de numpy (Pista: busca en google que función de numpy hace esto)
7. Encuentra el valor más alto del primer array que has creado.
8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard
deviation) de los arrays (Nota: No nos importa el significado matemático de estos
valores, lo importante es que encuentres que función de numpy necesitas. Puedes
hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
haber más resultados).'''

import numpy as np


numeros_aleatorios = np.random.randint(1,100,15)
print(numeros_aleatorios)

multiplica_array = 0
for numeros in numeros_aleatorios:
    multiplica_array *= numeros
print(multiplica_array)

multiplica_metodo = np.prod(numeros_aleatorios)
print(multiplica_array)

print("___________________")

array_decimal = np.random.uniform(0,1,15)
print(array_decimal)

dos_arrays_sumadas = numeros_aleatorios + array_decimal
print(dos_arrays_sumadas)
dos_arrays_sumadas_metodo = np.add(numeros_aleatorios,array_decimal)
print(dos_arrays_sumadas_metodo)

dos_arrays_restadas = numeros_aleatorios - array_decimal
print(dos_arrays_restadas)
dos_arrays_restadas_metodo = np.subtract(numeros_aleatorios,array_decimal)
print(dos_arrays_restadas_metodo)

dos_arrays_multiplicadas = numeros_aleatorios * array_decimal
print(dos_arrays_multiplicadas)
dos_arrays_multiplicadas_metodo = np.multiply(numeros_aleatorios,array_decimal)
print(dos_arrays_multiplicadas_metodo)


numero_max = np.max(numeros_aleatorios)
print(numero_max)

numero_mean = np.mean(numeros_aleatorios)
print(numero_mean)

print(np.median(numeros_aleatorios))
print(np.std(numeros_aleatorios))
