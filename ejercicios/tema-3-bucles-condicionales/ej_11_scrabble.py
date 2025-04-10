'''SCRABBLE:
Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano.'''

mano_scrabble = ["A1", "Q5", "D2", "Z10", "B3", "E1", "I1", "I1"]
suma_mano_scrabble = 0

for ficha_scrabble in mano_scrabble:    # itero sobre cada string de la lista mano_scrabble
    numero_scrabble = int(ficha_scrabble[1:]) # realizo un corte a partir de la posicion 1 y lo convierto en interger
    suma_mano_scrabble = suma_mano_scrabble + numero_scrabble # acumulo y sumo los intergers a la variable declarada en 0 desde el principio
print("La suma de las fichas de esta mano es: ", suma_mano_scrabble)
