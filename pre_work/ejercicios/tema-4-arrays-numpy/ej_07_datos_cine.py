'''DATOS CINEMATOGRÁFICOS
Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película.'''

import numpy as np

# array con datos de películas
peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])  


# Genero función de popularidad de peliculas por calificacion
# Creo la funcionn
def peliculas_popularidad_calificacion (peliculas):
    # Busco el funcionamiento de np.unique para que devuelva un array con valores unicos
    # Genero una variable para que devuelva el resultado agrupado de la columna 1 
    clasificacion_generos_uniq = np.unique(peliculas[:, 1])

    # Creo una lista donde voy a alojar los datos al final
    lista_promedios_calificacion = []

    # Itero por la columna uno sobre la variable de np.unique
    for genero in clasificacion_generos_uniq:

        # Creo un condicional sobre el aaray para que se quede con los resultados True 
        mascara_generos_calificacion = peliculas[:, 1] == genero

        # Creo una variable para alojar la mascara del condicional
        generos_calificacion = peliculas[mascara_generos_calificacion]

        # Creo una variable para hacer la operacion de la media de la popularidad por genero
        mean_generos_calificacion = np.mean(generos_calificacion[:, 4].astype(float))

        # Agrego todos los resultado a la lista
        lista_promedios_calificacion.append([genero, round(mean_generos_calificacion, 2)])
    return lista_promedios_calificacion

resultado_popularidad_generos = peliculas_popularidad_calificacion(peliculas)
print(resultado_popularidad_generos)


# Genero función de peliculas por genero
def peliculas_por_genero(peliculas):
    
    # Agrupo generos de forma unica
    generos_unicos = np.unique(peliculas[:, 1])
    # Creo lista para alojar resultados
    lista_generos_unicos = []

    # Itero sobre la columna 1 para obtener los generos agrupados
    for generos in generos_unicos:
        # Creo mascara condicional para determinar sobre el array que resultados agrupar
        mascara_generos = peliculas[:, 1] == generos

        # Creo variable para para alojar la mascara de generos
        generos_agrupados = peliculas[mascara_generos]

        # Sumo los generos con la funcion sum()
        suma_generos_agrupados = np.sum(len(generos_agrupados[:, 1]))
        lista_generos_unicos.append([generos, suma_generos_agrupados])
    return lista_generos_unicos    
resultado_suma_generos = peliculas_por_genero(peliculas)
print("este resiltado",resultado_suma_generos)

# Cuantas peliculas se lanzaron en cada decada en general
def peliculas_por_decadas(peliculas):

    # Agrupo decadas con np.unique - la cuenta matematica tuve que buscar la solucion porque se iba
    decadas_unicas = np.unique(peliculas[:, 3].astype(int) // 10 * 10)
    lista_decadas = []

    # Itero sobre el array en la columna de las decadas
    for decadas in decadas_unicas:
        # Genero el condicionlal y la variable para agrupar las decadas
        mascara_decada = peliculas[:, 3].astype(int) // 10 * 10 == decadas
        decadas_agrupadas = peliculas[mascara_decada]
        # Realizo la suma de lanzamiento por decada
        suma_decadas_agrupadas = len(decadas_agrupadas)
        lista_decadas.append([decadas, suma_decadas_agrupadas])
    return lista_decadas
resultado_suma_decadas = peliculas_por_decadas(peliculas)
print(resultado_suma_decadas)

# Cuantas peliculas se lanzaron en cada decada por genero
def peliculas_por_decada_genero(peliculas):
    generos = np.unique(peliculas[:, 1])
    decadas = np.unique(peliculas[:, 3].astype(int) // 10 * 10)
    resultados = []

    for genero in generos:
        for decada in decadas:
            mascara = (peliculas[:, 1] == genero) & ((peliculas[:, 3].astype(int) // 10 * 10) == decada)
            cantidad = np.sum(mascara)
            resultados.append([genero, decada, cantidad])
    return resultados

resultado_decada_genero = peliculas_por_decada_genero(peliculas)
print(resultado_decada_genero)

# Duracion promedio de peliculas
def duracion_promedio_por_genero(peliculas):
    generos = np.unique(peliculas[:, 1])
    resultado = []
    for genero in generos:
        mascara = (peliculas[:, 1] == genero).nonzero()[0]
        duraciones = peliculas[mascara][:, 2].astype(float)
        promedio = np.mean(duraciones)
        resultado.append([genero, round(promedio, 2)])
    return resultado


