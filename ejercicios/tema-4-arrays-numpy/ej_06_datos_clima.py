'''ANALISIS DE DATOS CLIMÁTICOS
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes.
(Pista 1) Tu array de entrada podría ser algo como esto, con datos de temperatura,
humedad, presión y mes del año:'''

import numpy as np

clima = np.array([
    [20, 70, 1009, 1],
    [21, 60, 1011, 1],
    [22, 40, 1010, 1],
    [18, 75, 1012, 2],
    [21, 60, 1008, 3],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [27, 49, 1007, 5],
    [29, 50, 1007, 5],
    [28, 51, 1007, 5],
    [30, 45, 1005, 6],
    [10, 30, 1005, 6],
    [32, 40, 1002, 7],
    [33, 35, 1001, 8],
    [31, 45, 1003, 9],
    [30, 42, 1001, 9],
    [29, 42, 1002, 9],
    [35, 43, 1001, 9],
    [28, 50, 1006, 10],
    [25, 60, 1010, 11],
    [27, 59, 1012, 11],
    [24, 58, 1011, 11],
    [22, 70, 1011, 12]
])

# Genero una lista con los meses del año para imprimir luego
meses_año = ["Enero ", "Febrero", "Marzo", 'Abril ', 'Mayo ', 'Junio ', 'Julio ', 'Agosto ', 'Septiembre ',
             'Octubre ', 'Noviembre ','Diciembre ']
lista_temperatura = []
# Realizo una copia por si las dudas
array_clima = clima.copy()


# Itero en un rango de 12 que son los meses
for meses in range(1,13):
   
    # Creo un condicional que me dice qué filas del array pertenecen al mes
    temperatura_mascara = array_clima[:, 3] == meses
    humedad_mascara = array_clima[:, 3] == meses
    presion_mascara = array_clima[:, 3] == meses
    
    # Genero una variable independiente para alojar la mascara (porque se me hace visualmente mas comprensible)
    temperatura_meses = array_clima[temperatura_mascara]
    humedad_meses = array_clima[humedad_mascara]
    presion_meses = array_clima[presion_mascara]
    
    # Utilizo el metodo mean para sacar la media de la temperatura en la columna 0 ya con la mascara aplicada
    temperatura_mean = np.mean(temperatura_meses[:,0])
    humedad_mean = np.mean(humedad_meses[:,1])
    presion_mean = np.mean(presion_meses[:,2])
    print(temperatura_mean)
    # Genero una lista para ordenar los meses y los promedios de los datos por mes
    lista_temperatura.append([meses_año[meses - 1],round(temperatura_mean, 2), round(humedad_mean, 2), round(presion_mean, 2)])

# Recorro la lista para obtener una impresión vertical    
for fila in lista_temperatura:
    print(fila)

# Uso lambda para urgar dentro de las listas internas y tomar el dato que quiero para sacar el maximo
print("--------------------")
print("El mes con temperatura promedio mas levada\n", max(lista_temperatura, key=lambda x: x[1]))
print("--------------------")
print("El mes con humedad promedio mas levada\n", max(lista_temperatura, key=lambda x: x[2]))
print("--------------------")
print("El mes con presión promedio mas levada\n", max(lista_temperatura, key=lambda x: x[3]))
print("--------------------")

# Busco el dia mas caluroso del año
maxima_temperatura_dia = np.max(array_clima[:,0])
print("El dia mas caluroso del año registó: ", maxima_temperatura_dia)

