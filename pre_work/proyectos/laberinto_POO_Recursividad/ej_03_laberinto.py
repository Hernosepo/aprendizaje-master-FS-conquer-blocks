import numpy as np

class Laberinto:
    def __init__(self, filas, columnas, inicio, salida):
        self.filas = filas
        self.columnas = columnas
        self.inicio = inicio
        self.salida = salida
        self.matriz = np.ones((filas, columnas))

    def generar_ruta(self):
        for fila in range(min(self.inicio[0], self.salida[0]), max(self.inicio[0], self.salida[0]) + 1):
            self.matriz[fila , self.inicio[1]] = 0
            
        for columna in range(min(self.inicio[1], self.salida[1]), max(self.inicio[1], self.salida[1]) + 1):
            self.matriz[self.salida[0], columna] = 0
        self.matriz[self.salida] = 9

    def agregar_caminos_falsos(self, falso_inicio, falsa_salida):
        for fila_falsa in range(min(falso_inicio[0], falsa_salida[0]), max(falso_inicio[0], falsa_salida[0]) + 1):
              self.matriz[fila_falsa , self.inicio[1]] = 0
        
        for columna_falsa in range(min(falso_inicio[1], falsa_salida[1]), max(falso_inicio[1], falsa_salida[1])):
            self.matriz[falsa_salida[0], columna_falsa] = 0

        celda_falsa_fila = falsa_salida[0]
        celda_falsa_columna = falsa_salida[1]

        if self.matriz[falsa_salida] == 1 and all(
            self.matriz[vecino] != 0
            for vecino in [
                (celda_falsa_fila - 1, celda_falsa_columna),
                (celda_falsa_fila + 1, celda_falsa_columna),
                #(celda_falsa_fila, celda_falsa_columna - 1),
                #(celda_falsa_fila, celda_falsa_columna + 1)
            ]
            if 0 <= vecino[0] < self.filas and 0 <= vecino[1] < self.columnas):
            self.matriz[falsa_salida] = 4

    def mostrar_laberinto(self):
        return(self.matriz)


laberinto = Laberinto(6, 6, (0,1), (5,5))
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (2,1), falsa_salida = (2,3))
print(Laberinto.mostrar_laberinto(laberinto))

print('PRUEBAS DE DIRECCIONES Y CAMINOS FALSOS\n')

print('Prueba 1 Camino vertical con desvío lateral:')
laberinto = Laberinto(6, 6, (0, 1), (5, 1))  # Ruta principal vertical
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (2, 1), falsa_salida = (2, 3))  # Desvío horizontal
print(Laberinto.mostrar_laberinto(laberinto))

print('\n-------------------------------------\n')

print('Prueba 2 Camino diagonal con desvío lateral bajo:')
laberinto = Laberinto(6, 6, (0, 0), (5, 5))  # Ruta principal diagonal (en L)
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (4, 2), falsa_salida = (4, 4))  # Camino falso al borde
print(Laberinto.mostrar_laberinto(laberinto))

print('\n-------------------------------------\n')

print('Prueba 3 Camino en L con desvío desde fila inferior:')
laberinto = Laberinto(6, 6, (1, 0), (4, 4))  # Ruta en L
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (5, 3), falsa_salida = (5, 4))  # Camino falso en la base
print(Laberinto.mostrar_laberinto(laberinto))

print('\n-------------------------------------\n')

