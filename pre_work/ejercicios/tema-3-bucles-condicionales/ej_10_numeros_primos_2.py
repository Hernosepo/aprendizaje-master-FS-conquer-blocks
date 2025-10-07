'''NUMEROS PRIMOS 2:
Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados'''

lista_prueba = [2, 3, 8, 31, 48, 55, 66, 73, 80, 97]
counter_primo = 0
suma_primo = 0
lista_primos_encontrados = []

for numeros in lista_prueba: # numeros recorre cada interger de la lista_prueba
    its_primo = True         # its_primo les da un valor True por defecto a todos los numeros
    for numero in range(2, numeros):   # numero va a aislar cada interger y los va a pasar por el condicional
        if numeros % numero == 0: # si ese interger aislado cumple con la condicion
            its_primo = False # le damos el valor de false y descartamos
    if its_primo: # si its_primo es True entonces realizamos lo siguiente
        lista_primos_encontrados.append(numeros)
        counter_primo = counter_primo + 1
        suma_primo = suma_primo + numeros
print("La lista de numeros primos encontrados es la siguiente: ", lista_primos_encontrados)
print("La cantidad de numeros primos es: ", counter_primo)
print("La suma de los numeros primos encontrados es: ", suma_primo)