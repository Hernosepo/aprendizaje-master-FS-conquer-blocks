
'''EMPRESA DE ELECTRONICA
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente.'''


'''
Razonamiento previo:
Mi razonamiento segun lo aprendido hasta ahora de como voy a resolver el ejercicio:
Voy a trabajar con funciones y mis analisis se van a basar en agrupar componenetes, meses y lotes
para calcular puntuaciones.
Pasos:
1.1 Crear variables unique para acceder a las columnas de componentes, meses y lotes por fuera y 
volverlas argumentos que ingresaré la función junto al array.
        componentes_unique = columna 1
        meses_unique       = .char.startwith columna 0
        lotes_unique       = columna 3

1.2 Posiblemente pueda crear mascaras por fuera de las funciones tambien para volverlas argumentos
        mascara_componentes = componentes[:, 1] == True
        mascara_meses       = componentes[:, 0] == True
        mascara_lote        = componentes[:, 3] == True    

2.1 Crear función para obtener segun componente cual tuvo la puntuación mas alta
        calidad_maxima_componente(componentes,componentes_unique,mascara_componentes):
        Aca puedo revisar bien el funcionamiento de argmax hacer un for para que itere y buscar el maximo
        Si no sale puedo usar el metodo de la lista
        for componente in componentes_unique: # iterar sobre la columna
            variable = maximo de columna 4    # resolver como buscar el maximo en esa columna  

   # Aca puedo imprimir solo el componente o poner toda la fila en una lista

2.2 Crear función para obtener el promedio de puntuación por tipo de componenete
    Aca puedo usar la funcion dot o mean tengo que elegir segun vaya viendo
    La idea es intentar:
    definir la funcion
    ver si tengo que iterar con un for o no segun la funcion dot me permita sacar el promedio de la
    columna

3.1 Crear funcion para saber cuantos componentes se crearon por mes
    Esto es lo mas parecido a ejercicios anteriores donde agrupe temperaturas y demas
    Esto lo puedo ordenar de mayor a menor según la cantidad de producción.    

'''


import numpy as np

componentes = np.array([
    ['2022-01-15', 'Sensor', 'L001', 85],
    ['2022-01-18', 'Batería', 'L001', 92],
    ['2022-02-10', 'Circuito', 'L002', 88],
    ['2022-02-15', 'Sensor', 'L002', 75],
    ['2022-03-05', 'Batería', 'L003', 95],
    ['2022-03-10', 'Circuito', 'L003', 82],
    ['2022-01-20', 'Sensor', 'L001', 90],
    ['2022-02-25', 'Batería', 'L002', 87],
    ['2022-03-15', 'Sensor', 'L003', 91],
])


# Componente con la mejor calidad y su puntuación
componentes_unique = np.unique(componentes[:, 1])
for componete in componentes_unique:
    #componetes_mascara = componentes[:,1] == componete
    maximo_componente = np.argmax(componentes[:, 3])
print("El componente mejor fue: ", componentes[maximo_componente, 1], " valorado en: ", componentes[maximo_componente, 3])

# Produccion por mes
meses_recorte = componentes[:, 0]
meses_unique, count = np.unique([meses[:7] for meses in meses_recorte], return_counts=True)
for prod in range(len(meses_unique)):
    print("La producción del mes", meses_unique[prod], " fue de: ", count[prod])

lista_componente = []
calificaciones_unique = np.unique(componentes[:,3])
for promedios in componentes_unique:
    tipos_componente = componentes[:,1] == promedios
    variable_componente = componentes[tipos_componente]
    calculo = np.mean(variable_componente[:,3].astype(float))
    lista_componente.append([promedios, round(calculo,2)])
print(lista_componente)