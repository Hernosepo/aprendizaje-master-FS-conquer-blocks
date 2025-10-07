'''CALCULO DE NOTAS FINALES
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna.'''


import numpy as np


# Genero un array aleatorio de 5 filas y 4 columnas con notas entre 4 y 10
array_bidimensional = np.random.randint(4, 11, size=(5,4)) 

# Le doy valores a los porcentajes de cada evaluacion
examen_1 = 0.3
examen_2 = 0.3
trabajo = 0.3
participacion = 0.1

# Itero por el array tomando las filas por separado
for fila in array_bidimensional:
# En cada fila realizo la operacion combinada para sacar el resultado    
    promedio = ((fila[0] * examen_1) + (fila[1] * examen_2) + (fila[2] * trabajo) + (fila[3] * participacion))
    print(promedio)

# Investigo y realizo nuevamente la operacion con el metodo dot()
# Genero un array para que cada elemento se multipilque con su correspondiente y luego se sume
valores_notas = np.array([0.3, 0.3, 0.3, 0.1])
promedio_metodo = np.dot(array_bidimensional, valores_notas)
print(promedio_metodo)