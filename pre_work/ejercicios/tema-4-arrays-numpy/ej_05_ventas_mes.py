'''ANALISIS DE DATOS - VENTAS POR MES
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año.
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la
venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos,
etc.). Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en
cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3
columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de
NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.
(Pista 1) Tu array de entrada puede tener un a forma de este tipo:
(Pista 2: puedes cambiar el tipo de dato del array de string a entero usando
array[:,i].astype(int) )'''



import numpy as np

ventas = np.array([
    ['2022-01-01', '100', 'ropa'],
    ['2022-01-02', '200', 'alimentos'],
    ['2022-01-03', '150', 'ropa'],
    ['2022-02-01', '120', 'alimentos'],
    ['2022-02-02', '180', 'electrónicos'],
    ['2022-02-03', '200', 'alimentos'],
    ['2022-03-01', '90',  'ropa'],
    ['2022-03-02', '110', 'electrónicos'],
    ['2022-03-03', '100', 'alimentos']
])

# realizo una copia por si a acaso
ventas_mes = ventas.copy()

# Con esta linea busco la cadena de string 'YYYY-MM' en la columna 0
enero_mascara = np.char.startswith(ventas_mes[:, 0], '2022-01')
febrero_mascara = np.char.startswith(ventas_mes[:, 0], '2022-02')
marzo_mascara = np.char.startswith(ventas_mes[:, 0], '2022-03')

# ventas_enero toma la fila entera de los que complen con la condicion de enero_mascara
ventas_enero = ventas_mes[enero_mascara]
ventas_febrero = ventas_mes[febrero_mascara]
ventas_marzo = ventas_mes[marzo_mascara]

# Transformo los numeros de columna 1 en interger con astype y los sumo
suma_enero = ventas_enero[:,1].astype(int).sum()
print(suma_enero)
suma_febrero = ventas_febrero[:,1].astype(int).sum()
print(suma_febrero)
suma_marzo = ventas_marzo[:,1].astype(int).sum()
print(suma_marzo)

# Realizo la suma de las variables que obtuve de ventas por mes para obtener las ventas totales
ventas_totales_meses = suma_enero + suma_febrero + suma_marzo
print(ventas_totales_meses)



# Realizo toda la operacion nuevamente para filtrar por producto
ropa_mascara = np.char.startswith(ventas_mes[:, 2], 'ropa')
alimentos_mascara = np.char.startswith(ventas_mes[:, 2], 'alimentos')
electronicos_mascara = np.char.startswith(ventas_mes[:, 2], 'electrónicos')

ventas_ropa = ventas_mes[ropa_mascara]
ventas_alimentos = ventas_mes[alimentos_mascara]
ventas_electronicos = ventas_mes[electronicos_mascara]

suma_ropa = ventas_ropa[:,1].astype(int).sum()
print(suma_ropa)
suma_alimentos = ventas_alimentos[:,1].astype(int).sum()
print(suma_alimentos)
suma_electronicos = ventas_electronicos[:,1].astype(int).sum()
print(suma_electronicos)

ventas_totales_productos = suma_alimentos + suma_electronicos + suma_ropa
print(ventas_totales_productos)