'''LISTAS NUMERICAS:
1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:
[1,2,3,4,5,6,7,8,9,10].
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso 
3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
consola. 
4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
compresión).
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla 
6. Haz lo mismo con el número más alto 
7. Suma todos los elementos de la lista con y sin un bucle. 
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
el punto 2.''' 

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in numeros:
    if i % 2 == 0:
        numeros_pares_inv = numeros[::-2]
print(numeros_pares_inv)

for i in numeros: 
    print(i**2)
    
print(min(numeros))    
print(max(numeros))

suma = 0
for i in numeros:
    suma += i
print(suma)

print(numeros.index(8))

